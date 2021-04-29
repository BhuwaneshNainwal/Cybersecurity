#!/usr/bin/env python
import scapy.all as scapy
def scan(ip):
    arp_request = scapy.ARP(pdst=ip)
    broadcast = scapy.Ether()
    broadcast.dst = "ff:ff:ff:ff:ff:ff"
    # scapy.ls(scapy.Ether())
    # print(broadcast.summary())
    arp_request_broadcast = broadcast/arp_request
    #arp_request_broadcast.show()
    #answered, unanswered = scapy.srp(arp_request_broadcast, timeout=1)
    answered_list = scapy.srp(arp_request_broadcast, timeout=1, verbose=False )[0]
    # print(answered_list.summary())
    for element in answered_list:
        # print(element)
        #print(element[1].show())
        print(element[1].psrc)
        print(element[1].hwsrc)
scan("10.0.2.1/24")