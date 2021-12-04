1. /etc/passwd and etc/group files.

/etc/passwd file containe information about all users in system and can containe encrypted passwords.

<img src="https://github.com/SDenisko/DevOps_online_Chernigiv_2021Q4/blob/e52d3f8c32f9c120ac1e2b2c49b744b418bc82a3/task5.2/images/passwd.JPG" width="300">

<img src="https://github.com/SDenisko/DevOps_online_Chernigiv_2021Q4/blob/e52d3f8c32f9c120ac1e2b2c49b744b418bc82a3/task5.2/images/passwd_list.JPG" width="300">
33333
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

<img src="https://github.com/SDenisko/DevOps_online_Chernigiv_2021Q4/blob/7d998687cf2cc03d53cecc007c542163ac1b7a89/task5.2/images/boloning%20to%20group.JPG" width="300">
 
5. For adding user to linux system uses "adduser" commnd. After enter it you should insert password for user (this is very importent point), full name, room number, work phone, home phone, some other information. After this will be created user and his home directory.   

<img src="https://github.com/SDenisko/DevOps_online_Chernigiv_2021Q4/blob/7d998687cf2cc03d53cecc007c542163ac1b7a89/task5.2/images/adduser.JPG" width="300">

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

7. Folder /etc/skel  (skeleton) uses for first start home directory when user creating.  
"Skeleton" folder defines in /etc/default/useradd. There are we can change location of "skeleton" folder.

	root@devopsonline:/home/mrbit# ls -alh /etc/skel/

	total 20K

	drwxr-xr-x   2 root root 4.0K Aug 24 08:45 .

	drwxr-xr-x 111 root root 4.0K Dec  4 17:49 ..

	-rw-r--r--   1 root root  220 Feb 25  2020 .bash_logout

	-rw-r--r--   1 root root 3.7K Feb 25  2020 .bashrc

	-rw-r--r--   1 root root  807 Feb 25  2020 .profile

<img src="https://github.com/SDenisko/DevOps_online_Chernigiv_2021Q4/blob/d6359fb81b36428dc6081084168b92519b407d43/task5.2/images/skel_def.JPG" width="300">

8. For delete user from the system uses "userdel" command with "-r" key. 

	root@devopsonline:/home/mrbit# ls /home/

        mrbit  newtest

	root@devopsonline:/home/mrbit# userdel newtest -r

	userdel: newtest mail spool (/var/mail/newtest) not found

	root@devopsonline:/home/mrbit# ls /home/

	mrbit

9. For lock/unlock of the user account in system uses "usermod" command with "-L" or "-U" keyes.

	root@devopsonline:/home/mrbit# usermod -L test
	root@devopsonline:/home/mrbit# su - mrbit
	mrbit@devopsonline:~$ su - test

	Password:

	su: Authentication failure

	mrbit@devopsonline:~$ sudo usermod -U test

	[sudo] password for mrbit:

	mrbit@devopsonline:~$ su - test

	Password:

	test@devopsonline:~$

10. For use username without password should do empty password for them before. there are uses "passwd" command with "-d" key 
From "man":
-d  Delete a user's password (make it empty). This is a quick way to disable a password for an account. It will set the named account passwordless.


	mrbit@devopsonline:~$ sudo passwd -d test

	passwd: password expiry information changed.

	mrbit@devopsonline:~$ su - test

	test@devopsonline:~$

11. 