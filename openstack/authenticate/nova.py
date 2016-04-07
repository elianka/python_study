#!/usr/bin/python

from os import environ as env
import novaclient.client
nova = novaclient.client.Client("2.0", auth_url=env['OS_AUTH_URL'],
                                username=env['OS_USERNAME'],
                                api_key=env['OS_PASSWORD'],
                                project_id=env['OS_TENANT_NAME'],
                                region_name=env['OS_REGION_NAME'])

print nova.servers.list()
print nova.flavors.list()
