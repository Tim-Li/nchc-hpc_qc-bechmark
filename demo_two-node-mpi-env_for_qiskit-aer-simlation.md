# Demo：two-node mpi env for qiskit-aer quantum circuit simulation on `vmware-ubuntu-20.04` virtual system
## Resource
1. [【Python-分布式】MPI集群环境搭建](https://blog.csdn.net/ztf312/article/details/80832506)
2. [利用两台Ubuntu模拟集群，安装MPICH3手把手图文教程-CSDN博客](https://blog.csdn.net/sinat_38368658/article/details/116945650)

## Build two `vmware-ubuntu-20.04` virtual system
- Download and Install [VMware Workstation Pro 17](https://www.vmware.com/tw/products/workstation-pro/workstation-pro-evaluation.html) .
- [Free VMware Workstation Pro 17 full license keys](https://gist.github.com/PurpleVibe32/30a802c3c8ec902e1487024cdea26251)：`MC60H-DWHD5-H80U9-6V85M-8280D`
- Download [Ubuntu 20.04.6 LTS (Focal Fossa)](https://releases.ubuntu.com/20.04.6/?_gl=1*1mb9fkc*_gcl_au*MTQ4NjEwMTEwNy4xNzA0OTkyMDI5&_ga=2.136896633.858023737.1704991985-2017594402.1704991985) iso file.
- Create two Ubuntu 20.04 virtual system
- `user name` 和 `password` 需要一致 (hpc/5780281)
- 更新系統
    ```
    sudo apt-get upgrade
    sudo apt-get update
    reboot
    ```
- issue：[Cannot connect the virtual device sata0:1 because no corresponding device is available on the host [closed]](https://stackoverflow.com/questions/43429362/cannot-connect-the-virtual-device-sata01-because-no-corresponding-device-is-ava)
- Install virtual machine tools
    - Rource：https://kb.vmware.com/s/article/1022525
    1. For Workstation: VM > Install VMware Tools.
    2. Open the VMware Tools CD mounted on the Ubuntu desktop
    3. Right-click the file name that is similar to `VMwareTools.x.x.x-xxxx.tar.gz`
    4. Right-click the file name that is similar to VMwareTools.x.x.x-xxxx.tar.gz on the Ubuntu Desktop, click `Extract here`.
    5. `cd Desktop/vmware-tools-distrib`
    6. `sudo chmod u+x vmware-install.pl`
    7. `sudo ./vmware-install.pl`
    8. `reboot`

- Modify `hostname`
    ```
    sudo nano /etc/hostname
    # hpc1 and hpc2
    reboot
    ```
- Setup `固定IP`
    - Resouce：[VMWare中Ubuntu设置固定IP上网](https://blog.csdn.net/wolf_soul/article/details/46409323)
    - hpc1：192.168.230.2
    - hpc2：192.168.230.3
---
## 設置 IP 主機映射
```
sudo nano /etc/hosts
# 192.168.230.2 hpc1
# 192.168.230.3 hpc2

# 測試 ping 看看
ping hpc1
ping hpc2
```

## Setup ssh no-password 
### Install ssh
```
sudo apt-get install ssh -y
```
### 生成金鑰
```
# 生成金鑰 (主節點)
ssh-keygen -t rsa
cat ~/.ssh/id_rsa.pub >> ~/.ssh/authorized_keys
```
### 傳送金鑰
```
# 主節點 傳送到 子節點
scp /home/hpc/.ssh/authorized_keys hpc2:~/.ssh/authorized_keys
```
### 驗證
```
# 驗證 (主節點：hpc1)
ssh hpc1
ssh hpc2
```
---
## 建立共同資料夾
### 配置nfs服务器端
- 安裝 nfs
```
sudo apt install nfs-kernel-server
sudo systemctl status nfs-server
```
- 創建 nfs 共享目录
```
sudo mkdir /opt/nfsdir
sudo chown nobody:nogroup /opt/nfsdir
sudo chmod -R 777 /opt/nfsdir
```
- 授權 客户端訪問 nfs server
```
sudo vi /etc/exports

# 加入下方指令，並儲存後退出
/opt/nfsdir 192.168.230.3/24(rw,sync,no_subtree_check)

sudo exportfs -a
sudo systemctl restart nfs-kernel-server
```
- 配置防火牆
```
sudo ufw allow from 192.168.230.3/24 to any port nfs

# check
sudo ufw enable
sudo ufw status
```
### 配置nfs客户端
- 安裝
```
sudo apt install nfs-common
```
- 创建用来挂载 nfs server的本地目录
```
sudo mkdir -p /opt/nfsdir
```
- 挂载 nfs server 共享目录到这个客户端本地目录
```
sudo mount hpc1:/opt/nfsdir /opt/nfsdir
```
- Check
```
# (hpc1)
cd /opt/nfsdir 
touch a.txt

# (hpc2)
cd /opt/nfsdir 
ls
```
- 设置永久挂载
```
sudo nano /etc/fstab
hpc1:/opt/nfsdir /opt/nfsdir   nfs   defaults,timeo=15,retrans=5,_netdev	0 0
```

---
./configure --prefix=/home/omnisky/xy/MPI --disable-fortran
---
## Buildup Qiskit Env



## Install qiskit-aer from source


## Research multi-node quantum circuit simulation on HPC
- [Cache Blocking Technique to Large Scale Quantum Computing Simulation on Supercomputers](https://arxiv.org/abs/2102.02957)
- [mpiQulacs: A Distributed Quantum Computer Simulator for A64FX-based Cluster Systems](https://arxiv.org/abs/2203.16044)