#!/usr/bin/env python

"""
Author: Stephen Sheridan
Web: http://www.sheridanresearch.com
"""

import re
from subprocess import Popen, PIPE
 
# Define IP range : based on DHCP settings on your router
prefix = "192.168.1."
network = []
numhosts = 255

# List of known devices on your network
devices = {
"MACADDRESS1" : "DESCRIPTION1",
"MACADDRESS2" : "DESCRIPTION2",
"MACADDRESS3" : "DESCRIPTION3"
}

def main():
    network = [prefix + str(i) for i in range(100, 199)]

    print '{0:18} {1:20} {2}'.format("IP", "MAC", "DESCRIPTION")
    for ip in network:
        # Run an nmap to refresh network for given IP
        pid = Popen(["/usr/local/bin/nmap", "-sn", ip], stdout=PIPE)
        s = pid.communicate()[0]
        # Run an arp command to get the mac address for given IP
        pid = Popen(["arp", "-n", ip], stdout=PIPE)
        s = pid.communicate()[0]
    
        if not (("no entry" in s) or ("incomplete" in s)):
            mac = re.search(r"(([a-f\d]{1,2}\:){5}[a-f\d]{1,2})", s).groups()[0]
            if mac in devices:
                print '{0:18} {1:20} {2}'.format(ip, mac, devices[mac])
            else:
                print '{0:18} {1:20} {2}'.format(ip, mac, "UNKNOWN")
           
if __name__ == '__main__':
    main()    
    
