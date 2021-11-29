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
news:x:9:9:news:/var/spool/news:/usr/sbin/nologin
uucp:x:10:10:uucp:/var/spool/uucp:/usr/sbin/nologin
proxy:x:13:13:proxy:/bin:/usr/sbin/nologin
www-data:x:33:33:www-data:/var/www:/usr/sbin/nologin
backup:x:34:34:backup:/var/backups:/usr/sbin/nologin
list:x:38:38:Mailing List Manager:/var/list:/usr/sbin/nologin
irc:x:39:39:ircd:/var/run/ircd:/usr/sbin/nologin
gnats:x:41:41:Gnats Bug-Reporting System (admin):/var/lib/gnats:/usr/sbin/nologin
nobody:x:65534:65534:nobody:/nonexistent:/usr/sbin/nologin
systemd-network:x:100:102:systemd Network Management,,,:/run/systemd:/usr/sbin/nologin
systemd-resolve:x:101:103:systemd Resolver,,,:/run/systemd:/usr/sbin/nologin
systemd-timesync:x:102:104:systemd Time Synchronization,,,:/run/systemd:/usr/sbin/nologin
messagebus:x:103:106::/nonexistent:/usr/sbin/nologin
syslog:x:104:110::/home/syslog:/usr/sbin/nologin
_apt:x:105:65534::/nonexistent:/usr/sbin/nologin
tss:x:106:111:TPM software stack,,,:/var/lib/tpm:/bin/false
uuidd:x:107:112::/run/uuidd:/usr/sbin/nologin
tcpdump:x:108:113::/nonexistent:/usr/sbin/nologin
landscape:x:109:115::/var/lib/landscape:/usr/sbin/nologin
pollinate:x:110:1::/var/cache/pollinate:/bin/false
usbmux:x:111:46:usbmux daemon,,,:/var/lib/usbmux:/usr/sbin/nologin
sshd:x:112:65534::/run/sshd:/usr/sbin/nologin
systemd-coredump:x:999:999:systemd Core Dumper:/:/usr/sbin/nologin
mrbit:x:1000:1000:mrbit:/home/mrbit:/bin/bash
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
lp:x:7:
mail:x:8:
news:x:9:
uucp:x:10:
man:x:12:
proxy:x:13:
kmem:x:15:
dialout:x:20:
fax:x:21:
voice:x:22:
cdrom:x:24:mrbit
floppy:x:25:
tape:x:26:
sudo:x:27:mrbit
audio:x:29:
dip:x:30:mrbit

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

man ls
 
NAME
       ls - list directory contents

SYNOPSIS
       ls [OPTION]... [FILE]...

DESCRIPTION
       List information about the FILEs (the current directory by default).  Sort entries alphabetically if none of -cftuvSUX nor --sort is specified.

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


5. Command "less" uses for read a big text files: 

For example:


# less /home/mrbit/.bash_history
sudo -s
exit
sudo git status
cd /home/mrbit/DevOps_online_Chernigiv_2021Q4/
ls
cd task1.1/
ls
git branch
git checkout image
sudo git checkout image
git branch
ls
git log
sudo -s
ip a
mc
ip a
sudo mc
sudo netply try
sudo netplan try
sudo nano /etc/netplan/00-installer-config.yaml
sudo netplan try
sudo nano /etc/netplan/00-installer-config.yaml
sudo netplan try
shutdown now
sudo -s
sudo apt upgrade
sudo -s
git status
sudo -s
^@^@^@^@^@


 Command "more" - file perusal filter for crt viewing. 


Keyes for it:


       Options are also taken from the environment variable MORE (make sure to precede them with a dash (-)) but command-line options will override those.

       -d     Prompt with "[Press space to continue, 'q' to quit.]", and display "[Press 'h' for instructions.]" instead of ringing the bell when an illegal
              key is pressed.

       -l     Do not pause after any line containing a ^L (form feed).

       -f     Count logical lines, rather than screen lines (i.e., long lines are not folded).

       -p     Do  not  scroll.  Instead, clear the whole screen and then display the text.  Notice that this option is switched on automatically if the exe‐
              cutable is named page.

       -c     Do not scroll.  Instead, paint each screen from the top, clearing the remainder of each line as it is displayed.

       -s     Squeeze multiple blank lines into one.

       -u     Suppress underlining.

For example:

# more /home/mrbit/.bash_logout


# ~/.bash_logout: executed by bash(1) when login shell exits.

# when leaving the console clear the screen to increase privacy

if [ "$SHLVL" = 1 ]; then
    [ -x /usr/bin/clear_console ] && /usr/bin/clear_console -q
fi
root@devopsonline:/home/mrbit/DevOps_online_Chernigiv_2021Q4# more /home/mrbit/.bash
.bash_history  .bash_logout   .bashrc
root@devopsonline:/home/mrbit/DevOps_online_Chernigiv_2021Q4# more /home/mrbit/.bashrc
# ~/.bashrc: executed by bash(1) for non-login shells.
# see /usr/share/doc/bash/examples/startup-files (in the package bash-doc)
# for examples

# If not running interactively, don't do anything
case $- in
    *i*) ;;
      *) return;;
esac

# don't put duplicate lines or lines starting with space in the history.
# See bash(1) for more options
HISTCONTROL=ignoreboth

# append to the history file, don't overwrite it
shopt -s histappend

# for setting history length see HISTSIZE and HISTFILESIZE in bash(1)
HISTSIZE=1000
HISTFILESIZE=2000

# check the window size after each command and, if necessary,
# update the values of LINES and COLUMNS.
shopt -s checkwinsize



6. For read information about "finger" command i use man command



Very usefull "ls" command - list directory contents. 
Example of use it for home directory:
 

# ls /home/mrbit/ -hla
total 52K
drwxr-xr-x 6 mrbit mrbit 4.0K Nov 29 09:17 .
drwxr-xr-x 3 root  root  4.0K Nov  2 20:39 ..
-rw------- 1 mrbit mrbit  434 Nov 19 18:32 .bash_history
-rw-r--r-- 1 mrbit mrbit  220 Feb 25  2020 .bash_logout
-rw-r--r-- 1 mrbit mrbit 3.7K Feb 25  2020 .bashrc
drwx------ 3 mrbit mrbit 4.0K Nov  5 12:17 .cache
drwx------ 3 mrbit mrbit 4.0K Nov  5 12:17 .config
drwxr-xr-x 9 root  root  4.0K Nov 29 09:16 DevOps_online_Chernigiv_2021Q4
-rw-r--r-- 1 root  root     0 Nov  8 17:42 Differences_of_HVs.txt
drwx------ 3 mrbit mrbit 4.0K Nov  5 12:17 .local
-rw-r--r-- 1 mrbit mrbit  807 Feb 25  2020 .profile
-rw-r--r-- 1 root  root  2.6K Nov  8 17:38 readme.md_2_1
-rw-rw-r-- 1 mrbit mrbit   72 Nov  5 12:19 .selected_editor
-rw-r--r-- 1 mrbit mrbit    0 Nov  2 16:48 .sudo_as_admin_successful
-rw------- 1 mrbit mrbit  116 Nov 29 09:17 .Xauthority


Command "ls" helps me list of content of any folders. There are a lot of keyes, for example some of them:  -a, --all - do not ignore entries starting with; -h, --human-readable - with -l and -s, print sizes like 1K 234M 2G etc; -i, --inode - print the index number of each file; -l - use a long listing format. This is very usefull command.


#####################Part 2#######################

In this task i should use some commands:

1. "tree"

# tree /root/
/root/
├── DevOps_online_Chernigiv_2021Q4
│   └── LICENSE
└── snap
    └── lxd
        ├── 21803
        ├── 21835
        ├── common
        └── current -> 21835

7 directories, 1 file

# tree /home/ -L 2
/home/
└── mrbit
    ├── DevOps_online_Chernigiv_2021Q4
    ├── Differences_of_HVs.txt
    └── readme.md_2_1


 
