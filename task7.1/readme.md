In task7.1 i should write three scripts on bash language which must fulfill the following requirements:

A. Create a script that uses the following keys:
	

	1. When starting without parameters, it will display a list of possible keys and their description.

	2. The --all key displays the IP addresses and symbolic names of all hosts in the current subnet

	3. The --target key displays a list of open system TCP ports.


The code that performs the functionality of each of the subtasks must be placed in a separate function
For task A  we can use special programs, for example nmap, lsof, portscan. But before use they should be installed. More universal way there is use standart bash commands and Linux sockets. Let's try.  


B. Using Apache log example create a script to answer the following questions:


	1. From which ip were the most requests?

	2. What is the most requested page?

	3. How many requests were there from each ip?

	4. What non-existent pages were clients referred to?

	5. What time did site get the most requests?

	6. What search bots have accessed the site? (UA + IP)



For start scriptB, which pars apache log file, we should use format:
bash scriptB <path to the apache log file>
For testing of the script i used apache_logs.txt file, it is near  scriptB file.


C. Create a data backup script that takes the following data as parameters:


	1. Path to the syncing directory.

	2. The path to the directory where the copies of the files will be stored.

	In case of adding new or deleting old files, the script must add a corresponding entry to the log file indicating the time, type of operation and file name.

	[The command to run the script must be added to crontab with a run frequency of one minute]



For backuping of files/folders/links there are some ways. First and more easy - this is use special programs with deamons, for example rsync. Rsync - perfect tool for syncronice folder to the remoute host. But before use it should be installed and configured. 
Second way - use standart bash commands. Let's try second way as more universal for backuping on the local host, as i think. 
For execute backup script let's configure cron, for this: 
1. open crontab file:
crontab -e  
2. add next line:
*/1 * * * *  bash /home/scriptC /mnt/src/ /mnt/backup/
3. save the changes and check.
crontab -l
