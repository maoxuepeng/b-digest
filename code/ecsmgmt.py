# -*- coding:utf-8 -*-

import json

from openstack import connection

def shutdown_ecs(event, context):
  projectId = context.getUserData('projectId')
  domain = context.getUserData('domain')
  region = context.getUserData('region')
  ak = context.getUserData('ak')
  sk = context.getUserData('sk')
  whiteLists = context.getUserData('whiteLists')

  logger = context.getLogger()  
  _shutdown_ecs(logger, projectId, domain, region, ak, sk, whiteLists)


def _shutdown_ecs(logger, projectId, domain, region, ak, sk, whiteLists):
  whites = whiteLists.split(',')
  conn = connection.Connection(project_id=projectId, domain=domain, region=region, ak=ak, sk=sk) 
  servers = conn.compute.servers()
  for server in servers:
    if server.name in whites:
      logger.info("DO NOT shutdown %s because it is in white lists" % (server.name))
      continue
    if "ACTIVE" == server.status:
      logger.info("try stop server %s ..." % (server.name))
      conn.compute.stop_server(server)
      conn.compute.wait_for_server(server, status="SHUTOFF", interval=5, wait=600)
      logger.info("stop server %s success" % (server.name))
