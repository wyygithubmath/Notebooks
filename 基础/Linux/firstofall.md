# Linux
1. Desktop
 + Ubuntu
 + CentOS
2. Server
 + Debian
 + CentOS
 + openSUSE

## sudo
```
su
apt-get install sudo
vim /etc/sudoers
----------------
"username" ALL=(ALL) ALL
----------------
```
## net
 + CentOS
```
# script
sudo vim /etc/sysconfig/network-scripts/
----------------------------------------

----------------------------------------
# ip
ip address
ip link show
ip link set ens33 up/down
ip link set ens33 dynamic on/off

# nmcli
nmcli general
nmcli networking
nmcli connection
```
 + Debian
```
sudo vim /etc/network/interfaces
sudo /etc/init.d/networking restart
```





