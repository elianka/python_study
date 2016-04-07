#!/usr/bin/python

from os import environ as env
from neutronclient.v2_0 import client as neutronclient
neutron = neutronclient.Client(auth_url=env['OS_AUTH_URL'],
                               username=env['OS_USERNAME'],
                               password=env['OS_PASSWORD'],
                               tenant_name=env['OS_TENANT_NAME'],
                               region_name=env['OS_REGION_NAME'])

nets = neutron.list_networks()
routers = neutron.list_routers()
ports = neutron.list_ports()


def print_value(val, type):
    if type == 'ports':
        val_list = val['ports']
    if type == 'networks':
        val_list = val['networks']
    if type == 'routers':
        val_list = val['routers']
    for p in val_list:
        for k,v in p.items():
            print("%s : %s" % (k,v))
        print('/n')
        
print_value(nets, 'networks')
print_value(routers, 'routers')
print_value(ports, 'ports')

