I created AWS Free tier account before Epam courses, so this part of task 2.2 was without issues. 
AWS hand-on tutorial and AWS Well Architecte Labs makes home studie more effective, to my position.
Let's start with Amazon Lightsail. 
For this sign in to account, AWS Management Console and in drop down menu "All Services" choose  "Lightsail". At opened page choose Instances and press "Creare instance". There are some parameters:
1. Instance location (Frankfurt as  default in my case).
2. Platform (Linux/Windows). I choose Linux/Unix.
3. Blueprint. I choose OS Only and Ubuntu 20.04 TLS.
4. We can add a script that will start first time at our instance.

<img src="https://github.com/SDenisko/DevOps_online_Chernigiv_2021Q4/blob/b9bf0814558a2e3a73f812ee5bc0eea9ffefef73/task2.2/images/NFS_enabled_2.JPG" width="250">

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


<img src="https://github.com/SDenisko/DevOps_online_Chernigiv_2021Q4/blob/b9bf0814558a2e3a73f812ee5bc0eea9ffefef73/task2.2/images/NFS_enabled.JPG" width="250">


4. Add storage. I added nfs share and 30Gb root volume. 


<img src="https://github.com/SDenisko/DevOps_online_Chernigiv_2021Q4/blob/b9bf0814558a2e3a73f812ee5bc0eea9ffefef73/task2.2/images/add_storage.JPG" width="250">

<img src="https://github.com/SDenisko/DevOps_online_Chernigiv_2021Q4/blob/b9bf0814558a2e3a73f812ee5bc0eea9ffefef73/task2.2/images/HFS_enabled.JPG" width="250">




5. Add tags. I added RedHat Tag and value =1.
6.Configure Security Group. In this point i added only ssh rule.
7. Review of parameters. Create VM.
ssh connection sucsessful!
[ec2-user@ip-172-31-21-227 ~]$ pwd
/home/ec2-user

Adding second volume (Disk_D) to my first AWS instance.
For this case uses EBS (Elastic Block Store). Go to path EC2>Volumes>Create volume. On this page i can set key parameters (type, size, zone, encryption, TAG). 

If Instace and Storage have different zone they are don't avaliably to eachother. Next step should be "Attach volume" to instance and if i use linux system - create partition table, create file system and mount it.


<img src="https://github.com/SDenisko/DevOps_online_Chernigiv_2021Q4/blob/b9bf0814558a2e3a73f812ee5bc0eea9ffefef73/task2.2/images/create_second_storage.JPG" width="250">


I mounted new partition to /mnt/disk_d/ folder and create file_for_test.txt with "Hello World!" inside.


<img src="https://github.com/SDenisko/DevOps_online_Chernigiv_2021Q4/blob/b9bf0814558a2e3a73f812ee5bc0eea9ffefef73/task2.2/images/disk_D_second_instance.JPG" width="250">


Launch instance from backup.
For backup file was created snapshot of VM. So, first of all need create image from this snapshot.


<img src="https://github.com/SDenisko/DevOps_online_Chernigiv_2021Q4/blob/b9bf0814558a2e3a73f812ee5bc0eea9ffefef73/task2.2/images/snapshot_1.JPG" width="250"> 


For this go to EBS>snapshots. In this page need choose snapshot and in drop down menu  "Action" choose "Create image", enter name of image, 
check other parameters and press "Create" . Next step, go to  "Images>AMIs" and launch instanse from it. 
There are five steps, were we can change parameters for new instance.


<img src="https://github.com/SDenisko/DevOps_online_Chernigiv_2021Q4/blob/b9bf0814558a2e3a73f812ee5bc0eea9ffefef73/task2.2/images/instance_from_snapshot.JPG" width="250">


Before detach volume from first instance and attach it to second instance it should be umount and check zone location. 
Instance and volume shoulde be in the same zone. In enother way volume does not visible for instance. For correcting this issue should make snapshot of the volume, create new volume from it with new region and attach it to second instance. 
And this is was my case. 
Attach and Deatache volume steps we can made in volume settings on page EC2>Volumes.


Amazon Lightsail - this is easy and user friendly . 
So, let's go. As a task need launch and configure WordPress instance. For this go to the lightsail page and press "Create Instance". After, all steps looks like as in point 4, 
but with enother parameters (Platform - linux/unix, Blueprint: App+OS>WordPress, doesn't attach any script, use the same key pair for ssh). 
Press "Create instance" and all DONE. 
If we have WordPress instance, we should have lightsail static IP address and it should be attach to instance (screens are in images folder). 
We can do this in Network settings of WordPress instance. Second importent point for WordPress page is DNS zone. This case was intersting for me. DNS zone create menu is in Amazone LightSail page in Network tap. 
And i was looking for them inside WordPress instance page. It was confuce for me. 


<img src="https://github.com/SDenisko/DevOps_online_Chernigiv_2021Q4/blob/b9bf0814558a2e3a73f812ee5bc0eea9ffefef73/task2.2/images/add_static_ip.JPG" width="250">

<img src="https://github.com/SDenisko/DevOps_online_Chernigiv_2021Q4/blob/b9bf0814558a2e3a73f812ee5bc0eea9ffefef73/task2.2/images/attach_static_ip.JPG" width="250">

<img src="https://github.com/SDenisko/DevOps_online_Chernigiv_2021Q4/blob/b9bf0814558a2e3a73f812ee5bc0eea9ffefef73/task2.2/images/attached_static_ip.JPG" width="250">


I entered domain DevOpsQ4Chernigiv.com and attach it to static address in lightsail options (A record: aws
.DevOpsQ4Chernigiv.com - 3.69.145.172).This domain name is no free tier, so we can use only static ip address for acces to webpage. 

<img src="https://github.com/SDenisko/DevOps_online_Chernigiv_2021Q4/blob/b9bf0814558a2e3a73f812ee5bc0eea9ffefef73/task2.2/images/DNS_zone.JPG" width="250">

For notes: for buy domaine and attach it to static ip we can use Route 53 service (5-12 usd/year).    

<img src="https://github.com/SDenisko/DevOps_online_Chernigiv_2021Q4/blob/b9bf0814558a2e3a73f812ee5bc0eea9ffefef73/task2.2/images/WordPress_heloWorld.JPG" width="250">


If we have nesesary in storage and retrieve a files we should use S3 service. First step in this case should be create a bucket. For this go to the S3 page and press Create bucket. In new page need set name and zone for AWS bucket, set encryption, control of bucket version, TAGs, object locks (read/write). 
And press Create Bucket. 
The second key point is public access to object and bucket.

For upload files to bucket we can use S3 service web page. On this page should chose bucket and press upload. Next step chose folder or files and press upload. 
If we need download files from AWS bucket we should select file and press download buttom. 
The second key point is opened public access to object and bucket from URL. We can do it in Permitions.


Enother way work with S3 service is use AWS CLI.
Before use this we should configure it. First of all need IAM user with AdministratorAccess credetentional, AWS Access key ID, AWS Secter Access Key . We cane do this on IAM page. Next step this is configure AWS CLI on the host . In my case i use windows command line and "aws configur" command. For use aws CLI on host should go  to path were was install AWS CLI (c:\Program Files\Amazon\AWSCLI>). Commands which need use for this task:

<img src="https://github.com/SDenisko/DevOps_online_Chernigiv_2021Q4/blob/b9bf0814558a2e3a73f812ee5bc0eea9ffefef73/task2.2/images/AWS_CLI_config.JPG" width="250">

List of buckets:

c:\Program Files\Amazon\AWSCLI>aws s3 ls
2021-11-12 14:27:35 devopsq4

upload file to bucket: 

c:\Program Files\Amazon\AWSCLI>aws s3 cp "d:\VirtualBox VMs\DevOps2.pem" s3://devopsq4/
upload: d:\VirtualBox VMs\DevOps2.pem to s3://devopsq4/DevOps2.pem

Check result of uploading:

c:\Program Files\Amazon\AWSCLI>aws s3 ls s3://devopsq4/
                           PRE CLI/
                           PRE task2.2/
2021-11-13 20:46:33       1700 DevOps2.pem

Amazon has Elastic Container Service (Amazon ECS), so we can deploy Docker containers to cloud. There is a good case for testing and develop.
First of all should create instance and install Docker to it. 
AWS instance with linux was created in enother point of task2.2, we can use it. Connect to it with ssh, install Docker (sudo yum install docker), install and configure AWS CLI.  
We can create docker container, create image from it and push to AWS ECR. 
For create container let's use dockerfile, there are all nececcary parameters  (core image, dependencies, configurations for them).

Build image: 
ec2-user@ip-172-31-45-170 ~]$ sudo docker build -t hello-world .
Sending build context to Docker daemon  8.192kB
Step 1/6 : FROM ubuntu:18.04
18.04: Pulling from library/ubuntu
284055322776: Pull complete
Digest: sha256:0fedbd5bd9fb72089c7bbca476949e10593cebed9b1fb9edf5b79dbbacddd7d6
Status: Downloaded newer image for ubuntu:18.04
 ---> 5a214d77f5d7
Step 2/6 : RUN apt-get update &&  apt-get -y install apache2
 ---> Running in 6afb990601d6
.........................
Run docker image:

[ec2-user@ip-172-31-45-170 ~]$ sudo docker images --filter reference=hello-world
REPOSITORY    TAG       IMAGE ID       CREATED          SIZE
hello-world   latest    cfa2eb488db4   31 seconds ago   198MB

We use apache2 inside Ubuntu container, so, for check should be open and forward port 80 on host and container.
[ec2-user@ip-172-31-45-170 ~]$ sudo docker run -t -i -p 80:80 hello-world
AH00558: apache2: Could not reliably determine the server's fully qualified domain name, using 172.17.0.2. Set the 'ServerName' directive globally to suppress this message
 

Let's run this container on EC2 instance.
For this we need some steps:
1. Ceate ECR repository: 
aws ecr create-repository --repository-name hello-repo
The key options are name and region of repository.
2. Tag the image with the repository URL value:
docker tag hello-world 706516783771.dkr.ecr.us-east-2.amazonaws.com/hello-repo
3. Login to repository:
[ec2-user@ip-172-31-45-170 ~]$ aws ecr get-login-password | docker login --username AWS --password-stdin 706516783771.dkr.ecr.us-east-2.amazonaws.com
WARNING! Your password will be stored unencrypted in /home/ec2-user/.docker/config.json.
Configure a credential helper to remove this warning. See
https://docs.docker.com/engine/reference/commandline/login/#credentials-store

Login Succeeded
4. Push container to ECR repository:
[ec2-user@ip-172-31-45-170 ~]$ docker push 706516783771.dkr.ecr.us-east-2.amazonaws.com/hello-repo
Using default tag: latest
The push refers to repository [706516783771.dkr.ecr.us-east-2.amazonaws.com/hello-repo]
53384c5fc94e: Layer already exists
ff4f9e5c28e1: Layer already exists
41472bce8adc: Layer already exists
824bf068fd3d: Layer already exists
latest: digest: sha256:d02219b8d6332d3c9537191512cdfae1e51190425a9d3dc23a3ec599fd4b9377 size: 1155

5. Next key step are create ECS Cluster.
 For this press Create Cluster>chose "EC2 Linux + Networking" type. There are a lot of key parameters: Name of cluster, Provisioning Model, Type of instance, Number of instances, Networking (VPC, Subnets, Security group inbound rules). At the End press Create.


<img src="https://github.com/SDenisko/DevOps_online_Chernigiv_2021Q4/blob/b9bf0814558a2e3a73f812ee5bc0eea9ffefef73/task2.2/images/ECS_Cluster.JPG" width="250">

After this we gete Cluster and ECS-instance on the EC2 page. All containers start on this instance. 


<img src="https://github.com/SDenisko/DevOps_online_Chernigiv_2021Q4/blob/b9bf0814558a2e3a73f812ee5bc0eea9ffefef73/task2.2/images/ECS_instance.JPG" width="250">

6. For start the docker-container uses "Task Definitions" menu on ECS page. Press New Task Definition, chose EC2 type, set name for task, network mode, task size, add container name and link from ECR repository and press Create.
<img src="https://github.com/SDenisko/DevOps_online_Chernigiv_2021Q4/blob/b9bf0814558a2e3a73f812ee5bc0eea9ffefef73/task2.2/images/ECR_image2.JPG" width="250">

<img src="https://github.com/SDenisko/DevOps_online_Chernigiv_2021Q4/blob/b9bf0814558a2e3a73f812ee5bc0eea9ffefef73/task2.2/images/task_definition.JPG" width="250">

7. Task Done, but need run it in claster. For this go to the Task tabe inside Cluster, chose lounch types> EC2, task name, cluster, press Run Task. If all ports forwarded - ALL DONE.

<img src="https://github.com/SDenisko/DevOps_online_Chernigiv_2021Q4/blob/b9bf0814558a2e3a73f812ee5bc0eea9ffefef73/task2.2/images/opened_port.JPG" width="250">

<img src="https://github.com/SDenisko/DevOps_online_Chernigiv_2021Q4/blob/b9bf0814558a2e3a73f812ee5bc0eea9ffefef73/task2.2/images/check_container.JPG" width="250">

Point 14 of the task2.2 was hard for me, i could not understand sequence of actions and interconnection between them. 

S3 service has a perfect option, it can contain static Website. 
Let's do this.
First of all need create bucket, name of it should be the same domaine name of site. Only for comfort. 
Next step  - enable static website hosting for your bucket, and enter the exact name of our index.html. Upload index.html file to bucket.

<img src="https://github.com/SDenisko/DevOps_online_Chernigiv_2021Q4/blob/b9bf0814558a2e3a73f812ee5bc0eea9ffefef73/task2.2/images/enable_website_bucket.JPG" width="250">

<img src="https://github.com/SDenisko/DevOps_online_Chernigiv_2021Q4/blob/b9bf0814558a2e3a73f812ee5bc0eea9ffefef73/task2.2/images/uploaded_index.JPG" width="250">

Next key step this is - Public Access Settings and Bucket Policy. For this go to the bucket settings, choose Permissions. Under Block public access, choose Edit. Clear Block all public access, and choose Save changes. Nexst step "Attach a bucket policy". 

<img src="https://github.com/SDenisko/DevOps_online_Chernigiv_2021Q4/blob/b9bf0814558a2e3a73f812ee5bc0eea9ffefef73/task2.2/images/public_access.JPG" width="250">

<img src="https://github.com/SDenisko/DevOps_online_Chernigiv_2021Q4/blob/b9bf0814558a2e3a73f812ee5bc0eea9ffefef73/task2.2/images/bucket_policy.JPG" width="250">

<img src="https://github.com/SDenisko/DevOps_online_Chernigiv_2021Q4/blob/b9bf0814558a2e3a73f812ee5bc0eea9ffefef73/task2.2/images/public_result.JPG" width="250">

All DONE. Let's check link:
http://jurnalq4web.s3-website.us-east-2.amazonaws.com/
