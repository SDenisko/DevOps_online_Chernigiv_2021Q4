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



