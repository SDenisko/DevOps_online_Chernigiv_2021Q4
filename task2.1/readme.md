######Part 1######
A hypervisor is a process that separate OS and programs from HW part of PC. 
The most famous HVs are ESXi, VirtualBox, Hyper-v, ProxMox.  
There are several types of hypervisors. The main of it are Type1 "Native hypervisors" and Type 2 "Guest hypervisors". 
Native hypervisor workes on a HW part of PC (example: ESXi, ProxMox). 
Guest hypervisor workes on a native OS of host (example: VirtualBox, Hyper-v).
######Part 2######
WORK WITH VIRTUALBOX  
When I was doing task I had work experience with CLI virtualbox. 
This is the most interesting case for me. I worked with VirtualBox GUI before - this is very user friendly. 
But CLI is faster. I made some screens for report and put them to an images folder. 
VirtualBox VM Groups are a good solution if you have a lot of the same tasks for several VMs (for example, reboot after update instalation).
If we open settings of any VM we can see a lot of interesting points, some of them: 
1. In "usb" point we can forward phisical usb port (usb token, usb key, usb storage) to VM.   
2. "Network" point has a drop down menu with network modes (the most interesting of them are NAT, NAT Network, Bridge, Internal Network, Host-Only). 
There is a table with posible connection in image folder. 
I tried NAT (VM1 doesn't ping VM2 but VMs ping other resourses), Brigre (all VMs ping all resourses), Internal Network (VM1 and VM2 are in the same subnetwork and can ping each other) modes.  
3. "Shared Folder" gives posibility to share files between  Host and VM, VM and VM. This case is very usefull. 
######Part 3######
WORK WITH VAGRANT 
Vagrant is a tool for building and managing virtual machine environments in a single workflow.  
I worked with Vagrant in PowerShell. I created the folder D:\VirtualBox VMs\SDenisko\vagrant_test and all operations did there.  
Key screen images are in the task2.1\images\vagrant folder. 
I underline next important notes: 
1. After creating work folder you should Initialize the environment with the default Vagrant box. In task they recomended to use hashicorp/precise64 image. 
2. As I saw, after "Vagrant destroy" command downloaded image hashicorp/precise64 does not delete. This is not bad. 
3. I worked with Vagrantfile. This is very intersting expirience. It's looks like Ansible for me. I used ansible for configuring VMs. In Vagrantfile,there are posibilities to create VMs and configure them and it works correctly. This is very interesting expirience  for me. Because,  as I know, in Ansible module for ProxMox this posibilities (create VM) are not good.  
4. My Vagrantfile is in the task2.1/images/vagrant folder.
