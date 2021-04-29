# !/usr/bin/env python
import subprocess
import argparse

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

values = parsing()
mac_changer(values.interface, values.new_mac)
