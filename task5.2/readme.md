1. /etc/passwd and etc/group files.

/etc/passwd file containe information about all users in system and can containe encrypted passwords.

<img src="" width="300">

<img src="" width="300">

/etc/group file contains information about groups to which users container.

<img src="" width="300">

<img src="" width="300">

Both files containe pseudousers and groups for them. If program not need root privilages, it should work from enother user, for this uses pseudousers. 

<img src="" width="300">

2. UID is the user's identifier. In Linux, every user has an ID. This can be verified with the "id" command or in the / etc / passwd file. UID and user rights are interconnected. All files owned by a user have the UID of that user. 
The UID can be from 0 to 65535. But UID = 0 is defined by the root user. UIDs from 1 to 100 (sometimes 101 to 499 or 101 to 999) are reserved for the system. For the "nobody" user uses the maximum UID or one of the system range.

<img src="" width="300">

3. GID is the group identifier. It can be verified  with the "id" command, in /etc/passwd or /etc/group file.

 
