My final project consists of two levels:
The first level is the Jenkins pipeline for building and testing the "HelloWorld" java project and notification of the build results to the telegram channel.
The second level is the Jenkins pipeline for building, testing, notifications to the telegram channel and storing artifacts in DockerHub.
The infrastructure for both tiers is built on VirtualBox and Vagrant for automation.

HelloWorld project:
Vagrant file: https://github.com/SDenisko/DevOps_online_Chernigiv_2021Q4/blob/main/Final%20Project/Hello%20World/vagrant/Vagrantfile

Jenkins file: https://github.com/SDenisko/DevOps_online_Chernigiv_2021Q4/blob/main/Final%20Project/Hello%20World/jenkins/Jenkinsfile

Bash script as axample of deliver process: https://github.com/SDenisko/DevOps_online_Chernigiv_2021Q4/blob/main/Final%20Project/Hello%20World/jenkins/scripts/deliver.sh


PetClinic project:

Vagrant file: https://github.com/SDenisko/DevOps_online_Chernigiv_2021Q4/blob/main/Final%20Project/PetClinic/vagrant/Vagrantfile

Jenkinsfile: https://github.com/SDenisko/DevOps_online_Chernigiv_2021Q4/blob/main/Final%20Project/PetClinic/jenkins/Jenkinsfile

Docker file for build docker image with artifact: https://github.com/SDenisko/DevOps_online_Chernigiv_2021Q4/blob/main/Final%20Project/PetClinic/Dockerfile
