1. For displaing of the processes is used "top" command, "ps -aux" command, "htop" command. 
Any process in linux can has 4 statce:
 - Running State - When the CPU executes a process, it will be in a RUNNING state. When the process is not waiting for any resource and ready to be executed by the CPU, it will be in the RUNNABLE state.
 - SLEEPING state - indicates the process is currently waiting on certain resources. There are two types of SLEEPING processes: INTERRUPTABLE_SLEEP -  When a process is in INTERRUPTABLE_SLEEP, it will wake up from the middle of sleep and process new signals sent to it. UNINTERRUPTABLE_SLEEP: When a process is in UNINTERRUPTABLE_SLEEP, it will not wake up from the middle of sleep even though new signals are sent to it.
 - Stopped State - state indicates that the process has been suspended from proceeding further. 
 - Zombie State - A process will terminate when it calls ‘system exit’ API or when someone else kills the process. When a process terminates, it will release all the data structures and the resources it holds. However, it will not release its slot in the ‘process’ table. Instead, the process will send a SIGCHLD signal to its parent process. Now it’s up to the parent process to release the child process slot in the ‘process’ table. The process will be in ZOMBIE state from the time the child process issues the SIGCHLD signal until the parent process releases the slot in the ‘process’ table.

Let's try look at processes list:

<img src="https://github.com/SDenisko/DevOps_online_Chernigiv_2021Q4/blob/8688f0c40aaeb57ebef8fe47fd140d4e4329e5c8/task5.3/images/ps.jpg" width="300"> 


	D	uninterruptible sleep (usually IO)
	R	running or runnable (on run queue)
	S	interruptible sleep (waiting for an event to complete)
	T	stopped, either by a job control signal or because it is being traced
	W	paging (not valid since the 2.6.xx kernel)
	X	dead (should never be seen)
	Z	defunct ("zombie") process, terminated but not reaped by its parent


For BSD formats and when the stat keyword is used, additional characters may be displayed:

	<	high-priority (not nice to other users)
	N	low-priority (nice to other users)
	L	has pages locked into memory (for real-time and custom IO)
	s	is a session leader
	l	is multi-threaded (using CLONE_THREAD, like NPTL pthreads do)
	+	is in the foreground process group


2. "pstree" command - display a tree of processes. There are a lot of keyes, some of them: 

	-a     Show command line arguments. 
	-A     Use ASCII characters to draw the tree.
	-c     Disable compaction of identical subtrees.  By default, subtrees are compacted whenever possible.
	-g     Show PGIDs.
	-h     Highlight  the  current  process  and  its  ancestors.
	-l     Display long lines.
	-n     Sort processes with the same ancestor by PID instead of by name.  (Numeric sort.)
	-p     Show PIDs.  PIDs are shown as decimal numbers in parentheses after each process name.
	-s     Show parent processes of the specified process.
	-t     Show full names for threads when available.
	-T     Hide threads and only show processes.
	-u     Show uid transitions.

<img src="https://github.com/SDenisko/DevOps_online_Chernigiv_2021Q4/blob/47c412eb4c4fcacb998816de496bceef0e6a7552/task5.3/images/pstree.JPG" width="300">

3. "proc" file system - special file system in unix-system, which is used to get information from the kernel about a system processes.
All information about processes are in the /proc directory. Let's look in it:

<img src="https://github.com/SDenisko/DevOps_online_Chernigiv_2021Q4/blob/47c412eb4c4fcacb998816de496bceef0e6a7552/task5.3/images/procfs.jpg" width="300">

4. There are system information in /proc directory. There are RAM, CPU e.t.c., for example: 

<img src="https://github.com/SDenisko/DevOps_online_Chernigiv_2021Q4/blob/47c412eb4c4fcacb998816de496bceef0e6a7552/task5.3/images/cpuinfo.jpg" width="300">

5. For get information about process (owner, state e.t.c.) is used ps command. Let's try:

<img src="https://github.com/SDenisko/DevOps_online_Chernigiv_2021Q4/blob/47c412eb4c4fcacb998816de496bceef0e6a7552/task5.3/images/ps.jpg" width="300">

6. All kernel processes are created by the kthread process, which has PID = 2. So, all child processes are kernel processes. Let's take a look at them:

<img src="https://github.com/SDenisko/DevOps_online_Chernigiv_2021Q4/blob/47c412eb4c4fcacb998816de496bceef0e6a7552/task5.3/images/ps_kernel.JPG" width="300">

User processes have a different PID from 2. Let's take a look at them:

<img src="https://github.com/SDenisko/DevOps_online_Chernigiv_2021Q4/blob/47c412eb4c4fcacb998816de496bceef0e6a7552/task5.3/images/ps_user.JPG" width="300">

7. For print all processes in system is used "ps -aux" command. Let's take a look at them:

<img src="https://github.com/SDenisko/DevOps_online_Chernigiv_2021Q4/blob/47c412eb4c4fcacb998816de496bceef0e6a7552/task5.3/images/ps_state.jpg" width="300">

8. For display only the processes of a specific user is used "ps -U <username>" command. Let's try: 

<img src="https://github.com/SDenisko/DevOps_online_Chernigiv_2021Q4/blob/47c412eb4c4fcacb998816de496bceef0e6a7552/task5.3/images/ps_for_user.JPG" width="">

9. We can see list of other programs for analyze the processes in man page for ps command . Take a look at them:


	SEE ALSO
	       pgrep(1), pstree(1), top(1), proc(5).


10. "top" command is used for display information about processes in real time.

<img src="https://github.com/SDenisko/DevOps_online_Chernigiv_2021Q4/blob/47c412eb4c4fcacb998816de496bceef0e6a7552/task5.3/images/top.JPG" width="300">

11. If we need to display real-time processes of a specific user, then we should use the -U <username> key for the "top" command:

<img src="https://github.com/SDenisko/DevOps_online_Chernigiv_2021Q4/blob/47c412eb4c4fcacb998816de496bceef0e6a7552/task5.3/images/top_user.JPG" width="300">

12. To control "top" command is used a lot of interactive commands, some of them:

Window 1:Def: Cumulative mode Off.  System: Delay 3.0 secs; Secure mode Off.

 - Z,B,E,e   Global: 'Z' colors; 'B' bold; 'E'/'e' summary/task memory scale
 -  l,t,m     Toggle Summary: 'l' load avg; 't' task/cpu stats; 'm' memory info
 -  0,1,2,3,I Toggle: '0' zeros; '1/2/3' cpus or numa node views; 'I' Irix mode
 -  f,F,X     Fields: 'f'/'F' add/remove/order/sort; 'X' increase fixed-width

 -  L,&,<,> . Locate: 'L'/'&' find/again; Move sort column: '<'/'>' left/right
 -  R,H,J,C . Toggle: 'R' Sort; 'H' Threads; 'J' Num justify; 'C' Coordinates
 -  c,i,S,j . Toggle: 'c' Cmd name/line; 'i' Idle; 'S' Time; 'j' Str justify
 -  x,y     . Toggle highlights: 'x' sort field; 'y' running tasks
 -  z,b     . Toggle: 'z' color/mono; 'b' bold/reverse (only if 'x' or 'y')
 -  u,U,o,O . Filter by: 'u'/'U' effective/any user; 'o'/'O' other criteria
 -  n,#,^O  . Set: 'n'/'#' max tasks displayed; Show: Ctrl+'O' other filter(s)
 -  V,v     . Toggle: 'V' forest view; 'v' hide/show forest view children

 -  k,r       Manipulate tasks: 'k' kill; 'r' renice
 -  d or s    Set update interval
 -  W,Y       Write configuration file 'W'; Inspect other output 'Y'

13. Let's try sort processes in "top" window: 

Sort by time+ :

<img src="https://github.com/SDenisko/DevOps_online_Chernigiv_2021Q4/blob/9eddcc59828abf62563f858dee88505847ab55c8/task5.3/images/time+.JPG" width="300">

Sort by memory used:

<img src="https://github.com/SDenisko/DevOps_online_Chernigiv_2021Q4/blob/9eddcc59828abf62563f858dee88505847ab55c8/task5.3/images/mem.JPG" width="300">

Sort by user:

<img src="https://github.com/SDenisko/DevOps_online_Chernigiv_2021Q4/blob/9eddcc59828abf62563f858dee88505847ab55c8/task5.3/images/user_sort.JPG" width="300">

14. Priority of the process - there are how much CPU time will be given to process. Linux and UNIX® systems use a priority system with 40 priorities, ranging from -20 (highest priority) to 19 (lowest priority.
Processes started by regular users usually have priority 0. To decrease the priority, we can use a regular user, to increase the priority, we need a superuser.
The "nice" command displays our default priority and can increase/decrease it. For "renice" command is used PID of the process.

Let's try increase priority for the apt list --upgradable command:

	mrbit@devopsonline:~$ sudo nice -n 18 apt list --upgradable

	Listing... Done

	gitlab-ce/focal 14.5.2-ce.0 amd64 [upgradable from: 14.4.1-ce.0]

	libgl1-mesa-dri/focal-updates 21.0.3-0ubuntu0.3~20.04.5 amd64 [upgradable from: 21.0.3-0ubuntu0.3~20.04.4]

	libglapi-mesa/focal-updates 21.0.3-0ubuntu0.3~20.04.5 amd64 [upgradable from: 21.0.3-0ubuntu0.3~20.04.4]

	libglx-mesa0/focal-updates 21.0.3-0ubuntu0.3~20.04.5 amd64 [upgradable from: 21.0.3-0ubuntu0.3~20.04.4]

	libgs9-common/focal-updates 9.50~dfsg-5ubuntu4.4 all [upgradable from: 9.50~dfsg-5ubuntu4.3]

	libgs9/focal-updates 9.50~dfsg-5ubuntu4.4 amd64 [upgradable from: 9.50~dfsg-5ubuntu4.3]

	libnetplan0/focal-updates 0.103-0ubuntu5~20.04.5 amd64 [upgradable from: 0.103-0ubuntu5~20.04.3]

	libssl1.1/focal-updates 1.1.1f-1ubuntu2.10 amd64 [upgradable from: 1.1.1f-1ubuntu2.9]

	mesa-vulkan-drivers/focal-updates 21.0.3-0ubuntu0.3~20.04.5 amd64 [upgradable from: 21.0.3-0ubuntu0.3~20.04.4]

	netplan.io/focal-updates 0.103-0ubuntu5~20.04.5 amd64 [upgradable from: 0.103-0ubuntu5~20.04.3]

	openssl/focal-updates 1.1.1f-1ubuntu2.10 amd64 [upgradable from: 1.1.1f-1ubuntu2.9]

	ubuntu-advantage-tools/focal-updates 27.4.2~20.04.1 amd64 [upgradable from: 27.4.1~20.04.1]

	wget/focal-updates 1.20.3-1ubuntu2 amd64 [upgradable from: 1.20.3-1ubuntu1]

<img src="https://github.com/SDenisko/DevOps_online_Chernigiv_2021Q4/blob/9eddcc59828abf62563f858dee88505847ab55c8/task5.3/images/nice.JPG" width="300" >

	mrbit@devopsonline:~$ sudo renice -n 15 12874

	12874 (process ID) old priority 0, new priority 15

<img src="https://github.com/SDenisko/DevOps_online_Chernigiv_2021Q4/blob/9eddcc59828abf62563f858dee88505847ab55c8/task5.3/images/renice.JPG" width="300">

15. For change priority with "top" command is used "r" key. Let's try:

<img src="https://github.com/SDenisko/DevOps_online_Chernigiv_2021Q4/blob/9eddcc59828abf62563f858dee88505847ab55c8/task5.3/images/top_priority20.JPG" width="300" >

<img src="https://github.com/SDenisko/DevOps_online_Chernigiv_2021Q4/blob/9eddcc59828abf62563f858dee88505847ab55c8/task5.3/images/top_priority201.JPG" width="300" >


16. We can kill any process using "kill" command and PID of the process.


	mrbit@devopsonline:~$ sudo kill 12894

Result:

	64 bytes from 8.8.8.8: icmp_seq=1152 ttl=117 time=21.7 ms

	64 bytes from 8.8.8.8: icmp_seq=1153 ttl=117 time=19.7 ms

	64 bytes from 8.8.8.8: icmp_seq=1154 ttl=117 time=22.8 ms

	64 bytes from 8.8.8.8: icmp_seq=1155 ttl=117 time=19.8 ms

	64 bytes from 8.8.8.8: icmp_seq=1156 ttl=117 time=19.8 ms

	64 bytes from 8.8.8.8: icmp_seq=1157 ttl=117 time=21.2 ms

	Terminated


List of the command which we can send with "kill"

	mrbit@devopsonline:~$ kill -l

	 1) SIGHUP       2) SIGINT       3) SIGQUIT      4) SIGILL       5) SIGTRAP

	 6) SIGABRT      7) SIGBUS       8) SIGFPE       9) SIGKILL     10) SIGUSR1

	11) SIGSEGV     12) SIGUSR2     13) SIGPIPE     14) SIGALRM     15) SIGTERM

	16) SIGSTKFLT   17) SIGCHLD     18) SIGCONT     19) SIGSTOP     20) SIGTSTP

	21) SIGTTIN     22) SIGTTOU     23) SIGURG      24) SIGXCPU     25) SIGXFSZ

	26) SIGVTALRM   27) SIGPROF     28) SIGWINCH    29) SIGIO       30) SIGPWR

	31) SIGSYS      34) SIGRTMIN    35) SIGRTMIN+1  36) SIGRTMIN+2  37) SIGRTMIN+3

	38) SIGRTMIN+4  39) SIGRTMIN+5  40) SIGRTMIN+6  41) SIGRTMIN+7  42) SIGRTMIN+8

	43) SIGRTMIN+9  44) SIGRTMIN+10 45) SIGRTMIN+11 46) SIGRTMIN+12 47) SIGRTMIN+13

	48) SIGRTMIN+14 49) SIGRTMIN+15 50) SIGRTMAX-14 51) SIGRTMAX-13 52) SIGRTMAX-12

	53) SIGRTMAX-11 54) SIGRTMAX-10 55) SIGRTMAX-9  56) SIGRTMAX-8  57) SIGRTMAX-7

	58) SIGRTMAX-6  59) SIGRTMAX-5  60) SIGRTMAX-4  61) SIGRTMAX-3  62) SIGRTMAX-2

	63) SIGRTMAX-1  64) SIGRTMAX

	SIGINT - Interrupt (request termination) of the process. This is the signal generated by the CTRL-C control sequence.
	SIGKILL - Force termination of the process (This signal may not be overridden by the process).
	SIGTERM	- Request Termination of the process.
	SIGTSTP - Stop (suspend) the process. This is the signal generated by the CTRL-Z control sequence.
	SIGINT - Signals when the Linux user presses ‘CONTROL-C’
	SIGHUP - Hangs up signals when controlling the terminal or at the end of the controlling processes.
	SIGQUIT - Signals when the Linux user presses ‘CONTROL-D’.




Example:

	mrbit@devopsonline:~$ kill -s SIGKILL 13536

	.....

	64 bytes from 8.8.8.8: icmp_seq=26 ttl=117 time=21.9 ms

	64 bytes from 8.8.8.8: icmp_seq=27 ttl=117 time=20.8 ms

	64 bytes from 8.8.8.8: icmp_seq=28 ttl=117 time=21.9 ms

	64 bytes from 8.8.8.8: icmp_seq=29 ttl=117 time=23.5 ms

	Killed


	mrbit@devopsonline:~$ kill -s SIGSTOP 13538

	...

	64 bytes from 8.8.8.8: icmp_seq=31 ttl=117 time=29.7 ms

	64 bytes from 8.8.8.8: icmp_seq=32 ttl=117 time=24.0 ms

	64 bytes from 8.8.8.8: icmp_seq=33 ttl=117 time=22.1 ms

	64 bytes from 8.8.8.8: icmp_seq=34 ttl=117 time=21.5 ms


	[1]+  Stopped                 ping 8.8.8.8


17. The jobs command displays the status of jobs started in the current terminal window. Jobs are numbered starting from 1 for each session. The job ID numbers are used by some programs instead of PIDs (for example, by fg and bg commands).
The fg command, short for the foreground, is a command that moves a background process on your current Linux shell to the foreground. This contrasts the bg command, short for background, that sends a process running in the foreground to the background in the current shell.  
nohup (No Hang Up) is a command in Linux systems that runs the process even after logging out from the shell/terminal. Usually, every process in Linux systems is sent a SIGHUP (Signal Hang UP) which is responsible for terminating the process after closing/exiting the terminal.


<img src="https://github.com/SDenisko/DevOps_online_Chernigiv_2021Q4/blob/9eddcc59828abf62563f858dee88505847ab55c8/task5.3/images/fg_bg_jobs.JPG" width="300">


########Part 2#########

1. Window 10 OS has embedded Openssh client. There are some commands:

 - ssh-add <path to the private key> - add the private key to the windows.
 - ssh <username>@<host> - ssh connection to the remove host.
 - ssh-keygen - generate private key for current user.

Some keyes for ssh command in Windows10 OS:

	ssh [-46AaCfGgKkMNnqsTtVvXxYy] [-B bind_interface]

	           [-b bind_address] [-c cipher_spec] [-D [bind_address:]port]

	           [-E log_file] [-e escape_char] [-F configfile] [-I pkcs11]

	           [-i identity_file] [-J [user@]host[:port]] [-L address]

	           [-l login_name] [-m mac_spec] [-O ctl_cmd] [-o option] [-p port]

	           [-Q query_option] [-R address] [-S ctl_path] [-W host:port]

	           [-w local_tun[:remote_tun]] destination [command]



<img src="https://github.com/SDenisko/DevOps_online_Chernigiv_2021Q4/blob/9ca18eb9b6c107f875e82ed334c88a493aadfeca/task5.3/images/winssh.JPG" width="300">

<img src="https://github.com/SDenisko/DevOps_online_Chernigiv_2021Q4/blob/9ca18eb9b6c107f875e82ed334c88a493aadfeca/task5.3/images/winsshkeygen.JPG" width="300">

<img src="https://github.com/SDenisko/DevOps_online_Chernigiv_2021Q4/blob/9ca18eb9b6c107f875e82ed334c88a493aadfeca/task5.3/images/winsshcommand.JPG" width="300">

2. The best ways to Secure our SSH Server:

 - Use SSH Protocol Version 2.
 - Use SSH keys instead of passwords or at list use strong usernames and passwords
 - Avoid Port 22.
 - Disable SSH Access with the Root account.
 - Configure idle timeout interval.
 - Disable empty passwords.
 - Limit users SSH access.
 - Allow only specific IP addreses access.
 - Enable Two-Factor Authentication, for example Google Authentification.

Before any changes should be make backup of configuration file:

sudo cp /etc/ssh/sshd_config /etc/ssh/sshd_config_copy

<img src="https://github.com/SDenisko/DevOps_online_Chernigiv_2021Q4/blob/ed8424883260c4d0b82ba9bf7597349c571e6e54/task5.3/images/sshconf1.jpg" width ="300">

<img src="https://github.com/SDenisko/DevOps_online_Chernigiv_2021Q4/blob/ed8424883260c4d0b82ba9bf7597349c571e6e54/task5.3/images/sshconf2.jpg" width ="300">

<img src="https://github.com/SDenisko/DevOps_online_Chernigiv_2021Q4/blob/ed8424883260c4d0b82ba9bf7597349c571e6e54/task5.3/images/sshconf3.jpg" width ="300">

Let's generate new ssh key for connection. SSH keys are 2048 bits by default. We can change this parameter to more security, for example to 4096 bits.

<img src="https://github.com/SDenisko/DevOps_online_Chernigiv_2021Q4/blob/ed8424883260c4d0b82ba9bf7597349c571e6e54/task5.3/images/sshdsa.JPG" width ="300">

<img src="https://github.com/SDenisko/DevOps_online_Chernigiv_2021Q4/blob/ed8424883260c4d0b82ba9bf7597349c571e6e54/task5.3/images/sshecdsa.JPG" width ="300">

<img src="https://github.com/SDenisko/DevOps_online_Chernigiv_2021Q4/blob/ed8424883260c4d0b82ba9bf7597349c571e6e54/task5.3/images/rsa_key.JPG" width ="300">


Port forwarding:


<img src="https://github.com/SDenisko/DevOps_online_Chernigiv_2021Q4/blob/ed8424883260c4d0b82ba9bf7597349c571e6e54/task5.3/images/portforwarding.JPG" width ="300">




Let's check results:



	C:\WINDOWS\system32>ssh -p 9922 mrbit@127.0.0.1

	The authenticity of host '[127.0.0.1]:9922 ([127.0.0.1]:9922)' can't be established.

	ECDSA key fingerprint is SHA256:JV9P1kHWanFWhV6YwchmFv3OaL/na85hQjvQc1l4OCs.

	Are you sure you want to continue connecting (yes/no/[fingerprint])? yes

	Warning: Permanently added '[127.0.0.1]:9922' (ECDSA) to the list of known hosts.

	mrbit@127.0.0.1's password:

	Welcome to Ubuntu 20.04.3 LTS (GNU/Linux 5.4.0-91-generic x86_64)

	 * Documentation:  https://help.ubuntu.com

	 * Management:     https://landscape.canonical.com

	 * Support:        https://ubuntu.com/advantage

	  System information as of Sat 11 Dec 2021 08:59:32 AM UTC

	  System load:  0.72              Processes:               146

	  Usage of /:   75.0% of 8.79GB   Users logged in:         1

	  Memory usage: 16%               IPv4 address for enp0s3: 10.0.2.15

	  Swap usage:   0%

	 * Super-optimized for small spaces - read how we shrank the memory

	   footprint of MicroK8s to make it the smallest full K8s around.

	   https://ubuntu.com/blog/microk8s-memory-optimisation

	13 updates can be applied immediately.

	To see these additional updates run: apt list --upgradable

	*** System restart required ***

	Last login: Fri Dec 10 16:25:55 2021 from 10.0.2.2

	mrbit@devopsonline:~$



3. 

Wireshark: 

ssh connection:


<img src="https://github.com/SDenisko/DevOps_online_Chernigiv_2021Q4/blob/ed8424883260c4d0b82ba9bf7597349c571e6e54/task5.3/images/wireshark.JPG" width="300">

telnet connection:

<img src="https://github.com/SDenisko/DevOps_online_Chernigiv_2021Q4/blob/ed8424883260c4d0b82ba9bf7597349c571e6e54/task5.3/images/telnet.JPG" width="300">



TCPDUMP:

ssh connection:


	mrbit@devopsonline:~/DevOps_online_Chernigiv_2021Q4$ sudo tcpdump --interface any -c 10 -nn

	tcpdump: verbose output suppressed, use -v or -vv for full protocol decode

	listening on any, link-type LINUX_SLL (Linux cooked v1), capture size 262144 bytes

	10:26:50.916625 IP 10.0.2.15.22 > 10.0.2.2.56663: Flags [P.], seq 3317007567:3317007615, ack 1118969558, win 65535, length 48

	10:26:50.917060 IP 10.0.2.2.56663 > 10.0.2.15.22: Flags [.], ack 48, win 65535, length 0

	10:26:50.917125 IP 10.0.2.15.22 > 10.0.2.2.56663: Flags [P.], seq 48:96, ack 1, win 65535, length 48

	10:26:50.917345 IP 10.0.2.2.56663 > 10.0.2.15.22: Flags [.], ack 96, win 65535, length 0

	10:26:50.917459 IP 10.0.2.15.22 > 10.0.2.2.56663: Flags [P.], seq 96:144, ack 1, win 65535, length 48

	10:26:50.917708 IP 10.0.2.2.56663 > 10.0.2.15.22: Flags [.], ack 144, win 65535, length 0

	10:26:50.917855 IP 10.0.2.15.22 > 10.0.2.2.56663: Flags [P.], seq 144:192, ack 1, win 65535, length 48

	10:26:50.918111 IP 10.0.2.2.56663 > 10.0.2.15.22: Flags [.], ack 192, win 65535, length 0

	10:26:50.918987 IP 10.0.2.2.56663 > 10.0.2.15.22: Flags [.], ack 352, win 65535, length 0

	10:26:50.919590 IP 10.0.2.2.56663 > 10.0.2.15.22: Flags [.], ack 480, win 65535, length 0

	10 packets captured

	48 packets received by filter

	30 packets dropped by kernel


Description of the flags:


	S	SYN	Connection Start

	F	FIN	Connection Finish

	P	PUSH	Data push

	R	RST	Connection reset

	.	ACK	Acknowledgment


