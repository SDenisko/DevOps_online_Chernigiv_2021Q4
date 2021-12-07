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


11. Some times for get long information about directory uses the "ls" command with "-l" and "-d" keys. Let's describe of the command result:

The first character shows the type file: d - directory;

The next nine characters are showing the file permitions:
( r - permition to read the file; w - permition to write the file; x - permition to execute the file; t - stiky bit; s - setgit and setuid bits;)
 - The following set of three characters (rwx) is for the owner permissions.
 - The second set of three characters (rwx) is for the Group permissions.
 - The third set of three characters (rwx) is for the All Users permissions.

The next two fields root root are showing the file owner and the group, followed by the size of the file (4096), shown in bytes. Use the -h option if you want to print sizes in a human-readable format. 
You can change the file owner using the chown command.

The last column is the name of the file/directory.

	root@devopsonline:/home/mrbit# ls -l DevOps_online_Chernigiv_2021Q4/

	total 40

	-rw-r--r-- 1 root root 11357 Nov  2 21:38 LICENSE

	drwxr-xr-x 6 root root  4096 Nov  8 18:06 task1.1

	drwxr-xr-x 3 root root  4096 Nov  8 18:08 task2.1

	drwxr-xr-x 3 root root  4096 Nov 16 14:58 task2.2

	drwxr-xr-x 3 root root  4096 Nov 19 18:25 task3

	drwxr-xr-x 3 root root  4096 Nov 28 19:55 task4.1

	drwxr-xr-x 3 root root  4096 Dec  3 09:47 task5.1

	drwxr-xr-x 3 root root  4096 Dec  6 08:54 task5.2

	root@devopsonline:/home/mrbit# ls -ld /tmp/

	drwxrwxrwt 13 root root 4096 Dec  6 09:49 /tmp/

12. Any file in linux has owner, this owner has the marks ID (UID - user id). For list of the uid of the file/folder  uses "ls" command with "-l" "-n" keyes.

	root@devopsonline:/home/mrbit# ls -lnd /home/mrbit/

	drwxr-xr-x 7 1000 1000 4096 Dec  6 09:34 /home/mrbit/

"1000" and "1000" - thare are UID and GID.

13. To change the owner of the file/directory uses "chown" command.
Some keyes for "chown" command from man:

	-c    like verbose but report only when a change is made

	-f     suppress most error messages

	-v      output a diagnostic for every file processed

	--dereference      affect the referent of each symbolic link (this is the default), rather than the symbolic link itself

	-R     operate on files and directories recursively

	-H     if a command line argument is a symbolic link to a directory, traverse it


 For example let's change owner of file from root user to test user:

	root@devopsonline:/home/mrbit# touch /home/testfile

	root@devopsonline:/home/mrbit# ls -l /home/testfile

	-rw-r--r-- 1 root root 0 Dec  6 12:12 /home/testfile

	root@devopsonline:/home/mrbit# id test

	uid=1001(test) gid=1001(test) groups=1001(test)

	root@devopsonline:/home/mrbit# chown 1001 /home/testfile

	root@devopsonline:/home/mrbit# ls -l /home/testfile

	-rw-r--r-- 1 test root 0 Dec  6 12:12 /home/testfile

To change the mode of the file uses "chmod" command. Keyes: 
 - u (owner) file's owner;
 - g (group) users who are members of the file's group;
 - o (others) users who are neither the file's owner nor members of the file's group;
 - a (all) All three of the above, same as ugo;
 - "+" adds the specified modes
 - "-" removes the specified modes
 - "=" the modes specified are to be made the exact modes for the specified classes

For example let's change mode of the testfile:

	root@devopsonline:~# ls -l /home/testfile

	-rw-r--r-- 1 test root 28 Dec  6 12:18 /home/testfile

	root@devopsonline:~# chmod u=rwx /home/testfile
	root@devopsonline:~# ls -l /home/testfile

	-rwxr--r-- 1 test root 28 Dec  6 12:18 /home/testfile

	root@devopsonline:~# chmod g=rw /home/testfile
	root@devopsonline:~# ls -l /home/testfile

	-rwxrw-r-- 1 test root 28 Dec  6 12:18 /home/testfile

	root@devopsonline:~# chmod o+rw /home/testfile
	root@devopsonline:~# chmod g+x /home/testfile
	root@devopsonline:~# chmod u-x /home/testfile
	root@devopsonline:~# ls -l /home/testfile

	-rw-rwxrw- 1 test root 28 Dec  6 12:18 /home/testfile

	root@devopsonline:~# chmod a-rw /home/testfile
	root@devopsonline:~# ls -l /home/testfile

	------x--- 1 test root 28 Dec  6 12:18 /home/testfile

	root@devopsonline:~# chmod o-x /home/testfile
	root@devopsonline:~# ls -l /home/testfile

	------x--- 1 test root 28 Dec  6 12:18 /home/testfile

	root@devopsonline:~# chmod g-x /home/testfile
	root@devopsonline:~# ls -l /home/testfile

	---------- 1 test root 28 Dec  6 12:18 /home/testfile

	root@devopsonline:~# chmod gou+rw /home/testfile
	root@devopsonline:~# chmod u+x /home/testfile
	root@devopsonline:~# chmod o-w /home/testfile
	root@devopsonline:~# ls -l /home/testfile

	-rwxrw-r-- 1 test root 28 Dec  6 12:18 /home/testfile

Numeric way:
r  ​(read) = 4
w (write) = 2
x (execute) = 1
without permitions = 0

read+write+execute=4+2+1=7
read+write=4+2=6

Example:

	root@devopsonline:~# chmod 644 /home/testfile
	root@devopsonline:~# ls -l /home/testfile

	-rw-r--r-- 1 test root 28 Dec  6 12:18 /home/testfile

14. When user create file or folder system define to it some permissions. "umask" - there are user mask which define this permissions. Umask for all users sets in etc/.bashrc or /etc/.profile.  As default it is "0022".

15. The sticky bit is usually used for a folder especially to protect files in it. If it is set for a folder, then only the owner of the file can delete a file in the folder. The chmod command is used to set the sticky bit.
An example of a folder with a sticky bit /tmp.

	root@devopsonline:/home/mrbit/DevOps_online_Chernigiv_2021Q4# ls -l / | grep tmp

	drwxrwxrwt  13 root root  4096 Dec  7 09:08 tmp

	root@devopsonline:/home/mrbit/DevOps_online_Chernigiv_2021Q4# chmod +t /home/testfolder
	root@devopsonline:/home/mrbit/DevOps_online_Chernigiv_2021Q4# ls -l /home/

	total 16

	drwxr-xr-x 7 mrbit mrbit 4096 Dec  7 08:43 mrbit

	drwxr-xr-x 3 test  test  4096 Dec  6 12:18 test

	-rw-r--r-T 1 test  root    28 Dec  6 12:18 testfile

	drwxr-xr-t 2 root  root  4096 Dec  7 09:28 testfolder
  
16. First of all, you need to select a shell in the script file. The most commonly used shell is bash. In this case, the first line should be:
#! / bin / bash
After that there should be a program text.
The file must be executable to use this script. To do this, use the command chmod u + x. 
For check attributes of the file is used "lsattr" command. 
Example:

	root@devopsonline:/home/mrbit/DevOps_online_Chernigiv_2021Q4# lsattr /home/testfile

	--------------e----- /home/testfile

Any file can has a lot of attributes:

	a — Append only. No one can overwrite, delete, rename, or hard link the file. Must be root to change.
	A — Do not record atime for this file.
	c — Compress file, if supported.
	C — Suppress copy on write, if supported.
	d — Do not backup using thedump utility (and possibly others).
	D — Write directory changes synchronously to disk.
	e — Do not fragment file; allocate extents contiguously
	i — Immutable; do not allow any changes. Must be root or have special permissions to change.
	j — Control journaling for ext file systems.
	P — Enforce project hierarchy; files inherit directory project numbers and can’t move into directories that do not match.
	s — Securely delete the file when deleting, if supported.
	S — Write changes directly to disk (synchronous).
	t — Prevents tail merging on filesystems that do tail merging.
	T — Controls block allocation for some filesystems by identifying the directory as a top-level container. For example, /home is a top level container where subdirectories are not really related and are unlikely to have steady access patterns between them.
	u — Save file on deletion for possible undeletion with appropriate tools.
	E — Error when trying to compress.
	h — File stored as huge file (indicates the file has been larger than 2TB at some point).
	I — File uses hashed tree index.
	N — File is stored inside inode.

for change attribute of the file uses "chattr" command.
