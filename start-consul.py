#!/usr/bin/python

import sys
import os
import boto
import boto.ec2
from boto.utils import get_instance_metadata

region = get_instance_metadata()['placement']['availability-zone'][:-1]
ec2_conn = boto.ec2.connect_to_region(region)

def find_nat_instances(ec2_conn, tag, value):
    instances = ec2_conn.get_only_instances(filters= {
        "tag:%s" % tag : value,
        'instance-state-name':'running'
        })
    return [i.private_ip_address for i in instances]

command = ""
(tag, value) = sys.argv[1].split('=')
for arg in sys.argv[2:]:
    command += "%s " % str(arg)
for ip in find_nat_instances(ec2_conn, tag, value):
    command += " -retry-join %s" % ip
os.system(command)
