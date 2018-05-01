# 

```bash
su -
su - username
su -l username 
#
sudo /etc/sudoers
---------------
root ALL= (ALL) All
wyy ALL= (ALL) ALL
---------------
visudo
---------------
root ALL= (ALL) All
wyy ALL= (ALL) ALL
---------------
```



# mode

1. /etc/passwd
2. /etc/shadow
3. /etc/group

## command

1. chgrp
2. chown
3. chmod

```
chgrp [-R] groupname dirname/filename
chown [-R] username:groupname dirname/filename

```

## number

+ r 4
+ w 2
+ x 1

## alphabeta

- + - =
- u g o a
```
chmod u=rwx u=rwx,go=rw .bashrc
chmod a+w .bashrc
chmod a-w .bashrc

ls -al .bashrc
```

# file

> r: read contents in directory
> w: modify contents of directory

1. create a new file and directory
2. delete a existed file and directory
3. rename a existed file and directory

> x: access directory



1. file

 + ASCII
 + binary
 + data

2. directory
3. link
4. device

 + block
 + character

```sh
sudo fdisk -l
```
