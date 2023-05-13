#!/usr/bin/env python

import subprocess
import optparse


def get_arguments():
    parser = optparse.OptionParser()  # created an object for parsing
    parser.add_option("-i", "--interface", dest="interface", help="Interface to change its MAC address")
    parser.add_option("-m", "--mac", dest="new_mac", help="New MAC Address")
    (options, arguments) = parser.parse_args()
    if not options.interface:
        parser.error("[-] Please specify an interface, use --help for more info.")
    elif not options.new_mac:
        parser.error("[-] Please specify a new mac, use --help for more info.")
    return options


def change_mac(interface, new_mac):
    print("[+] Changing MAC Address to", new_mac)
    subprocess.call(["ifconfig", interface, "down"])
    subprocess.call(["ifconfig", interface, "hw", "ether", new_mac])
    subprocess.call(["ifconfig", interface, "up"])
    subprocess.call(["ifconfig"])


options = get_arguments()  # created a variable for arguments and options
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
