#!/usr/bin/env python
import subprocess
interface = input("Enter interface to be changed>")
new_mac = input("Enter new mac address>")
subprocess.call("ifconfig " + interface + " down", shell=True)
subprocess.call("ifconfig " + interface + " hw ether " + new_mac, shell=True)
subprocess.call("ifconfig " + interface + " up", shell=True)

