1. For displaing of the processes is used "top" command, "ps -aux" command, "htop" command. 
Any process in linux can has 4 statce:
 - Running State - When the CPU executes a process, it will be in a RUNNING state. When the process is not waiting for any resource and ready to be executed by the CPU, it will be in the RUNNABLE state.
 - SLEEPING state - indicates the process is currently waiting on certain resources. There are two types of SLEEPING processes: INTERRUPTABLE_SLEEP -  When a process is in INTERRUPTABLE_SLEEP, it will wake up from the middle of sleep and process new signals sent to it. UNINTERRUPTABLE_SLEEP: When a process is in UNINTERRUPTABLE_SLEEP, it will not wake up from the middle of sleep even though new signals are sent to it.
 - Stopped State - state indicates that the process has been suspended from proceeding further. 
 - Zombie State - A process will terminate when it calls ‘system exit’ API or when someone else kills the process. When a process terminates, it will release all the data structures and the resources it holds. However, it will not release its slot in the ‘process’ table. Instead, the process will send a SIGCHLD signal to its parent process. Now it’s up to the parent process to release the child process slot in the ‘process’ table. The process will be in ZOMBIE state from the time the child process issues the SIGCHLD signal until the parent process releases the slot in the ‘process’ table.

Let's try look at processes list:

<img src="" width="300"> 


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
	I	is multi-threaded (using CLONE_THREAD, like NPTL pthreads do)
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

<img src="" width="300">

3. "proc" file system - special file system in unix-system, which is used to get information from the kernel about a system processes.
All information about processes are in the /proc directory. Let's look in it:

<img src="" width="300">

4. There are system information in /proc directory. There are RAM, CPU e.t.c., for example: 

<img src="" width="300">

5.  