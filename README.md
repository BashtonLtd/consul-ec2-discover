# Consul EC2 Discover

A Python script to discover Consul servers from the EC2 API, and start
Consul accordingly

Requires boto

Currently no error checking of any sort.

Example usage:

`start-consul.py Name=NAT /usr/bin/consul -server -bootstrap-expect 3`
