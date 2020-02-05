# This is for educational purposed and should never be used on a network without the owners full concent.

import socket
import subprocess
import sys
from datetime import datetime

#clear screen
subprocess.call('clear',shell=True)

#Ask for input
remoteServer = raw_input ("Enter a remote host to scan: ")
remoteServerIP = socket.gethostbyname(remoteServer)

#Print a banner with information on which host is about to be scanned
print"_"*60
print"Please wait, scanning remote host", remoteServerIP
print"_"*60

#Check what time the scan started
t1 = datetime.now()

#using the range function to specify port

try:
    for port in range(1,1025):
        sock= socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        result = sock.connect_ex((remoteServerIP, port))
        if result ==0:
            print"Port{}: Open".format(port)
        sock.close()

except KeyboardInterrupt:
    print"You pressed Ctrl+C"
    sys.exit()

except socket.gaierror:
    print 'Hostname could no be resolved. Exiting'
    sys.exit()

except socket.error:
    print 'Couldnt connect to server'
    sys.exit()

#Check time again
t2 = datetime.now()

total = t2 - t1

print 'Scanning Completed in: ', total
