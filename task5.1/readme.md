1. For connect to Linux host i use ssh, so connect with root user is denyded. 

mrbit@devopsonline:~$ sudo -s

[sudo] password for mrbit:

2. root@devopsonline:/home/mrbit# passwd root

New password:

Retype new password:

passwd: password updated successfully

"passwd" command chages password of user. /etc/passwd file containe encrypted information about users, privilages and passwords.

/etc/group containe list of user groups.



root:x:0:0:root:/root:/bin/bash

daemon:x:1:1:daemon:/usr/sbin:/usr/sbin/nologin

bin:x:2:2:bin:/bin:/usr/sbin/nologin

sys:x:3:3:sys:/dev:/usr/sbin/nologin

sync:x:4:65534:sync:/bin:/bin/sync

games:x:5:60:games:/usr/games:/usr/sbin/nologin

man:x:6:12:man:/var/cache/man:/usr/sbin/nologin

lp:x:7:7:lp:/var/spool/lpd:/usr/sbin/nologin

mail:x:8:8:mail:/var/mail:/usr/sbin/nologin

.....

lxd:x:998:100::/var/snap/lxd/common/lxd:/bin/false

mysql:x:113:117:MySQL Server,,,:/nonexistent:/bin/false



<img src="https://github.com/SDenisko/DevOps_online_Chernigiv_2021Q4/blob/5e6c325e30c3360e1ee70377470675bf8b14bf75/task5.1/images/list-users.png" width="300">


root@devopsonline:/home/mrbit/DevOps_online_Chernigiv_2021Q4# cat /etc/group

root:x:0:

daemon:x:1:

bin:x:2:

sys:x:3:

adm:x:4:syslog,mrbit

tty:x:5:syslog

disk:x:6:

.....

www-data:x:33:

backup:x:34:

staff:x:50:

games:x:60:

users:x:100:

nogroup:x:65534:

crontab:x:105:

kvm:x:108:

render:x:109:

syslog:x:110:

tss:x:111:

uuidd:x:112:

tcpdump:x:113:

ssh:x:114:

landscape:x:115:

lxd:x:116:mrbit

systemd-coredump:x:999:

mrbit:x:1000:

mysql:x:117:


<img src="https://github.com/SDenisko/DevOps_online_Chernigiv_2021Q4/blob/5e6c325e30c3360e1ee70377470675bf8b14bf75/task5.1/images/list-groups.jpg" width="300">



Where,
1 - group_name: It is the name of group. If you run ls -l command, you will see this name printed in the group field.

2 - Password: Generally password is not used, hence it is empty/blank. It can store encrypted password. This is useful to implement privileged groups.

3 - Group ID (GID): Each user must be assigned a group ID. You can see this number in your /etc/passwd file.

4 - Group List: It is a list of user names of users who are members of the group. The user names, must be separated by commas.


3. Let's change personal information for mrbit user:


root@devopsonline:/home/mrbit/DevOps_online_Chernigiv_2021Q4# chfn mrbit


Changing the user information for mrbit

Enter the new value, or press ENTER for the default

        Full Name [mrbit]: mister

        Room Number []: 1

        Work Phone []: 1234567

        Home Phone []: 7654321

        Other []: I live in Chernigiv


root@devopsonline:/home/mrbit/DevOps_online_Chernigiv_2021Q4# finger mrbit



Login: mrbit                            Name: mister

Directory: /home/mrbit                  Shell: /bin/bash

Office: 1, 123-4567                     Home Phone: 765-4321

On since Mon Nov 29 09:15 (UTC) on pts/0 from 10.0.2.2

   1 second idle

On since Mon Nov 29 09:17 (UTC) on pts/1 from 10.0.2.2

   6 minutes 57 seconds idle

No mail.

No Plan.


4. For get more information about any command can use "man" command. 


Example of "man" command for "ls":
--
man ls
 
NAME
       ls - list directory contents


       Mandatory arguments to long options are mandatory for short options too.

       -a, --all
              do not ignore entries starting with .

       -A, --almost-all
              do not list implied . and ..

       --author
              with -l, print the author of each file

       -b, --escape
              print C-style escapes for nongraphic characters

       --block-size=SIZE
              with -l, scale sizes by SIZE when printing them; e.g., '--block-size=M'; see SIZE format below

       -B, --ignore-backups
              do not list implied entries ending with ~

       -c     with  -lt:  sort  by, and show, ctime (time of last modification of file status information); with -l: show ctime and sort by name; otherwise:
              sort by ctime, newest first

       -C     list entries by columns

       -g     like -l, but do not list owner

       --group-directories-first
              group directories before files;

              can be augmented with a --sort option, but any use of --sort=none (-U) disables grouping

       -G, --no-group
              in a long listing, don't print group names

       -h, --human-readable
              with -l and -s, print sizes like 1K 234M 2G etc.

       --si   likewise, but use powers of 1000 not 1024

       -H, --dereference-command-line
              follow symbolic links listed on the command line

       --dereference-command-line-symlink-to-dir
              follow each command line symbolic link

              that points to a directory

       --hide=PATTERN
              do not list implied entries matching shell PATTERN (overridden by -a or -A)

       --hyperlink[=WHEN]
              hyperlink file names; WHEN can be 'always' (default if omitted), 'auto', or 'never'

       --indicator-style=WORD
              append indicator with style WORD to entry names: none (default), slash (-p), file-type (--file-type), classify (-F)

       -i, --inode

--
5. Command "less" uses for read a big text files: 

For example:



<img src="https://github.com/SDenisko/DevOps_online_Chernigiv_2021Q4/blob/ec058d7d19c4c114172b228ea8c84b92df847d03/task5.1/images/less.JPG" width="300">



 Command "more" - file perusal filter for crt viewing. 


<img src = "https://github.com/SDenisko/DevOps_online_Chernigiv_2021Q4/blob/ec058d7d19c4c114172b228ea8c84b92df847d03/task5.1/images/man_more.JPG" width="300">


For example:


<img src="https://github.com/SDenisko/DevOps_online_Chernigiv_2021Q4/blob/ec058d7d19c4c114172b228ea8c84b92df847d03/task5.1/images/more.JPG" width="300">


6. For read information about "finger" command i used man command



Very usefull "ls" command - list directory contents. 
Example of use it for home directory:
 
<img src="https://github.com/SDenisko/DevOps_online_Chernigiv_2021Q4/blob/ec058d7d19c4c114172b228ea8c84b92df847d03/task5.1/images/ls-ahl.JPG" width ="300">

Command "ls" helps me list of content of any folders. There are a lot of keyes, for example some of them:  -a, --all - do not ignore entries starting with; -h, --human-readable - with -l and -s, print sizes like 1K 234M 2G etc; -i, --inode - print the index number of each file; -l - use a long listing format. This is very usefull command.


#####################Part 2#######################

In this task i should use some commands:

1. "tree"

<img src="https://github.com/SDenisko/DevOps_online_Chernigiv_2021Q4/blob/ec058d7d19c4c114172b228ea8c84b92df847d03/task5.1/images/tree.JPG" width ="300">

<img src="https://github.com/SDenisko/DevOps_online_Chernigiv_2021Q4/blob/6fc2c21049ab8bc5eddbc825339773abe96d4c0c/task5.1/images/tree_root.JPG" width ="300">


2. Command "file" — determine file type.

<img src="https://github.com/SDenisko/DevOps_online_Chernigiv_2021Q4/blob/d94af0baa2caa0ad587e4081c716dabb8c89dd28/task5.1/images/file.JPG" width = "400"> 
