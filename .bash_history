ll
vim /etc/sysconfig/network-scripts/ifcfg-ens33 
vi /etc/sysconfig/network-scripts/ifcfg-ens33 
systemctl restart network
vi /etc/sysconfig/network-scripts/ifcfg-ens33 
systemctl restart network
systemctl status network
vi /etc/init.d/network 
vi /etc/sysconfig/network-scripts/ifcfg-ens33 
cd /etc/sysconfig/network-scripts/
ll
cp ifcfg-ens33 ifcfg-eth0
rm -f ifcfg-ens33 
systemctl restart network
vi ifcfg-eth0 
systemctl restart network
journalctl -xe
systemctl status firewalld
systemctl stop firewalld
systemctl disable firewalld
systemctl restart network
systemctl stop NetworkManager
systemctl disable NetworkManager
systemctl restart network
cat /var/log/messages 
cat /var/log/messages |grep network
ll
vi ifcfg-eth0 
systemctl restart network
vi ifcfg-eth0 
systemctl restart network
vi /etc/sysconfig/grub 
q!
cd /etc/udev/rules.d/
ll
cd /etc/sysconfig/network-scripts/ifcfg-eth0 
vi /etc/sysconfig/network-scripts/ifcfg-eth0 
reboot
systemctl restart network
cd /etc/sysconfig/network-scripts/
ll
vi ifcfg-eth0 
systemctl restart network
ifconfig
ip a
vi ifcfg-eth0 
reboot
ip a
systemctl restart network
ip a
ping www.baidu.com
cd /etc/sysconfig/network-scripts/
vi ifcfg-eth0 
ping 114.114.114.114
ping 160.6.64.1
ip a
systemctl restart network
ping 160.6.64.1
vi ifcfg-eth0 
reboot
ip a
rm -f * /etc/yum.repos.d/
rm -f * /etc/yum.repos.d/*
wget -O /etc/yum.repos.d/CentOS-Base.repo https://mirrors.aliyun.com/repo/Centos-6.repo
curl -o /etc/yum.repos.d/CentOS-Base.repo https://mirrors.aliyun.com/repo/Centos-6.repo
rm -f * /etc/yum.repos.d/*
curl -o /etc/yum.repos.d/CentOS-Base.repo https://mirrors.aliyun.com/repo/Centos-7.repo
yum clean all
yum makecache
yum -y install yum-plugin-downloadpnly
yum -y install yum-plugin-downloadonly
yum -y install ansible
yum list all | grep ansible
wget https://releases.ansible.com/ansible/ansible-2.7.5.tar.gz
curl -o https://releases.ansible.com/ansible/ansible-2.7.5.tar.gz
curl  https://releases.ansible.com/ansible/ansible-2.7.5.tar.gz
curl -o . https://releases.ansible.com/ansible/ansible-2.7.5.tar.gz
ll
yum -y install wget
wget https://github.com/ansible/ansible/archive/release1.6.1.zip
ll
rm -f release1.6.1.zip 
yum -y install lrzsz
rz
ll
unzip ansible-release1.6.1.zip -d .
yum provides */unzip
yum -y isntall unzip
yum -y install unzip
ll
unzip ansible-release1.6.1.zip -d .
ll
cd ansible-release1.6.1
ll
python setup.py build
pip install setuptools
python setup.py 
yum -y install python-setuptools
python setup.py build
python setup.py install
find / -name 'pip'
cd
yum provides */pip
find / -name 'python2*'
cd /usr/bin/
ll
lwho
who
whoiam
whoia
whoami
find / -name 'python2*'
find / -name 'pip*'
vi /etc/resolv.conf
systemctl restart network
cd
cd ansible-release1.6.1
ll
python setup.py install
curl https://pypi.python.org/simple/pycrypto/
cd
wget http://dl.fedoraproject.org/pub/epel/epel-release-latest-7.noarch.rpm
ll
rpm -ivh epel-release-latest-7.noarch.rpm
yum repolist
yum -y install ansible
yum list
yum list | wc -l
yum list all | wc -l
yum list  |grep python
yum list  |grep docker
ssh-keygen --help
ssh-keygen -t rsa -b 4096
cd .ssh/
ll
ssh-copy-id id_rsa.pub root@160.6.68.14
ssh-copy-id -i id_rsa.pub root@160.6.68.14
vim /etc/hosts
vi /etc/ansible/hosts 
ansible all -m shell -a 'yum -y install vim'
vi /etc/ansible/hosts 
ansible all -m shell -a 'yum -y install vim'
ansible use -m shell -a 'yum -y install vim'
python
ansible -i /etc/ansible/hosts all -m ping
ansible -i /etc/ansible/hosts usqe -m ping
ansible -i /etc/ansible/hosts use -m ping
uname -r
cat /etc/redhat-release 
yum -y remove ansible
yum -y install ansible
cat /etc/ansible/hosts
vi /etc/ansible/hosts
ansible -i /etc/ansible/hosts use -m ping
vi /usr/bin/ansible
ansible -i /etc/ansible/hosts use -m ping
vi /usr/bin/ansible
ansible -i /etc/ansible/hosts use -m ping
vi /usr/bin/ansible
ansible -i /etc/ansible/hosts use -m ping
cd
mkdir ~/.pip
cd .pip/
vi pip.conf
pip3 install ansible
ll
cd /etc/ansible/
ll
cd ..
cd ansible/
ll
cat hosts.rpmsave 
:q!
ll
cp hosts.rpmsave hosts
ansible -i /etc/ansible/hosts use -m ping
vi /etc/ansible/hosts
ansible
ansible --version
ll
cd
ll
find / -name 'ansible'
ansible
/usr/local/bin/ansible use 
echo $PATH
/usr/local/bin/ansible -i /etc/ansible/hosts use -m ping
ansible
find / -name '/usr/bin/ansible: 没有那个文件或目录'
find / -name 'ansible.cfg'
ansible
cd /usr/bin/
kk
ll
find / -name 'ansible'
echo $PATH
ll
cd
cd /etc/an
cd /etc/ansible/
ll
ssh-copy-id root@160.6.68.3
vi hosts
find / -name '*ansible.cfg'
cd
ll
vi /etc/rc.local 
ansible
find / -name 'ansible'
vi /etc/rc.local 
source /etc/rc.local 
ansible
ansible --version
ansible use -m shell 'yum -y install vim'
ansible use -m shell -a 'yum -y install vim'
yum list  | grep bash-complete
yum list  | grep bash-comple
ansible use -m shell -a 'yum -y install bash-completion.noarch'
ll
cd 
cd /
ll
ct 3.txt 
cat 3.txt 
echo > 3.txt 
ls -l /proc/sys/net/ipv4/
ls -lf /proc/sys/net/ipv4/
ls -f /proc/sys/net/ipv4/
ls --help
history
histroy|grep redis
history | grep redis
vim /etc/redis.conf 
ifocnfig
ifconfig
ip a
ansible all -m shell -a 'yum -y isntall ifconfig'
ansible all -m shell -a 'yum -y install ifconfig'
ssh root@160.6.66.76
vim /etc/ansible/hosts
ansible all -m ping
yum provides * /ifconfig
ifconfig
yum list | grep net-tool
yum provides */ifconfig
yum provides */ifconfig|awk '/x86/{print $1}' | yum -y install 
yum provides */ifconfig|awk '/x86/{print $1}'
`yum provides */ifconfig|awk '/x86/{print $1}'` | yum -y install
`yum provides */ifconfig|awk '/x86/{print $1}'` -xargs yum -y install
`yum provides */ifconfig|awk '/x86/{print $1}'` |xargs yum -y install
yum provides */ifconfig|awk '/x86/{print $1}'|grep 
`yum provides */ifconfig|awk '/x86/{print $1}'` |xargs yum -y install
`yum provides */ifconfig|awk '/x86/{print $1}'` | yum -y install
a = `yum provides */ifconfig|awk '/x86/{print $1}'` | yum -y install $a
a = `yum provides */ifconfig|awk '/x86/{print $1}'` && yum -y install $a
a=`yum provides */ifconfig|awk '/x86/{print $1}'` && yum -y install $a
echo $a
echo $a
