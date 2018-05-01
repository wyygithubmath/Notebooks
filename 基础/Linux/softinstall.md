## 软件

------

### Jupyter

1. Python(Anaconda)

```sh
bash anaconda.sh
source /home/wyy/.bashrc
```

2. R

```R
# 1/3
install.packages(c('repr', 'IRdisplay', 'evaluate', 'crayon', 'pbdZMQ', 'devtools', 'uuid', 'digest'))
# 2/3
devtools::install_github('IRkernel/IRkernel')
# 3/3 system-wide
IRkernel::installspec(user = FALSE)
```
3. Julia
```julia
ENV["JUPYTER"]="C:/Program/anaconda/Scripts/jupyter.exe"
Pkg.add("IJulia")

Pkg.update()

Pkg.build("IJulia")
```

4. Haskell

```sh
# ubuntu
sudo apt-get install -y python3-pip git libtinfo-dev libzmq3-dev libcairo2-dev libpango1.0-dev libmagic-dev libblas-dev liblapack-dev

curl -sSL https://get.haskellstack.org/ | sh
git clone https://github.com/gibiansky/IHaskell
cd IHaskell
pip3 install -r requirements.txt
stack install gtk2hs-buildtools
stack install --fast
ihaskell install --stack
```



### Atom

| Python   | R    | Latex | Markdown |
| -------- | ---- | ----- | -------- |
| hydrogen |      |       |          |

### Matlab

```sh
sudo mount -o loop R2015b_glnxa64.iso /mnt
cd /mnt
sudo ./install
sudo cp /[Your crack directory] /Matlab_R2015b/Matlab_2015b_Linux64_Crack/R2015b/bin/glnxa64/* /usr/local/MATLAB/R2015b/bin/glnxa64
sudo umount /mnt

# uninstall
sudo rm -rf /usr/local/MATLAB/R2014b
sudo rm /usr/local/bin/matlab /usr/local/bin/mcc /usr/local/bin/mex /usr/local/bin/mbuild

# if wrong
sys/os/glnxa64
libstdc++.so.6 -> libstdc++.so.6.old
```

### Latex

1. sublime text
2. atom
3. texstudio

```sh
# ubuntu
suao apt install perl-MD5 perl-tk
sudo perl install-tl
+ O
+ P L Y
+ R
+ I
# Windows
perl
perl install-tl
```



### Mathematica

```
6504-25355-71771
1234-4321-123456
8466-145-331 ：：1
```

### R

```sh
# Ubuntu 1604 LTS
sudo vim/gedit /etc/apt/sources.list 
"deb https://cloud.r-project.org//bin/linux/ubuntu xenial/" 
sudo apt update
sudo apt upgrade
# if wrong
sudo apt-key adv --keyserver keyserver.ubuntu.com --recv-keys E084DAB9 
sudo apt update
sudo apt upgrade

sudo apt install r-base r-base-dev

# Rstudio
sudo apt-get -f install
sudo dpkg -i rstudio.deb

# CentOS
sodu yum install -y R
sodu yum install -y rstudio.rpm

# windows MRS
```

### Youtube

```sh
pip install you-get
pip install youtube-dl
```

## 系统

1. Ubuntu
2. CentOS

```sh
# ubuntu
sudo apt-get -f install
sodu apt-get install -y *
sodu dpkg -i *.deb

# centos
sodu yum install -y epel-release
sudo yum install -y */*.rpm
```
