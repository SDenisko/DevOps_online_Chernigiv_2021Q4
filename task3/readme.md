Cisco Packet Tracer is an excellent utility for network exploration. This is my first experience with it, and I got a lot of positive emotions.
I created three workplaces with different equipment: PCs, servers, switches, Wi-Fi router and routers. I made the setting of ip addresses and checked the connection with the ping utility.
Packet Tracer PC Command Line 1.0
C:\>ping 10.87.23.20

Pinging 10.87.23.20 with 32 bytes of data:

Reply from 10.87.23.20: bytes=32 time<1ms TTL=128
Reply from 10.87.23.20: bytes=32 time=1ms TTL=128
Reply from 10.87.23.20: bytes=32 time<1ms TTL=128
Reply from 10.87.23.20: bytes=32 time<1ms TTL=128

Ping statistics for 10.87.23.20:
    Packets: Sent = 4, Received = 4, Lost = 0 (0% loss),
Approximate round trip times in milli-seconds:
    Minimum = 0ms, Maximum = 1ms, Average = 0ms

C:\>ping 10.87.23.100

Pinging 10.87.23.100 with 32 bytes of data:

Reply from 10.87.23.100: bytes=32 time<1ms TTL=128
Reply from 10.87.23.100: bytes=32 time=1ms TTL=128
Reply from 10.87.23.100: bytes=32 time<1ms TTL=128
Reply from 10.87.23.100: bytes=32 time=1ms TTL=128

Ping statistics for 10.87.23.100:
    Packets: Sent = 4, Received = 4, Lost = 0 (0% loss),
Approximate round trip times in milli-seconds:
    Minimum = 0ms, Maximum = 1ms, Average = 0ms

As you can see, ping packets pass between nodes. 
But, there are many other packages of different protocols on the network. We can catch one pack and look inside. We can use the WireShark tool for this.
Any pack should has inside desttination  mac addr, sourse mac addr, destination port, soure port, destination ip addr, sourse ip addr and type.

<img src="https://github.com/SDenisko/DevOps_online_Chernigiv_2021Q4/blob/fd4c9f0591d9765754e090503053636f9025ac79/task3/images/1_2/wireshark.jpg" width="500">


Lets check with wo we exchange of packeges:

<img src="https://github.com/SDenisko/DevOps_online_Chernigiv_2021Q4/blob/fd4c9f0591d9765754e090503053636f9025ac79/task3/images/1_2/whois_ip.JPG" width="250">



In second task need create native Internet  and configure VLANs.
First of all let's divide ip range:

ip			mask	prefix	hosts		broadcast
33.6.87.0	255.255.255.192	26	33.6.87.62	33.6.87.63
33.6.87.64	255.255.255.192	26	33.6.87.126	33.6.87.127
33.6.87.128	255.255.255.192	26	33.6.87.190	33.6.87.191
33.6.87.192	255.255.255.192	26	33.6.87.254	33.6.87.255

After configuring the IP addresses, mask and gateways on the PC, we can see that the PC and the gateway are avaliable to each other:

Packet Tracer PC Command Line 1.0
C:\>ping 10.87.23.1

Pinging 10.87.23.1 with 32 bytes of data:

Reply from 10.87.23.1: bytes=32 time<1ms TTL=255
Reply from 10.87.23.1: bytes=32 time<1ms TTL=255
Reply from 10.87.23.1: bytes=32 time=1ms TTL=255
Reply from 10.87.23.1: bytes=32 time<1ms TTL=255

Ping statistics for 10.87.23.1:
    Packets: Sent = 4, Received = 4, Lost = 0 (0% loss),
Approximate round trip times in milli-seconds:
    Minimum = 0ms, Maximum = 1ms, Average = 0ms

Let's change mask of subnetwork in DataCenter work space to 255.255.255.192 and check connection with tracer tool.

With mask 255.255.255.0 all servers are in one subnetwork and we have one HOP between them.

If servers have mask 255.255.255.192 (they are in different subnetworks) and gatewey has 255.255.255.0 (it include subnetworks of all servers) mask, than we have two HOPS: server1>gateway and gateway>server2.   

tracert to gateway:

C:\>tracert 6.87.23.1

Tracing route to 6.87.23.1 over a maximum of 30 hops: 

  1   *         *         1 ms      6.87.23.1

Trace complete.

tracert to server:
C:\>tracert 6.87.23.150

Tracing route to 6.87.23.150 over a maximum of 30 hops: 

  1   0 ms      1 ms      0 ms      6.87.23.1
  2   1 ms      0 ms      14 ms     6.87.23.150

Trace complete.

And now let's configure VLANs 2,3,4 on DataCenter switch and check result.
The first step is to  create VLANs and then attach servers to it own VLAN.
As we know, VLANs are isolated from each other. So, if each server is in its own VLAN, then the servers are also isolated from each other. 
Let's check:

Packet Tracer SERVER Command Line 1.0
C:\>ping 6.87.23.100

Pinging 6.87.23.100 with 32 bytes of data:

Request timed out.
Request timed out.
Request timed out.
Request timed out.

Ping statistics for 6.87.23.100:
    Packets: Sent = 4, Received = 0, Lost = 4 (100% loss),

C:\>tracer 6.87.23.100
Invalid Command.

C:\>tracert 6.87.23.100

Tracing route to 6.87.23.100 over a maximum of 30 hops: 

  1   *         *         *         Request timed out.
  2   *         *         *         Request timed out.
  3   *         *         *         Request timed out.
  4   *         *         *         Request timed out.
  5   *         *         *         Request timed out.
  6   *         *         *         Request timed out.
  7   *         *         *         Request timed out.
  8   *         *         *         Request timed out.
  9   *         *         *         Request timed out.

Trace complete.

I tried to do an additional task with VLAN, but the result confused me. In our teaching group, we have two positions: there should be communication between servers and there should be no communication between servers. In my case, there was no connection, I checked the ping. But I think there should be such a connection. Configuration: The DataCenter switch has three VLANs 2, 3, 4 connected to the servers and a Gig0 / 1 port configured as a "trunk". The ISP3 router has a Gig0 / 0 port configured with three subnets: gig0 / 0.2 ip 6.87.23.1/26, gig0 / 0.3 ip 6.87.23.65/26, gig0 / 0.4 ip 6.87.23.129/26.
Servers have IP addresses and masks from their ranges and VLANs.
   And there is no ping between servers. Perhaps this is due to the absence of routes between VLANs.
I want know trues!! :)

<img src="https://github.com/SDenisko/DevOps_online_Chernigiv_2021Q4/blob/fd4c9f0591d9765754e090503053636f9025ac79/task3/images/1_2/VLAN1.jpg" width="250">

<img src="https://github.com/SDenisko/DevOps_online_Chernigiv_2021Q4/blob/fd4c9f0591d9765754e090503053636f9025ac79/task3/images/1_2/VLAN2.jpg" width="250">

<img src="https://github.com/SDenisko/DevOps_online_Chernigiv_2021Q4/blob/fd4c9f0591d9765754e090503053636f9025ac79/task3/images/1_2/VLAN3.jpg" width="250">

<img src="https://github.com/SDenisko/DevOps_online_Chernigiv_2021Q4/blob/fd4c9f0591d9765754e090503053636f9025ac79/task3/images/1_2/VLAN4.jpg" width="250">

<img src="https://github.com/SDenisko/DevOps_online_Chernigiv_2021Q4/blob/fd4c9f0591d9765754e090503053636f9025ac79/task3/images/1_2/VLAN5.jpg" width="250">

<img src="https://github.com/SDenisko/DevOps_online_Chernigiv_2021Q4/blob/fd4c9f0591d9765754e090503053636f9025ac79/task3/images/1_2/VLAN6.jpg" width="250">


Routing configuration.

We can detect two types of routing: manual and automatic.
For manual routing, we need to write the subnet to which we need access and ip address of next hop to the routing table. For example, if we need access to 4.25.99.4/24 from WRT 300, should write  to route table of ISP2: 4.25.99.0 255.255.255.0 and next hop 35.4.99.130.  
Check:

tracert client 3 thrue wifi router:
C:\>tracert 10.99.25.2

Tracing route to 10.99.25.2 over a maximum of 30 hops: 

  1   15 ms     21 ms     23 ms     192.168.0.1
  2   *         *         *         Request timed out.
  3   *         *         *         Request timed out.
  4   21 ms     8 ms      16 ms     10.99.25.2

Trace complete.

C:\>tracert 4.25.99.4

Tracing route to 4.25.99.4 over a maximum of 30 hops: 

  1   18 ms     24 ms     54 ms     192.168.0.1
  2   *         *         *         Request timed out.
  3   *         *         *         Request timed out.
  4   *         24 ms     15 ms     4.25.99.4

Trace complete.

tracert Client1:
C:\>tracert 4.25.99.4

Tracing route to 4.25.99.4 over a maximum of 30 hops: 

  1   0 ms      0 ms      1 ms      10.99.25.1
  2   1 ms      11 ms     1 ms      35.4.99.66
  3   12 ms     1 ms      1 ms      4.25.99.4

Trace complete.

C:\>tracert 35.4.99.194

Tracing route to 35.4.99.194 over a maximum of 30 hops: 

  1   0 ms      0 ms      0 ms      10.99.25.1
  2   1 ms      1 ms      0 ms      35.4.99.2
  3   *         *         *         Request timed out.
  4   *         *         *         Request timed out.
  5   *         *         *         Request timed out.
  6   *         *         *         Request timed out.
  7   *         *         *         Request timed out.
  8   *         *         *         Request timed out.

tracert server 1:

C:\>tracert 10.99.25.2

Tracing route to 10.99.25.2 over a maximum of 30 hops: 

  1   0 ms      0 ms      0 ms      4.25.99.1
  2   1 ms      1 ms      0 ms      35.4.99.65
  3   14 ms     12 ms     10 ms     10.99.25.2

Trace complete.

C:\>tracert 35.4.99.194

Tracing route to 35.4.99.194 over a maximum of 30 hops: 

  1   0 ms      1 ms      1 ms      4.25.99.1
  2   0 ms      11 ms     11 ms     35.4.99.129
  3   *         *         *         Request timed out.
  4   *         *         *         Request timed out.
  5   *         *         *         Request timed out.
  6   *         *         *         Request timed out.
  7   *         *         *         Request timed out.
  8   *         *         *         Request timed out.


"Request timed out" received from WRT300 because its firewall was dropping packets.

Automatic routing uses RIP. So, you should enable it in routers and specify the addresses in the class format (35.0.0.0 10.0.0.0) that they have on the ports. 
Let's check result:

Client 3:
C:\>
C:\>tracert 10.99.25.2

Tracing route to 10.99.25.2 over a maximum of 30 hops: 

  1   20 ms     4 ms      24 ms     192.168.0.1
  2   *         *         *         Request timed out.
  3   *         *         *         Request timed out.
  4   27 ms     32 ms     23 ms     10.99.25.2

Trace complete.

C:\>tracert 4.25.99.4

Tracing route to 4.25.99.4 over a maximum of 30 hops: 

  1   27 ms     23 ms     29 ms     192.168.0.1
  2   *         *         *         Request timed out.
  3   *         *         *         Request timed out.
  4   31 ms     15 ms     24 ms     4.25.99.4

Trace complete.

Client 1:
C:\>tracert 4.25.99.4

Tracing route to 4.25.99.4 over a maximum of 30 hops: 

  1   0 ms      0 ms      0 ms      10.99.25.1
  2   0 ms      0 ms      1 ms      35.4.99.66
  3   11 ms     10 ms     12 ms     4.25.99.4

Trace complete.

C:\>tracert 35.4.99.194

Tracing route to 35.4.99.194 over a maximum of 30 hops: 

  1   0 ms      1 ms      10 ms     10.99.25.1
  2   0 ms      0 ms      0 ms      35.4.99.2
  3   *         *         *         Request timed out.
  4   *         *         *         Request timed out.
  5   *         *         *         Request timed out.
  6   *         *         *         Request timed out.




    DHCP DNS NAT

DHCP (Dynamic Host Configuration Protocol) allows you to automatically configure your network (IP address, mask, gateway, DNS server IP address) on your PC. 
Let's configure DHCP server in Interprise Server:

<img src="https://github.com/SDenisko/DevOps_online_Chernigiv_2021Q4/blob/7624c1eeeaacb8604f29a7fe26f4a0a423166f73/task3/images/4/dhcp_server.JPG" width="300">

Enable DHCP on clients PCs in our project and check network using Ping tool: 


<img src="https://github.com/SDenisko/DevOps_online_Chernigiv_2021Q4/blob/7624c1eeeaacb8604f29a7fe26f4a0a423166f73/task3/images/4/dhcp_client2.JPG" width="300">


ping Client 2 to Client 1:

C:\>ping 10.87.23.2

Pinging 10.87.23.2 with 32 bytes of data:

Reply from 10.87.23.2: bytes=32 time=37ms TTL=125
Reply from 10.87.23.2: bytes=32 time=22ms TTL=125
Reply from 10.87.23.2: bytes=32 time=16ms TTL=125
Reply from 10.87.23.2: bytes=32 time=23ms TTL=125

Ping statistics for 10.87.23.2:
    Packets: Sent = 4, Received = 4, Lost = 0 (0% loss),
Approximate round trip times in milli-seconds:
    Minimum = 16ms, Maximum = 37ms, Average = 24ms

C:\>


Enable DHCP on the Client 3 and configure DHCP server on the wifi router:


<img src="https://github.com/SDenisko/DevOps_online_Chernigiv_2021Q4/blob/7624c1eeeaacb8604f29a7fe26f4a0a423166f73/task3/images/4/dhcp_wifi.JPG" width="300">


<img src="https://github.com/SDenisko/DevOps_online_Chernigiv_2021Q4/blob/7624c1eeeaacb8604f29a7fe26f4a0a423166f73/task3/images/4/dhcp_client3.JPG" width="300">

ping Client 3 to Client 1:

C:\>ping 10.87.23.2

Pinging 10.87.23.2 with 32 bytes of data:

Reply from 10.87.23.2: bytes=32 time=37ms TTL=125
Reply from 10.87.23.2: bytes=32 time=22ms TTL=125
Reply from 10.87.23.2: bytes=32 time=16ms TTL=125
Reply from 10.87.23.2: bytes=32 time=23ms TTL=125

Ping statistics for 10.87.23.2:
    Packets: Sent = 4, Received = 4, Lost = 0 (0% loss),
Approximate round trip times in milli-seconds:
    Minimum = 16ms, Maximum = 37ms, Average = 24ms

C:\>

	DNS Server

DNS (Domain Name System) server allows words to be used as IP address. Let's configure our DNS Server, add it to DHCP server and try how it work.



<img src="https://github.com/SDenisko/DevOps_online_Chernigiv_2021Q4/blob/7624c1eeeaacb8604f29a7fe26f4a0a423166f73/task3/images/4/dns_srv.JPG" width="300">

<img src="https://github.com/SDenisko/DevOps_online_Chernigiv_2021Q4/blob/7624c1eeeaacb8604f29a7fe26f4a0a423166f73/task3/images/4/dhcp_dns_client1.JPG" width="300">



Ping from Client1 to WebServer1:

C:\>ping domain1.com

Pinging 4.25.99.2 with 32 bytes of data:

Request timed out.
Reply from 4.25.99.2: bytes=32 time=11ms TTL=126
Reply from 4.25.99.2: bytes=32 time=10ms TTL=126
Reply from 4.25.99.2: bytes=32 time=24ms TTL=126

Ping statistics for 4.25.99.2:
    Packets: Sent = 4, Received = 3, Lost = 1 (25% loss),
Approximate round trip times in milli-seconds:
    Minimum = 10ms, Maximum = 24ms, Average = 15ms

C:\>

      NAT and Port Forwarding

NAT (Network Address Translation) mechanism translates one address to another in a forwarding packet. For this case it can change port of the package.
Let's add WebServer with index.html file to Home Officce workspace, open all ports for HTTP protocol to this server in WiFi router, configure DNS Server, add it to  DHCP server in WiFi router and check result:

<img src="https://github.com/SDenisko/DevOps_online_Chernigiv_2021Q4/blob/7624c1eeeaacb8604f29a7fe26f4a0a423166f73/task3/images/4/forward.JPG" width="300">


<img src="https://github.com/SDenisko/DevOps_online_Chernigiv_2021Q4/blob/7624c1eeeaacb8604f29a7fe26f4a0a423166f73/task3/images/4/HomeServerWeb.JPG" width="300">



It works!!!

Thanks a lot for this practice!!


