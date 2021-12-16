1. Parameters of the network adapters for the VM1,VM2,VM3:


<img src="https://github.com/SDenisko/DevOps_online_Chernigiv_2021Q4/blob/0ed239496293b9af91e89bc15e81e7d49d0cfe8e/task6.2/images/vm11network.JPG" width="300">

<img src="https://github.com/SDenisko/DevOps_online_Chernigiv_2021Q4/blob/0ed239496293b9af91e89bc15e81e7d49d0cfe8e/task6.2/images/vm12network.JPG" width="300">



	enp0s3: flags=4163<UP,BROADCAST,RUNNING,MULTICAST>  mtu 1500

	        inet 10.0.2.15  netmask 255.255.255.0  broadcast 10.0.2.255

	enp0s8: flags=4163<UP,BROADCAST,RUNNING,MULTICAST>  mtu 1500

	        inet 192.168.2.1  netmask 255.255.255.0  broadcast 192.168.2.255


VM2:        

<img src="https://github.com/SDenisko/DevOps_online_Chernigiv_2021Q4/blob/0ed239496293b9af91e89bc15e81e7d49d0cfe8e/task6.2/images/vm2network.JPG" width="300">


VM3:

<img src="https://github.com/SDenisko/DevOps_online_Chernigiv_2021Q4/blob/0ed239496293b9af91e89bc15e81e7d49d0cfe8e/task6.2/images/vm3network.JPG" width="300">


2. Now we need to install and configure a DHCP server. In this case, we will use the dnsmasq package. Let's do that:



	mrbit@devopsonline:~$ sudo apt install dnsmasq



Config file there are to /etc/dnsmasq.conf:



	#DNS forwarding:

	server=8.8.4.4

	# If you want dnsmasq to change uid and gid to something other

	# than the default, edit the following lines.

	#user=dnsmasq

	#group=dnsmasq

	# If you want dnsmasq to listen for DHCP and DNS requests only on

	# specified interfaces (and the loopback) give the name of the

	# interface (eg eth0) here.

	# Repeat the line for more than one interface.

	interface=enp0s8



	# This is an example of a DHCP range where the netmask is given. This

	# is needed for networks we reach the dnsmasq DHCP server via a relay

	# agent. If you don't know what a DHCP relay agent is, you probably

	# don't need to worry about this.

	dhcp-range=192.168.2.15,192.168.2.30,255.255.255.0,12h



	# Always give the host with Ethernet address 11:22:33:44:55:66

	# the name fred and IP address 192.168.0.60 and lease time 45 minutes

	#dhcp-host=11:22:33:44:55:66,fred,192.168.0.60,45m

	dhcp-host=08:00:27:C2:A2:3A,VM2,192.168.2.20

	dhcp-host=08:00:27:36:F0:32,VM3.192.168.2.30



	# Do the same thing, but using the option name

	#dhcp-option=option:router,1.2.3.4


	dhcp-option=option:router,192.168.2.1

	dhcp-option=option:dns-server,8.8.8.8


	# The DHCP server needs somewhere on disk to keep its lease database.

	# This defaults to a sane location, but if you want to change it, use

	# the line below.


	dhcp-leasefile=/var/lib/misc/dnsmasq.leases



	# Set the DHCP server to authoritative mode. In this mode it will barge in
	# and take over the lease for any client which broadcasts on the network,
	# whether it has a record of the lease or not. This avoids long timeouts
	#  when a machine wakes up on a new network. DO NOT enable this if there's
	# the slightest chance that you might end up accidentally configuring a DHCP
	# server for your campus/company accidentally. The ISC server uses
	# the same option, and this URL provides more information:
	# http://www.isc.org/files/auth.html

	dhcp-authoritative


The next step, should be disable systemd-resolved service and restart dnsmasq service:


	sudo systemctl disable systemd-resolved
	sudo systemctl stop systemd-resolved

	sudo systemctl start dnsmasq
	sudo systemctl status dnsmasq




Check the results:



VM2:



	mrbit@devopsonline:~$ ssh mrbit@192.168.2.20 'cat /etc/netplan/00-installer-config.yaml && ifconfig -a'

	mrbit@192.168.2.20's password:

	# This is the network config written by 'subiquity'

	network:

	  ethernets:

	    enp0s3:

	      dhcp4: true

	#      addresses: [192.168.2.16/24]

	#      gateway4: 192.168.2.1

	#      nameservers:

	#        addresses: [8.8.8.8]

	  version: 2


	enp0s3: flags=4163<UP,BROADCAST,RUNNING,MULTICAST>  mtu 1500

	        inet 192.168.2.20  netmask 255.255.255.0  broadcast 192.168.2.255



VM3:


	mrbit@devopsonline:~$ ssh mrbit@192.168.2.30 'cat /etc/netplan/00-installer-config.yaml && ifconfig -a'

	mrbit@192.168.2.30's password:

	# This is the network config written by 'subiquity'

	network:

	  ethernets:

	    enp0s3:

	      dhcp4: true

	#      addresses: [192.168.2.17/24]

	#      gateway4: 192.168.2.1

	#      nameservers:

	#        addresses: [8.8.8.8]

	  version: 2

	enp0s3: flags=4163<UP,BROADCAST,RUNNING,MULTICAST>  mtu 1500

	        inet 192.168.2.30  netmask 255.255.255.0  broadcast 192.168.2.255

3. DNSMASQ package has a DNS server. Let's use it. 

First of all we should change /etc/dnsmasq.conf file:


<img src="https://github.com/SDenisko/DevOps_online_Chernigiv_2021Q4/blob/0ed239496293b9af91e89bc15e81e7d49d0cfe8e/task6.2/images/dnsmasq_dnsconfig.JPG" width="300">



Let's check results:



<img src="https://github.com/SDenisko/DevOps_online_Chernigiv_2021Q4/blob/0ed239496293b9af91e89bc15e81e7d49d0cfe8e/task6.2/images/dnsmasq_status.JPG" width="300">




	# ping VM2

	PING VM2 (192.168.2.20) 56(84) bytes of data.

	64 bytes from VM2 (192.168.2.20): icmp_seq=1 ttl=64 time=0.461 ms

	64 bytes from VM2 (192.168.2.20): icmp_seq=2 ttl=64 time=0.496 ms



	# ping VM3

	PING VM3 (192.168.2.30) 56(84) bytes of data.

	64 bytes from VM3 (192.168.2.30): icmp_seq=1 ttl=64 time=0.529 ms

	64 bytes from VM3 (192.168.2.30): icmp_seq=2 ttl=64 time=0.475 ms

	64 bytes from VM3 (192.168.2.30): icmp_seq=3 ttl=64 time=0.449 ms

DNS server works!



	Dynamic Routing


For this task we should install and configure quagga package on the VM1-VM3.
Let's start:

VM1: 

1. apt install quagga

2. create zebra.conf and ospfd.conf

sudo touch /etc/quagga/zebra.conf
sudo touch /etc/quagga/ospfd.conf

3. Make owner of the files quagga user and quagga group:

sudo chown quagga:quagga /etc/quagga/zebra.conf
sudo chown quagga:quagga /etc/quagga/ospfd.conf

4. Add config to the zebra.conf and to the ospfd.conf files: 

root@devopsonline:/home/mrbit# cat /etc/quagga/zebra.conf

	hostname devopsonline

	password 123487654@

	enable password 123487654@

	log file /var/log/quagga/zebra.log

	!

	line vty

	!



root@devopsonline:/home/mrbit# cat /etc/quagga/ospfd.conf


	log file /var/log/quagga/ospfd.log

	router ospf

	!router id got from the DHCP

	 ospf router-id 192.168.2.1

	 log-adjacency-changes

	!to announce the routs lifted automaticaly

	 redistribute kernel

	!to annouce the routs before network connection

	 redistribute connected

	!to announce static routs

	 redistribute static

	!network and zone number of neighboring routers

	 network 192.168.2.0/24 area 1

	!
	!network, which will be annonced, in our case this is 192.168.2.0 /24

	access-list 20 permit 192.168.2.0 0.0.0.255

	access-list 20 deny any

	!
	line vty
	!

5. Check and start service:

sudo service zebra start
sudo service zebra status

sudo service ospfd start
sudo service ospfd status


VM2:


1. apt install quagga

2. create zebra.conf and ospfd.conf

sudo touch /etc/quagga/zebra.conf
sudo touch /etc/quagga/ospfd.conf

3. Make owner of the files quagga user and quagga group:

sudo chown quagga:quagga /etc/quagga/zebra.conf
sudo chown quagga:quagga /etc/quagga/ospfd.conf

4. Add config to the zebra.conf and to the ospfd.conf files:

root@devopsonline:/home/mrbit# cat /etc/quagga/zebra.conf

        hostname clonedevopsonline

        password 123487654@

        enable password 123487654@

        log file /var/log/quagga/zebra.log

        !

        line vty

        !



root@devopsonline:/home/mrbit# cat /etc/quagga/ospfd.conf


        log file /var/log/quagga/ospfd.log

        router ospf

        !router id got from the DHCP

         ospf router-id 192.168.2.20

         log-adjacency-changes

        !to announce the routs lifted automaticaly

         redistribute kernel

        !to annouce the routs before network connection

         redistribute connected

        !to announce static routs

         redistribute static

        !network and zone number of neighboring routers

         network 192.168.2.0/24 area 1

        !
        !network, which will be annonced, in our case this is 192.168.2.0 /24

        access-list 20 permit 192.168.2.0 0.0.0.255

        access-list 20 deny any

        !
        line vty
        !

5. Check and start service:

sudo service zebra start
sudo service zebra status

sudo service ospfd start
sudo service ospfd status


VM3:


1. apt install quagga

2. create zebra.conf and ospfd.conf


sudo touch /etc/quagga/zebra.conf
sudo touch /etc/quagga/ospfd.conf


3. Make owner of the files quagga user and quagga group:

sudo chown quagga:quagga /etc/quagga/zebra.conf
sudo chown quagga:quagga /etc/quagga/ospfd.conf

4. Add config to the zebra.conf and to the ospfd.conf files:

root@devopsonline:/home/mrbit# cat /etc/quagga/zebra.conf

        hostname clonedevopsonline2

        password 123487654@

enable password 123487654@

        log file /var/log/quagga/zebra.log

        !

        line vty

        !



root@devopsonline:/home/mrbit# cat /etc/quagga/ospfd.conf


        log file /var/log/quagga/ospfd.log

        router ospf

        !router id got from the DHCP

         ospf router-id 192.168.2.30

         log-adjacency-changes

        !to announce the routs lifted automaticaly

         redistribute kernel

        !to annouce the routs before network connection

         redistribute connected

        !to announce static routs

         redistribute static

        !network and zone number of neighboring routers

         network 192.168.2.0/24 area 1

        !
        !network, which will be annonced, in our case this is 192.168.2.0 /24

        access-list 20 permit 192.168.2.0 0.0.0.255

        access-list 20 deny any

        !
        line vty
        !

5. Check and start service:
sudo service zebra start
sudo service zebra status

sudo service ospfd start
sudo service ospfd status






