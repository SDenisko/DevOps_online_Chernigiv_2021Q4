1. /etc/passwd and etc/group files.

/etc/passwd file containe information about all users in system and can containe encrypted passwords.

<img src="https://github.com/SDenisko/DevOps_online_Chernigiv_2021Q4/blob/e52d3f8c32f9c120ac1e2b2c49b744b418bc82a3/task5.2/images/passwd.JPG" width="300">

<img src="https://github.com/SDenisko/DevOps_online_Chernigiv_2021Q4/blob/e52d3f8c32f9c120ac1e2b2c49b744b418bc82a3/task5.2/images/passwd_list.JPG" width="300">

/etc/group file contains information about groups to which users container.

<img src="https://github.com/SDenisko/DevOps_online_Chernigiv_2021Q4/blob/e52d3f8c32f9c120ac1e2b2c49b744b418bc82a3/task5.2/images/group_inf.jpg" width="300">

<img src="https://github.com/SDenisko/DevOps_online_Chernigiv_2021Q4/blob/e52d3f8c32f9c120ac1e2b2c49b744b418bc82a3/task5.2/images/group_list.JPG" width="300">

Both files containe pseudousers and groups for them. If program not need root privilages, it should work from enother user, for this uses pseudousers. 

<img src="https://github.com/SDenisko/DevOps_online_Chernigiv_2021Q4/blob/e52d3f8c32f9c120ac1e2b2c49b744b418bc82a3/task5.2/images/pseudousers.JPG" width="300">

2. UID is the user's identifier. In Linux, every user has an ID. This can be verified with the "id" command or in the / etc / passwd file. UID and user rights are interconnected. All files owned by a user have the UID of that user. 
The UID can be from 0 to 65535. But UID = 0 is defined by the root user. UIDs from 1 to 100 (sometimes 101 to 499 or 101 to 999) are reserved for the system. For the "nobody" user uses the maximum UID or one of the system range.

<img src="https://github.com/SDenisko/DevOps_online_Chernigiv_2021Q4/blob/e52d3f8c32f9c120ac1e2b2c49b744b418bc82a3/task5.2/images/uid.JPG" width="300">

3. GID is the group identifier. It can be verified  with the "id" command, in /etc/passwd or /etc/group file. Please, look on the image before.

4. To determine belonging of user to the specific group uses "groups" command:

<img src="" width="300">
 
5. For adding user to linux system uses "adduser" commnd. After enter it you should insert password for user (this is very importent point), full name, room number, work phone, home phone, some other information. After this will be created user and his home directory.   

<img src="" width="300">

6. We can rename user. Thare are uses "usermod -l <old name> <new name>" command. But, home directory stay with old name and should be renamed manualy.

	root@devopsonline:/home/mrbit/DevOps_online_Chernigiv_2021Q4# usermod -l  newtest test
	root@devopsonline:/home/mrbit/DevOps_online_Chernigiv_2021Q4# mv /home/test/ /home/newtest
	root@devopsonline:/home/mrbit/DevOps_online_Chernigiv_2021Q4# ls /home/
	mrbit  newtest
	newtest@devopsonline:/home/mrbit/DevOps_online_Chernigiv_2021Q4$ id newtest
	uid=1001(newtest) gid=1001(test) groups=1001(test)
	root@devopsonline:/home/mrbit/DevOps_online_Chernigiv_2021Q4# ls /home/
	mrbit  test
	root@devopsonline:/home/mrbit/DevOps_online_Chernigiv_2021Q4# su - newtest
	newtest@devopsonline:~$

