# !/usr/bin/env python
import subprocess
subprocess.call("ifconfig eth0 down", shell=True)
subprocess.call("ifconfig eth0 hw ether 14:26:39:54:95:70", shell=True)
subprocess.call("ifconfig eth0 up", shell=True)
