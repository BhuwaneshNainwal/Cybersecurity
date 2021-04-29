#!/usr/bin/env python
import scapy.all as scapy

def scan(ip):
    arp_request = scapy.ARP()
    arp_request.pdst = ip
    # scapy.ARP(pdst = ip)
    print(arp_request.summary())
    scapy.ls(scapy.ARP())
scan("10.0.2.1/24")