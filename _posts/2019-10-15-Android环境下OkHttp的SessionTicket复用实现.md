---
key: 20191015
title: Android环境下OkHttp的SessionTicket复用实现
tags: SSL Session-Resumption SessionTicket OkHttp Android
published: false
---


#### Android 运行环境下 SessionTicket 存储空间控制

客户端Session缓存在内存与文件中，Session有两种类型：multi-use/single-use，只有multi-use类型的Session才缓存到文件。

1. RealConnection.kt
fun connect

private fun establishProtocol
    connectTls(connectionSpecSelector)

private fun connectTls(connectionSpecSelector: ConnectionSpecSelector)
      // Configure the socket's ciphers, TLS versions, and extensions.
      val connectionSpec = connectionSpecSelector.configureSecureSocket(sslSocket)
      if (connectionSpec.supportsTlsExtensions) {
        Platform.get().configureTlsExtensions(sslSocket, address.protocols)
      }


2. Platform.kt
  companion object {
    @Volatile private var platform = findPlatform()

    /** Attempt to match the host runtime to a capable Platform implementation. */
    private fun findPlatform(): Platform {
      val android10 = Android10Platform.buildIfSupported()

      if (android10 != null) {
        return android10
      }

      val android = AndroidPlatform.buildIfSupported()

      if (android != null) {
        return android
      }

3. AndroidPlatform.kt
/** Android 5+. */
class AndroidPlatform : Platform() {
  private val socketAdapters = listOfNotNull(
      StandardAndroidSocketAdapter.buildIfSupported(),
      ConscryptSocketAdapter.buildIfSupported(),
      DeferredSocketAdapter("com.google.android.gms.org.conscrypt")
  ).filter { it.isSupported() }

  override fun configureTlsExtensions(
    sslSocket: SSLSocket,
    protocols: List<@JvmSuppressWildcards Protocol>
  ) {
    // No TLS extensions if the socket class is custom.
    socketAdapters.find { it.matchesSocket(sslSocket) }
        ?.configureTlsExtensions(sslSocket, protocols)
  }

4. ConscryptSocketAdapter.kt

  override fun configureTlsExtensions(
    sslSocket: SSLSocket,
    protocols: List<Protocol>
  ) {
    // No TLS extensions if the socket class is custom.
    if (matchesSocket(sslSocket)) {
      // Enable session tickets.
      Conscrypt.setUseSessionTickets(sslSocket, true)

      // Enable ALPN.
      val names = Platform.alpnProtocolNames(protocols)
      Conscrypt.setApplicationProtocols(sslSocket, names.toTypedArray())
    }
  }

5. org.conscrypt.OpenSSLSocketImpl
public abstract void setUseSessionTickets(boolean useSessionTickets);

6. org.conscrypt.ConscryptEngineSocket extends OpenSSLSocketImpl
    @Override
    public final void setUseSessionTickets(boolean useSessionTickets) {
        engine.setUseSessionTickets(useSessionTickets);
    }

    private static ConscryptEngine newEngine(
            SSLParametersImpl sslParameters, final ConscryptEngineSocket socket) {
        SSLParametersImpl modifiedParams;
        if (Platform.supportsX509ExtendedTrustManager()) {
            modifiedParams = sslParameters.cloneWithTrustManager(
                getDelegatingTrustManager(sslParameters.getX509TrustManager(), socket));
        } else {
            modifiedParams = sslParameters;
        }
        ConscryptEngine engine = new ConscryptEngine(modifiedParams, socket.peerInfoProvider());

        // When the handshake completes, notify any listeners.
        engine.setHandshakeListener(new HandshakeListener() {
            /**
             * Protected by {@code stateLock}
             */
            @Override
            public void onHandshakeFinished() {
                // Just call the outer class method.
                socket.onHandshakeFinished();
            }
        });

        // Transition the engine state to MODE_SET
        engine.setUseClientMode(sslParameters.getUseClientMode());
        return engine;
    }

7. RealConnection.kt
private fun connectTls(connectionSpecSelector: ConnectionSpecSelector){
    ...

          // Force handshake. This can throw!
      sslSocket.startHandshake()
      // block for session establishment
      val sslSocketSession = sslSocket.session
      val unverifiedHandshake = sslSocketSession.handshake()

    ...
}

8. sslSocket 对象就是 OpenSSLSocketImpl，实现类是 org.conscrypt.ConscryptEngineSocket
public final void startHandshake() throws IOException {
    ...

    if (state == STATE_NEW) {
    state = STATE_HANDSHAKE_STARTED;
    engine.beginHandshake();
    in = new SSLInputStream();
    out = new SSLOutputStream();

    ...
}

9. ConscryptEngine.java
    @Override
    public void beginHandshake() throws SSLException {
        synchronized (ssl) {
            beginHandshakeInternal();
        }
    }

   private void beginHandshakeInternal() throws SSLException {
       ...

               try {
            // Prepare the SSL object for the handshake.
            ssl.initialize(getHostname(), channelIdPrivateKey);

            // For clients, offer to resume a previously cached session to avoid the
            // full TLS handshake.
            if (getUseClientMode()) {
                NativeSslSession cachedSession = clientSessionContext().getCachedSession(
                        getHostname(), getPeerPort(), sslParameters);
                if (cachedSession != null) {
                    cachedSession.offerToResume(ssl);
                }
            }

            maxSealOverhead = ssl.getMaxSealOverhead();
            handshake();
        
       ...
   }

    private ClientSessionContext clientSessionContext() {
        return sslParameters.getClientSessionContext();
    }

10. org.conscrypt.SSLParametersImpl 
构造函数中传递了org.conscrypt.ClientSessionContext clientSessionContext对象

11. org.conscrypt.ClientSessionContext.java
    /**
     * Gets the suitable session reference from the session cache container.
     */
    synchronized NativeSslSession getCachedSession(String hostName, int port,
            SSLParametersImpl sslParameters) {
        ...
        
        NativeSslSession session = getSession(hostName, port);
        if (session == null) {
            return null;
        }

        ...

        if (session.isSingleUse()) {   ///只用一次？
            removeSession(session);
        }
        return session;

        ...
    }

    /**
     * Finds a cached session for the given host name and port.
     *
     * @param host of server
     * @param port of server
     * @return cached session or null if none found
     */
    private NativeSslSession getSession(String host, int port) {
        ...

        //先从内存读
        synchronized (sessionsByHostAndPort) {
            List<NativeSslSession> sessions = sessionsByHostAndPort.get(key);
            if (sessions != null && sessions.size() > 0) {
                session = sessions.get(0);
            }
        }

        ...

        //内存没有，则从持久化存储读

        // Look in persistent cache.  We don't currently delete sessions from the persistent
        // cache, so we may find a multi-use (aka TLS 1.2) session after having received and
        // then used up one or more single-use (aka TLS 1.3) sessions.
        if (persistentCache != null) {
            byte[] data = persistentCache.getSessionData(host, port);
            ...
        }

        ...
    }

保存session时候，只有multi-use的session才会存储到文件，single-use的session只存储到内存

    @Override
    void onBeforeAddSession(NativeSslSession session) {
        String host = session.getPeerHost();
        int port = session.getPeerPort();
        if (host == null) {
            return;
        }

        HostAndPort key = new HostAndPort(host, port);
        putSession(key, session);

        // TODO: Do this in a background thread.
        if (persistentCache != null && !session.isSingleUse()) {
            byte[] data = session.toBytes();
            if (data != null) {
                persistentCache.putSessionData(session.toSSLSession(), data);
            }
        }
    }

判断session是single use还是multi use在org.conscrypt.NativeSslSession中
        @Override
        boolean isSingleUse() {
            return NativeCrypto.SSL_SESSION_should_be_single_use(ref.address);
        }

NativeSsl.java
    void initialize(String hostname, OpenSSLKey channelIdPrivateKey) throws IOException {
        ...

        if (parameters.useSessionTickets) {
            NativeCrypto.SSL_clear_options(ssl, this, SSL_OP_NO_TICKET);
        } else {
            NativeCrypto.SSL_set_options(
                    ssl, this, NativeCrypto.SSL_get_options(ssl, this) | SSL_OP_NO_TICKET);
        }
        ...
    }

12. SSLClientSessionCache 

13. org.conscrypt.FileClientSessionCache.java
        public synchronized void putSessionData(SSLSession session, byte[] sessionData) {
            String host = session.getPeerHost();
            if (sessionData == null) {
                throw new NullPointerException("sessionData == null");
            }

            String name = fileName(host, session.getPeerPort());
            File file = new File(directory, name);

            // Used to keep track of whether or not we're expanding the cache.
            boolean existedBefore = file.exists();

            FileOutputStream out;
            try {
                out = new FileOutputStream(file);
            } catch (FileNotFoundException e) {
                // We can't write to the file.
                logWriteError(host, file, e);
                return;
            }

            // If we expanded the cache (by creating a new file)...
            if (!existedBefore) {
                size++;

                // Delete an old file if necessary.
                makeRoom();
            }
        
        ...
        }

        /**
         * Deletes old files if necessary.
         */
        private void makeRoom() {
            if (size <= MAX_SIZE) {
                return;
            }

            indexFiles();

            // Delete LRUed files.
            int removals = size - MAX_SIZE;
            Iterator<File> i = accessOrder.values().iterator();
            do {
                delete(i.next());
                i.remove();
            } while (--removals > 0);
        }

14. org.conscrypt.NativeSsl.java
    int doHandshake() throws IOException {
        lock.readLock().lock();
        try {
            return NativeCrypto.ENGINE_SSL_do_handshake(ssl, this, handshakeCallbacks);
        } finally {
            lock.readLock().unlock();
        }
    }

handshakeCallbacks 由 ConscryptEngine 实现：

final class ConscryptEngine extends AbstractConscryptEngine implements NativeCrypto.SSLHandshakeCallbacks,
                                                         SSLParametersImpl.AliasChooser,
                                                         SSLParametersImpl.PSKCallbacks {...}

15. ConscryptEngineSocket.onHandshakeFinished()

    private void onHandshakeFinished() {
        boolean notify = false;
        synchronized (stateLock) {
            if (state != STATE_CLOSED) {
                if (state == STATE_HANDSHAKE_STARTED) {
                    state = STATE_READY_HANDSHAKE_CUT_THROUGH;
                } else if (state == STATE_HANDSHAKE_COMPLETED) {
                    state = STATE_READY;
                }

                // Unblock threads that are waiting for our state to transition
                // into STATE_READY or STATE_READY_HANDSHAKE_CUT_THROUGH.
                stateLock.notifyAll();
                notify = true;
            }
        }

        if (notify) {
            notifyHandshakeCompletedListeners();
        }
    }

16. AbstractConscryptSocket.java
    final void notifyHandshakeCompletedListeners() {
        if (listeners != null && !listeners.isEmpty()) {
            // notify the listeners
            HandshakeCompletedEvent event = new HandshakeCompletedEvent(this, getActiveSession());
            for (HandshakeCompletedListener listener : listeners) {
                try {
                    listener.handshakeCompleted(event);
                } catch (RuntimeException e) {
                    // The RI runs the handlers in a separate thread,
                    // which we do not. But we try to preserve their
                    // behavior of logging a problem and not killing
                    // the handshaking thread just because a listener
                    // has a problem.
                    Thread thread = Thread.currentThread();
                    thread.getUncaughtExceptionHandler().uncaughtException(thread, e);
                }
            }
        }
    }

5. SSLCertificateSocketFactory
SSLCertificateSocketFactory.setUseSessionTickets(...)

https://developer.android.com/reference/android/net/SSLCertificateSocketFactory.html#setUseSessionTickets(java.net.Socket,%20boolean)


## Reference

[](https://source.android.google.cn/devices/architecture/modular-system/conscrypt)