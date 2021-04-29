#!/usr/bin/env python
import scapy.all as scapy
from scapy.layers import http
def sniff(interface):
    scapy.sniff(iface=interface, store=False, prn=process_sniffed_packet)
def process_sniffed_packet(packet):
    if(packet.haslayer(http.HTTPRequest)):
        url = packet[http.HTTPRequest].Host + packet[http.HTTPRequest].Path
        print(url)
sniff("eth0")