#!/usr/bin/python

import nmap

nm = nmap.PortScannerAsync()
def callback_result(host, scan_result):
    print ('------------------')
    print (host, scan_result)
    
nm.scan('127.0.0.1', arguments="-O -v",
callback=callback_result)
while nm.still_scanning():
    print("Waiting >>>")
    nm.wait(2)
    nm1 = nmap.PortScanner()
a = nm1.nmap_version()
print (a)