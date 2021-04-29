#!/usr/bin/env python
import scapy.all as scapy
def scan(ip):
    arp_request = scapy.ARP(pdst=ip)
    broadcast = scapy.Ether()
    broadcast.dst = "ff:ff:ff:ff:ff:ff"
    # scapy.ls(scapy.Ether())
    # print(broadcast.summary())
    arp_request_broadcast = broadcast/arp_request
    arp_request_broadcast.show()
scan("10.0.2.1/24")