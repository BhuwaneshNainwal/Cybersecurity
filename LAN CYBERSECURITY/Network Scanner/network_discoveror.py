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
    answered_list = scapy.srp(arp_request_broadcast, timeout=1, verbose=False)[0]
    # print(answered_list.summary())
    client_list = []
    for element in answered_list:
        # print(element)
        #print(element[1].show())
        client_dict = {"ip": element[1].psrc, "MAC": element[1].hwsrc}
        client_list.append(client_dict)
    return client_list
def print_result(results_list):
    print("IP \t\t\t MAC ADDRESS")
    for client in results_list:
        print(client["ip"] + "\t\t " + client["MAC"])
scan_result=scan("10.0.2.1/24")
print_result(scan_result)