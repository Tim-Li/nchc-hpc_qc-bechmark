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
sudo apt install nfs-kernel-server -y
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
sudo nano /etc/exports

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
## Install `MPICH`
sudo apt-get install mpich libmpich-dev
- 安裝相關套件
```
sudo apt-get install build-essential
```
- Download [MPICH](https://www.mpich.org/downloads/)
- 安裝 MPICH from source
```
wget https://www.mpich.org/static/downloads/4.2.0/mpich-4.2.0.tar.gz
tar xfz mpich-4.2.0.tar.gz
cd mpich-4.2.0
mkdir build
cd build
../configure --prefix=/opt/nfsdir/mpich-4.2.0 --disable-fortran 2>&1 | tee c.txt
sudo make -j 4 && sudo make install
```
- 加入環境變數
```
sudo nano ~/.bashrc
export MPI_ROOT=/opt/nfsdir/mpich-4.2.0 
export PATH=$MPI_ROOT/bin:$PATH
export LD_LIBRARY_PATH=$MPI_ROOT/lib:$LD_LIBRARY_PATH
<!-- export MANPATH=$MPI_ROOT/man:$MANPATH -->


source ~/.bashrc
```
- 驗證是否安裝成功
```
mpiexec --version
which mpicc mpiexec
```
- `hello_world_c.c`
```
cd /opt/nfsdir/mpich-4.2.0/exmaple
ls -l
nano hell.c
mpicc hello.c -o hello
mpirun hello
# Hellow world, I am 0 of 2, (hpc1)
# Hellow world, I am 1 of 2, (hpc1)
```
## 測試 openmpi 多節點計算
<!-- - 關閉防火牆
```
sudo systemctl stop ufw
sudo systemctl disable ufw
``` -->
- 編輯 `mpi_host` file
```
sudo nano /opt/nfsdir/mpi_host
```
```
# add
hpc1
hpc2
```
- 執行檔案
```
mpirun -np 8 -f /opt/nfsdir/mpi_host ./hel|sort
```
```
# return
Hellow world, I am 0 of 8, (hpc1)
Hellow world, I am 1 of 8, (hpc2)
Hellow world, I am 2 of 8, (hpc1)
Hellow world, I am 3 of 8, (hpc2)
Hellow world, I am 4 of 8, (hpc1)
Hellow world, I am 5 of 8, (hpc2)
Hellow world, I am 6 of 8, (hpc1)
Hellow world, I am 7 of 8, (hpc2)
```
---
## Buildup Qiskit Env
- install miniconda and create env for qiskit
```
# install miniconda
wget https://repo.continuum.io/miniconda/Miniconda3-latest-Linux-x86_64.sh
sh Miniconda3-latest-Linux-x86_64.sh
# set path /opt/nfsdir/miniconda3
conda config --set auto_activate_base false
# create env
conda create --name qiskit python=3.11
# env activate
conda activate qiskit
```
-  install qiskit-aer from source
```
sudo apt-get install git -y
git clone https://github.com/Qiskit/qiskit-aer
cd qiskit-aer
pip install -r requirements-dev.txt
pip install pybind11 auditwheel
sudo apt install build-essential -y
sudo apt install libopenblas-dev -y
python ./setup.py bdist_wheel -- -DAER_MPI=True -DAER_DISABLE_GDR=True
pip install -U dist/qiskit_aer*.whl
```
- install qiskit
```
pip install qiskit==0.45.3
```
## qiskit-aer mpi test
- demo code (sudo nano qv.py)
```
from qiskit import *
from qiskit.circuit.library import *
from qiskit_aer import *
sim = AerSimulator(method='statevector',device='CPU', blocking_enable=True, blocking_qubits=10)
shots = 100
depth=10
qubits =  25
circuit = transpile(QuantumVolume(qubits, depth, seed=0),backend=sim,optimization_level=0)
circuit.measure_all()
result = execute(circuit,sim,shots=shots,seed_simulator=12345, blocking_enable=True, blocking_qubits=10).result()
dict=result.to_dict()
meta = dict['metadata']
myrank = meta['mpi_rank']
data = dict['results'][0]['data']['counts']
print(meta)
```
- run demo code 
```


```
## Research multi-node quantum circuit simulation on HPC
- [Cache Blocking Technique to Large Scale Quantum Computing Simulation on Supercomputers](https://arxiv.org/abs/2102.02957)
- [mpiQulacs: A Distributed Quantum Computer Simulator for A64FX-based Cluster Systems](https://arxiv.org/abs/2203.16044)

```
HYDRA build details:
    Version:                                 3.3.2
    Release Date:                            Tue Nov 12 21:23:16 CST 2019
    CC:                              gcc   -Wl,-Bsymbolic-functions -Wl,-z,relro 
    CXX:                             g++   -Wl,-Bsymbolic-functions -Wl,-z,relro 
    F77:                             f77  -Wl,-Bsymbolic-functions -Wl,-z,relro 
    F90:                             f95  -Wl,-Bsymbolic-functions -Wl,-z,relro 
    Configure options:                       
    '--disable-option-checking' 
    '--prefix=/usr' 
    '--build=x86_64-linux-gnu' 
    '--includedir=${prefix}/include' 
    '--mandir=${prefix}/share/man' 
    '--infodir=${prefix}/share/info' 
    '--sysconfdir=/etc' 
    '--localstatedir=/var' 
    '--disable-silent-rules' 
    '--libdir=${prefix}/lib/x86_64-linux-gnu' 
    '--runstatedir=/run' 
    '--disable-maintainer-mode' 
    '--disable-dependency-tracking' 
    '--with-libfabric' 
    '--enable-shared' 
    '--enable-fortran=all' 
    '--disable-rpath' 
    '--disable-wrapper-rpath' 
    '--sysconfdir=/etc/mpich' 
    '--libdir=/usr/lib/x86_64-linux-gnu' 
    '--includedir=/usr/include/x86_64-linux-gnu/mpich' 
    '--docdir=/usr/share/doc/mpich' 
    'CPPFLAGS= -Wdate-time -D_FORTIFY_SOURCE=2 -I/build/mpich-VeuB8Z/mpich-3.3.2/src/mpl/include -I/build/mpich-VeuB8Z/mpich-3.3.2/src/mpl/include -I/build/mpich-VeuB8Z/mpich-3.3.2/src/openpa/src -I/build/mpich-VeuB8Z/mpich-3.3.2/src/openpa/src -D_REENTRANT -I/build/mpich-VeuB8Z/mpich-3.3.2/src/mpi/romio/include' 
    'CFLAGS= -g -O2 -fdebug-prefix-map=/build/mpich-VeuB8Z/mpich-3.3.2=. -fstack-protector-strong -Wformat -Werror=format-security -O2' 
    'CXXFLAGS= -g -O2 -fdebug-prefix-map=/build/mpich-VeuB8Z/mpich-3.3.2=. -fstack-protector-strong -Wformat -Werror=format-security -O2' 
    'FFLAGS= -g -O2 -fdebug-prefix-map=/build/mpich-VeuB8Z/mpich-3.3.2=. -fstack-protector-strong -O2' 
    'FCFLAGS= -g -O2 -fdebug-prefix-map=/build/mpich-VeuB8Z/mpich-3.3.2=. -fstack-protector-strong -cpp -O2' 
    'BASH_SHELL=/bin/bash' 
    'build_alias=x86_64-linux-gnu' 
    'MPICHLIB_CFLAGS=-g -O2 -fdebug-prefix-map=/build/mpich-VeuB8Z/mpich-3.3.2=. -fstack-protector-strong -Wformat -Werror=format-security' 
    'MPICHLIB_CPPFLAGS=-Wdate-time -D_FORTIFY_SOURCE=2' 
    'MPICHLIB_CXXFLAGS=-g -O2 -fdebug-prefix-map=/build/mpich-VeuB8Z/mpich-3.3.2=. -fstack-protector-strong -Wformat -Werror=format-security' 
    'MPICHLIB_FFLAGS=-g -O2 -fdebug-prefix-map=/build/mpich-VeuB8Z/mpich-3.3.2=. -fstack-protector-strong' 
    'MPICHLIB_FCFLAGS=-g -O2 -fdebug-prefix-map=/build/mpich-VeuB8Z/mpich-3.3.2=. -fstack-protector-strong -cpp' 
    'LDFLAGS=-Wl,-Bsymbolic-functions -Wl,-z,relro' 
    'FC=f95' 
    'F77=f77' 
    'MPILIBNAME=mpich' 
    '--cache-file=/dev/null' 
    '--srcdir=.' 
    'CC=gcc' 
    'LIBS=' 
    'MPLLIBNAME=mpl'

    Process Manager:                         pmi
    Launchers available:                     ssh rsh fork slurm ll lsf sge manual persist
    Topology libraries available:            hwloc
    Resource management kernels available:   user slurm ll lsf sge pbs cobalt
    Checkpointing libraries available:       
    Demux engines available:                 poll select
```