I created AWS Free tier account before Epam courses, so this part of task 2.2 was without issues. 
AWS hand-on tutorial and AWS Well Architecte Labs makes home studie more effective, to my position.
Let's start with Amazon Lightsail. 
For this sign in to account, AWS Management Console and in drop down menu "All Services" choose  "Lightsail". At opened page choose Instances and press "Creare instance". There are some parameters:
1. Instance location (Frankfurt as  default in my case).
2. Platform (Linux/Windows). I choose Linux/Unix.
3. Blueprint. I choose OS Only and Ubuntu 20.04 TLS.
4. We can add a script that will start first time at our instance.
5. I desided  create new ssh key. Very importent: don't forget download and import it to your host.
6. Choose instance plan 3.5 USD/month. This is free plan for three first months.
7. Enter the name for our instance. I desided enter "DevOpsOnline" name.
8. I desided add Key-only tag "first". Without value it can be used for filter and organize resources.
9. Press "Create Instance". 
After this AMAZON took 1 USD from me. I forgot check my credit card before start task. This is tereable, because this is free tier account. But, it is importent expirience!
IP address of my new instance: 18.157.165.210. Let's try ssh connection with ssh key.

Launch VM without AWS Lightsail
For this task we should choose EC2 service at the AWS Management Console. After this we have 7 steps with different parameters of VM:
1. There are list of AMI (Amazon Machine Images). I choose RedHet Linux in the Free tier eligible case. 
2. On this position i should chose type of VM. List of free tier types has t3.micro and t4g. T3 type use CPU Intel Xenon Platinum, T4g - ARM CPU. I desided chose T3 type. But, as i know ARM CPU x64 has a very good performens too. 
3. On this step i have a lot of detail parameters of VM. There are number of instances, purchaising option with maximum price you are willing to pay per instance hour,  network parameters, placement groups, domain directory which centralized management experience across a network, credit specification, file system (for mount NFS file system, I desided use it), advanced details for computer environment and more.
4. Add storage. I added nfs share and 30Gb root volume. 
5. Add tags. I added RedHat Tag and value =1.
6.Configure Security Group. In this point i added only ssh rule.
7. Review of parameters. Create VM.
ssh connection sucsessful!
[ec2-user@ip-172-31-21-227 ~]$ pwd
/home/ec2-user

Adding second volume (Disk_D) to my first AWS instance.
For this case uses EBS (Elastic Block Store). Go to path EC2>Volumes>Create volume. On this page i can set key parameters (type, size, zone, encryption, TAG). If Instace and Storage have different zone they are don't avaliably to eachother. Next step should be "Attach volume" to instance and if i use linux system - create partition table, create file system and mount it.
I mounted new partition to /mnt/disk_d/ folder and create file_for_test.txt with "Hello World!" inside.

Launch instance from backup.
For backup file was created snapshot of VM. So, first of all need create image from this snapshot. 
For this go to EBS>snapshots. In this page need choose snapshot and in drop down menu  "Action" choose "Create image", enter name of image, 
check other parameters and press "Create" . Next step, go to  "Images>AMIs" and launch instanse from it. 
There are five steps, were we can change parameters for new instance.
 Before detach volume from first instance and attach it to second instance it should be umount and check zone location. 
Instance and volume shoulde be in the same zone. In enother case should make snapshot of the volume, create new volume from it and attach it to second instance. 
And this is my case. Some images are in image folder.


Amazon Lightsail - this is easy and user friendly . 
So, let's go. As a task need launch and configure WordPress instance. For this go to the lightsail page and press "Create Instance". After, all steps looks like as in point 4, but with enother parameters (Platform - linux/unix, Blueprint: App+OS>WordPress, doesn't attach any script, use the same key pair for ssh). Press "Create instance" and all DONE. If we have WordPress instance, we should have lightsail static IP address and it should be attach to instance (screens are in images folder). We can do this in Network settings of WordPress instance. Second importent point for WordPress page is DNS zone. This case was intersting for me. DNS zone create menu is in Amazone LightSail page in Network tap. And i was looking for them inside WordPress instance page. It was confuce for me. I create domain DevOpsQ4Chernigiv.com and attach it to static address (A record: aws
.DevOpsQ4Chernigiv.com - 3.69.145.172). 

If we have nesesary store and retrieve a files we should use S3 service. First step in this case should be create a bucket. For this go to the S3 page and press Create bucket. In new page need set name and zone for AWS bucket, set encryption, control of bucket version, TAGs, object locks (read/write). And press Create Bucket. The second key point is public access to object and bucket.
