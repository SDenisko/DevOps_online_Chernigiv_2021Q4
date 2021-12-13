For accept  internet to internal network is needed next configurations:

VM1 should has two network adapters, first for internet, second - internal network:

<img src="https://github.com/SDenisko/DevOps_online_Chernigiv_2021Q4/blob/6f55bdef589f62984ab3ff057e437642dd3c3600/task6.1/images/VM1external.JPG" width="300">


<img src="https://github.com/SDenisko/DevOps_online_Chernigiv_2021Q4/blob/6f55bdef589f62984ab3ff057e437642dd3c3600/task6.1/images/VM1internal.JPG" width="300">

<img src="https://github.com/SDenisko/DevOps_online_Chernigiv_2021Q4/blob/6f55bdef589f62984ab3ff057e437642dd3c3600/task6.1/images/VM1netplan.JPG" width="300">



For the  VM2 one network adapter is enough:

<img src="https://github.com/SDenisko/DevOps_online_Chernigiv_2021Q4/blob/6f55bdef589f62984ab3ff057e437642dd3c3600/task6.1/images/VM2internal.JPG" width="300">

<img src="https://github.com/SDenisko/DevOps_online_Chernigiv_2021Q4/blob/6f55bdef589f62984ab3ff057e437642dd3c3600/task6.1/images/VM2netplan.JPG" width="300">

For the VM1 is needed next changes:
 - for allow forwarding uncommit the "net.ipv4.ip_forward=1" line  in the /etc/sysctl.conf file.

<img src="https://github.com/SDenisko/DevOps_online_Chernigiv_2021Q4/blob/6f55bdef589f62984ab3ff057e437642dd3c3600/task6.1/images/vm1sysctl.JPG" width="300">


 - add rules:

	iptables -t nat -A POSTROUTING -o eth0 -j MASQUERADE

	iptables -A FORWARD -p udp --dport 53 -j ACCEPT


Let's check results:


 - ping from the VM2 to the VM1:

	mrbit@clonedevopsonline:~$ ping 192.168.2.1

	PING 192.168.2.1 (192.168.2.1) 56(84) bytes of data.

	64 bytes from 192.168.2.1: icmp_seq=1 ttl=64 time=0.298 ms

	64 bytes from 192.168.2.1: icmp_seq=2 ttl=64 time=0.443 ms

	64 bytes from 192.168.2.1: icmp_seq=3 ttl=64 time=0.577 ms


 - ping from the VM2 to 8.8.8.8:

	 mrbit@clonedevopsonline:~$ ping 8.8.8.8

	PING 8.8.8.8 (8.8.8.8) 56(84) bytes of data.

	64 bytes from 8.8.8.8: icmp_seq=1 ttl=110 time=89.4 ms

	64 bytes from 8.8.8.8: icmp_seq=2 ttl=110 time=73.0 ms

	64 bytes from 8.8.8.8: icmp_seq=3 ttl=110 time=64.5 ms

 - route command on the VM2:

	mrbit@clonedevopsonline:~$ route

	Kernel IP routing table

	Destination     Gateway         Genmask         Flags Metric Ref    Use Iface

	default         192.168.2.1     0.0.0.0         UG    0      0        0 enp0s3

	192.168.2.0     0.0.0.0         255.255.255.0   U     0      0        0 enp0s3


	mrbit@clonedevopsonline:~$ traceroute 4.4.4.5

	traceroute to 4.4.4.5 (4.4.4.5), 30 hops max, 60 byte packets

	 1  192.168.2.1 (192.168.2.1)  0.299 ms  0.599 ms  0.569 ms

	 2  10.0.2.2 (10.0.2.2)  0.646 ms  0.756 ms  0.447 ms


 - Determine, which IP belongs to the epam.com resource:

	mrbit@clonedevopsonline:~$ nslookup epam.com

	Server:         8.8.4.4

	Address:        8.8.4.4#53

	
	Non-authoritative answer:

	Name:   epam.com

	Address: 3.214.134.159

 - Determine default gateway for host machine:

	IPv4 Route Table

	===========================================================================

	Active Routes:

	Network Destination        Netmask          Gateway       Interface  Metric

	          0.0.0.0          0.0.0.0    192.168.96.22   192.168.96.211     55

	       10.10.56.0    255.255.255.0         On-link        10.10.56.1    281

	       10.10.56.1  255.255.255.255         On-link        10.10.56.1    281

	     10.10.56.255  255.255.255.255         On-link        10.10.56.1    281

	        127.0.0.0        255.0.0.0         On-link         127.0.0.1    331

	        127.0.0.1  255.255.255.255         On-link         127.0.0.1    331

	  127.255.255.255  255.255.255.255         On-link         127.0.0.1    331

	     192.168.56.0    255.255.255.0         On-link      192.168.56.1    281

	     192.168.56.1  255.255.255.255         On-link      192.168.56.1    281

	   192.168.56.255  255.255.255.255         On-link      192.168.56.1    281

	     192.168.96.0    255.255.255.0         On-link    192.168.96.211    311

	   192.168.96.211  255.255.255.255         On-link    192.168.96.211    311

	   192.168.96.255  255.255.255.255         On-link    192.168.96.211    311

	        224.0.0.0        240.0.0.0         On-link         127.0.0.1    331

	        224.0.0.0        240.0.0.0         On-link      192.168.56.1    281

	        224.0.0.0        240.0.0.0         On-link        10.10.56.1    281

	        224.0.0.0        240.0.0.0         On-link    192.168.96.211    311

	  255.255.255.255  255.255.255.255         On-link         127.0.0.1    331

	  255.255.255.255  255.255.255.255         On-link      192.168.56.1    281

	  255.255.255.255  255.255.255.255         On-link        10.10.56.1    281

	  255.255.255.255  255.255.255.255         On-link    192.168.96.211    311

	===========================================================================



 - traceroute to the google.com from VM1 is very strange:


<img src="https://github.com/SDenisko/DevOps_online_Chernigiv_2021Q4/blob/6f55bdef589f62984ab3ff057e437642dd3c3600/task6.1/images/traceroute_to_the_google.JPG" width="300">



