#!/usr/bin/env python

import subprocess
import optparse


def change_mac(interface, new_mac):
    print("[+] Changing MAC Address to", new_mac)
    subprocess.call(["ifconfig", interface, "down"])
    subprocess.call(["ifconfig", interface, "hw", "ether", new_mac])
    subprocess.call(["ifconfig", interface, "up"])
    subprocess.call(["ifconfig"])


parser = optparse.OptionParser()  # created an object for parsing
parser.add_option("-i", "--interface", dest="interface", help="Interface to change its MAC address")
parser.add_option("-m", "--mac", dest="new_mac", help="New MAC Address")
(options, arguments) = parser.parse_args()  # created a variable for arguments and options

change_mac(options.interface, options.new_mac)
# #!/usr/bin/env python3 version of code
# import subprocess
# import argparse
#
# parser = argparse.ArgumentParser()
# parser.add_argument("-i", "--interface", dest="interface", help="Interface to change its MAC address")
# parser.add_argument("-m", "--mac", dest="new_mac", help="New MAC Address")
#
# args = parser.parse_args()
#
# interface = args.interface
# new_mac = args.new_mac
