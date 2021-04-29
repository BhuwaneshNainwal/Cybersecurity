# !/usr/bin/env python
import subprocess
import argparse
import re

def parsing():
    parser = argparse.ArgumentParser()
    parser.add_argument("-i", "--interface", dest="interface", help="interface to be changed")
    parser.add_argument("-m", "--mac", dest="new_mac", help="new mac to be added")
    values = parser.parse_args()
    if not values.interface:
        print("[-] Please specify the interface to be changed, --help for more info")
    elif not values.new_mac:
        print("[-] Please specify the new mac address to be changed, --help for more info")
    return values


def mac_changer(interface, new_mac):
    subprocess.call(["ifconfig", interface, "down"])
    subprocess.call(["ifconfig", interface, "hw", "ether", new_mac])
    subprocess.call(["ifconfig", interface, "up"])

def get_current_mac():
    ifconfig_result = subprocess.check_output(["ifconfig", values.interface])
    # print(ifconfig_result)
    mac_address_search_result = re.search(r"\w\w:\w\w:\w\w:\w\w:\w\w:\w\w", ifconfig_result)
    if mac_address_search_result:
        return mac_address_search_result.group(0)
    else:
        print("[-] could not read mac address")

values = parsing()
current_mac=get_current_mac()
print("current mac=" + str(current_mac))
mac_changer(values.interface, values.new_mac)
current_mac = get_current_mac()
if current_mac == values.new_mac:
    print("[+] MAC address was successfully changed")
else:
    print("[-] MAC address didn't get change")




