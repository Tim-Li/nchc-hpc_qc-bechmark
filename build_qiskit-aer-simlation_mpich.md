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
    - hpc1：192.168.134.10
    - hpc2：192.168.134.11

## 設置 IP 主機映射
```
sudo nano /etc/hosts
# 192.168.134.10 hpc1
# 192.168.134.11 hpc2

# 測試 ping 看看
ping hpc1
ping hpc2
```

## Setup ssh no-password 
- Install ssh
```
sudo apt-get install ssh -y
```
- 生成金鑰
```
# 生成金鑰 (主節點)
ssh-keygen -t rsa
cat ~/.ssh/id_rsa.pub >> ~/.ssh/authorized_keys
```
- 傳送金鑰
```
# 主節點 傳送到 子節點
scp /home/hpc/.ssh/authorized_keys hpc2:~/.ssh/authorized_keys
```
- 驗證
```
# 驗證 (主節點：hpc1)
ssh hpc1
ssh hpc2
```

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

## Install `MPICH`
### From `apt-get`
```
sudo apt-get install mpich libmpich-dev

# uninstall 
sudo apt-get remove mpich 
sudo apt-get remove --auto-remove mpich 
```
### From `source` 
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
### 驗證安裝
```
mpiexec --version
which mpicc mpiexec mpirun
```
- `hello.c`
```
cd /opt/nfsdir/mpich-4.2.0/exmaple
ls -l
nano hello.c
mpicc hello.c -o hello
mpirun hello
# Hellow world, I am 0 of 2, (hpc1)
# Hellow world, I am 1 of 2, (hpc1)
```
### 驗證 `多節點` 計算
<!-- - 關閉防火牆
```
sudo systemctl stop ufw
sudo systemctl disable ufw
``` 
-->
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

## qiskit-aer MPI simulation
### Buildup Qiskit Env
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
sudo apt-get install git build-essential libopenblas-dev -y
git clone https://github.com/Qiskit/qiskit-aer
cd qiskit-aer
pip install -r requirements-dev.txt
pip install pybind11 auditwheel
python ./setup.py bdist_wheel -- -DAER_MPI=True -DAER_DISABLE_GDR=True
pip install -U dist/qiskit_aer*.whl
```
- install qiskit
```
pip install qiskit==0.45.3
```
### qiskit-aer mpi test
- demo code (sudo nano qv.py)
```
from qiskit import *
from qiskit.circuit.library import *
from qiskit_aer import *
sim = AerSimulator(method='statevector',device='CPU', blocking_enable=True, blocking_qubits=10, precision='double')
shots = 100
depth = 10
qubits =  25
circuit = transpile(QuantumVolume(qubits, depth, seed=0),backend=sim,optimization_level=0)
circuit.measure_all()
result = execute(circuit,sim,shots=shots,seed_simulator=12345, blocking_enable=True, blocking_qubits=10, precision='double').result()
dict=result.to_dict()
meta = dict['metadata']
myrank = meta['mpi_rank']
data = dict['results'][0]['data']['counts']
print(meta)
```
- run demo code 
```
mpirun -np 1 python qv.py

# return
{'time_taken_execute': 44.798362483, 'mpi_rank': 0, 'time_taken_parameter_binding': 0.000202007, 'num_mpi_processes': 1, 'num_processes_per_experiments': 1, 'omp_enabled': True, 'max_gpu_memory_mb': 0, 'max_memory_mb': 7902, 'parallel_experiments': 1}
```
```
mpirun -np 2 python qv.py

# return
{'time_taken_execute': 24.663890334, 'mpi_rank': 1, 'time_taken_parameter_binding': 0.000243463, 'num_mpi_processes': 2, 'num_processes_per_experiments': 2, 'omp_enabled': True, 'max_gpu_memory_mb': 0, 'max_memory_mb': 7902, 'parallel_experiments': 1}
{'time_taken_execute': 24.66666312, 'mpi_rank': 0, 'time_taken_parameter_binding': 0.000233067, 'num_mpi_processes': 2, 'num_processes_per_experiments': 2, 'omp_enabled': True, 'max_gpu_memory_mb': 0, 'max_memory_mb': 7902, 'parallel_experiments': 1}
```
```
mpirun -np 4 python qv.py

# return
{'time_taken_execute': 13.590343541, 'mpi_rank': 1, 'time_taken_parameter_binding': 6.7164e-05, 'num_mpi_processes': 4, 'num_processes_per_experiments': 4, 'omp_enabled': True, 'max_gpu_memory_mb': 0, 'max_memory_mb': 7902, 'parallel_experiments': 1}
{'time_taken_execute': 13.590243606, 'mpi_rank': 2, 'time_taken_parameter_binding': 8.5812e-05, 'num_mpi_processes': 4, 'num_processes_per_experiments': 4, 'omp_enabled': True, 'max_gpu_memory_mb': 0, 'max_memory_mb': 7902, 'parallel_experiments': 1}
{'time_taken_execute': 13.590308556, 'mpi_rank': 0, 'time_taken_parameter_binding': 0.000210263, 'num_mpi_processes': 4, 'num_processes_per_experiments': 4, 'omp_enabled': True, 'max_gpu_memory_mb': 0, 'max_memory_mb': 7902, 'parallel_experiments': 1}
{'time_taken_execute': 13.590614883, 'mpi_rank': 3, 'time_taken_parameter_binding': 0.000198609, 'num_mpi_processes': 4, 'num_processes_per_experiments': 4, 'omp_enabled': True, 'max_gpu_memory_mb': 0, 'max_memory_mb': 7902, 'parallel_experiments': 1}
```
```
mpirun -np 6 python qv.py

# return
{'time_taken_execute': 10.894197182, 'mpi_rank': 5, 'time_taken_parameter_binding': 7.6223e-05, 'num_mpi_processes': 6, 'num_processes_per_experiments': 6, 'omp_enabled': True, 'max_gpu_memory_mb': 0, 'max_memory_mb': 7902, 'parallel_experiments': 1}
{'time_taken_execute': 10.894292032, 'mpi_rank': 3, 'time_taken_parameter_binding': 7.4579e-05, 'num_mpi_processes': 6, 'num_processes_per_experiments': 6, 'omp_enabled': True, 'max_gpu_memory_mb': 0, 'max_memory_mb': 7902, 'parallel_experiments': 1}
{'time_taken_execute': 10.894907731, 'mpi_rank': 0, 'time_taken_parameter_binding': 6.783e-05, 'num_mpi_processes': 6, 'num_processes_per_experiments': 6, 'omp_enabled': True, 'max_gpu_memory_mb': 0, 'max_memory_mb': 7902, 'parallel_experiments': 1}
{'time_taken_execute': 10.895332128, 'mpi_rank': 2, 'time_taken_parameter_binding': 9.0659e-05, 'num_mpi_processes': 6, 'num_processes_per_experiments': 6, 'omp_enabled': True, 'max_gpu_memory_mb': 0, 'max_memory_mb': 7902, 'parallel_experiments': 1}
{'time_taken_execute': 10.896393971, 'mpi_rank': 1, 'time_taken_parameter_binding': 7.1912e-05, 'num_mpi_processes': 6, 'num_processes_per_experiments': 6, 'omp_enabled': True, 'max_gpu_memory_mb': 0, 'max_memory_mb': 7902, 'parallel_experiments': 1}
{'time_taken_execute': 10.896700949, 'mpi_rank': 4, 'time_taken_parameter_binding': 7.2801e-05, 'num_mpi_processes': 6, 'num_processes_per_experiments': 6, 'omp_enabled': True, 'max_gpu_memory_mb': 0, 'max_memory_mb': 7902, 'parallel_experiments': 1}
```
```
mpirun -np 8 python qv.py

# return
{'time_taken_execute': 12.092238211, 'mpi_rank': 0, 'time_taken_parameter_binding': 6.812e-05, 'num_mpi_processes': 8, 'num_processes_per_experiments': 8, 'omp_enabled': True, 'max_gpu_memory_mb': 0, 'max_memory_mb': 7902, 'parallel_experiments': 1}
{'time_taken_execute': 12.092379407, 'mpi_rank': 4, 'time_taken_parameter_binding': 7.2023e-05, 'num_mpi_processes': 8, 'num_processes_per_experiments': 8, 'omp_enabled': True, 'max_gpu_memory_mb': 0, 'max_memory_mb': 7902, 'parallel_experiments': 1}
{'time_taken_execute': 12.076616399, 'mpi_rank': 6, 'time_taken_parameter_binding': 7.1571e-05, 'num_mpi_processes': 8, 'num_processes_per_experiments': 8, 'omp_enabled': True, 'max_gpu_memory_mb': 0, 'max_memory_mb': 7902, 'parallel_experiments': 1}
{'time_taken_execute': 12.080465466, 'mpi_rank': 7, 'time_taken_parameter_binding': 7.61e-05, 'num_mpi_processes': 8, 'num_processes_per_experiments': 8, 'omp_enabled': True, 'max_gpu_memory_mb': 0, 'max_memory_mb': 7902, 'parallel_experiments': 1}
{'time_taken_execute': 12.093475145, 'mpi_rank': 5, 'time_taken_parameter_binding': 7.5121e-05, 'num_mpi_processes': 8, 'num_processes_per_experiments': 8, 'omp_enabled': True, 'max_gpu_memory_mb': 0, 'max_memory_mb': 7902, 'parallel_experiments': 1}
{'time_taken_execute': 12.106572619, 'mpi_rank': 1, 'time_taken_parameter_binding': 7.1868e-05, 'num_mpi_processes': 8, 'num_processes_per_experiments': 8, 'omp_enabled': True, 'max_gpu_memory_mb': 0, 'max_memory_mb': 7902, 'parallel_experiments': 1}
{'time_taken_execute': 12.121836523, 'mpi_rank': 3, 'time_taken_parameter_binding': 7.3629e-05, 'num_mpi_processes': 8, 'num_processes_per_experiments': 8, 'omp_enabled': True, 'max_gpu_memory_mb': 0, 'max_memory_mb': 7902, 'parallel_experiments': 1}
{'time_taken_execute': 12.123436689, 'mpi_rank': 2, 'time_taken_parameter_binding': 7.184e-05, 'num_mpi_processes': 8, 'num_processes_per_experiments': 8, 'omp_enabled': True, 'max_gpu_memory_mb': 0, 'max_memory_mb': 7902, 'parallel_experiments': 1}
```
```
mpirun -np 10 python qv.py

# return
{'time_taken_execute': 29.878171447, 'mpi_rank': 2, 'time_taken_parameter_binding': 6.7902e-05, 'num_mpi_processes': 10, 'num_processes_per_experiments': 10, 'omp_enabled': True, 'max_gpu_memory_mb': 0, 'max_memory_mb': 7902, 'parallel_experiments': 1}
{'time_taken_execute': 29.873693804, 'mpi_rank': 9, 'time_taken_parameter_binding': 7.5828e-05, 'num_mpi_processes': 10, 'num_processes_per_experiments': 10, 'omp_enabled': True, 'max_gpu_memory_mb': 0, 'max_memory_mb': 7902, 'parallel_experiments': 1}
{'time_taken_execute': 29.88044808, 'mpi_rank': 7, 'time_taken_parameter_binding': 7.2848e-05, 'num_mpi_processes': 10, 'num_processes_per_experiments': 10, 'omp_enabled': True, 'max_gpu_memory_mb': 0, 'max_memory_mb': 7902, 'parallel_experiments': 1}
{'time_taken_execute': 29.889980141, 'mpi_rank': 0, 'time_taken_parameter_binding': 6.8676e-05, 'num_mpi_processes': 10, 'num_processes_per_experiments': 10, 'omp_enabled': True, 'max_gpu_memory_mb': 0, 'max_memory_mb': 7902, 'parallel_experiments': 1}
{'time_taken_execute': 29.888492437, 'mpi_rank': 6, 'time_taken_parameter_binding': 7.6125e-05, 'num_mpi_processes': 10, 'num_processes_per_experiments': 10, 'omp_enabled': True, 'max_gpu_memory_mb': 0, 'max_memory_mb': 7902, 'parallel_experiments': 1}
{'time_taken_execute': 29.883764117, 'mpi_rank': 8, 'time_taken_parameter_binding': 8.4783e-05, 'num_mpi_processes': 10, 'num_processes_per_experiments': 10, 'omp_enabled': True, 'max_gpu_memory_mb': 0, 'max_memory_mb': 7902, 'parallel_experiments': 1}
{'time_taken_execute': 29.884264334, 'mpi_rank': 3, 'time_taken_parameter_binding': 7.5535e-05, 'num_mpi_processes': 10, 'num_processes_per_experiments': 10, 'omp_enabled': True, 'max_gpu_memory_mb': 0, 'max_memory_mb': 7902, 'parallel_experiments': 1}
{'time_taken_execute': 29.885235713, 'mpi_rank': 1, 'time_taken_parameter_binding': 7.4077e-05, 'num_mpi_processes': 10, 'num_processes_per_experiments': 10, 'omp_enabled': True, 'max_gpu_memory_mb': 0, 'max_memory_mb': 7902, 'parallel_experiments': 1}
{'time_taken_execute': 29.890909823, 'mpi_rank': 4, 'time_taken_parameter_binding': 7.5444e-05, 'num_mpi_processes': 10, 'num_processes_per_experiments': 10, 'omp_enabled': True, 'max_gpu_memory_mb': 0, 'max_memory_mb': 7902, 'parallel_experiments': 1}
{'time_taken_execute': 29.883318743, 'mpi_rank': 5, 'time_taken_parameter_binding': 0.000188913, 'num_mpi_processes': 10, 'num_processes_per_experiments': 10, 'omp_enabled': True, 'max_gpu_memory_mb': 0, 'max_memory_mb': 7902, 'parallel_experiments': 1}
```
```
mpirun -np 12 python qv.py

# return
{'time_taken_execute': 254.338567109, 'mpi_rank': 0, 'time_taken_parameter_binding': 8.3985e-05, 'num_mpi_processes': 12, 'num_processes_per_experiments': 12, 'omp_enabled': True, 'max_gpu_memory_mb': 0, 'max_memory_mb': 7902, 'parallel_experiments': 1}
{'time_taken_execute': 254.33665569, 'mpi_rank': 2, 'time_taken_parameter_binding': 7.2699e-05, 'num_mpi_processes': 12, 'num_processes_per_experiments': 12, 'omp_enabled': True, 'max_gpu_memory_mb': 0, 'max_memory_mb': 7902, 'parallel_experiments': 1}
{'time_taken_execute': 254.329729831, 'mpi_rank': 4, 'time_taken_parameter_binding': 6.576e-05, 'num_mpi_processes': 12, 'num_processes_per_experiments': 12, 'omp_enabled': True, 'max_gpu_memory_mb': 0, 'max_memory_mb': 7902, 'parallel_experiments': 1}
{'time_taken_execute': 254.329064125, 'mpi_rank': 5, 'time_taken_parameter_binding': 7.2205e-05, 'num_mpi_processes': 12, 'num_processes_per_experiments': 12, 'omp_enabled': True, 'max_gpu_memory_mb': 0, 'max_memory_mb': 7902, 'parallel_experiments': 1}
{'time_taken_execute': 254.328494438, 'mpi_rank': 3, 'time_taken_parameter_binding': 7.2864e-05, 'num_mpi_processes': 12, 'num_processes_per_experiments': 12, 'omp_enabled': True, 'max_gpu_memory_mb': 0, 'max_memory_mb': 7902, 'parallel_experiments': 1}
{'time_taken_execute': 254.330537914, 'mpi_rank': 6, 'time_taken_parameter_binding': 6.7845e-05, 'num_mpi_processes': 12, 'num_processes_per_experiments': 12, 'omp_enabled': True, 'max_gpu_memory_mb': 0, 'max_memory_mb': 7902, 'parallel_experiments': 1}
{'time_taken_execute': 254.34295719, 'mpi_rank': 1, 'time_taken_parameter_binding': 6.8545e-05, 'num_mpi_processes': 12, 'num_processes_per_experiments': 12, 'omp_enabled': True, 'max_gpu_memory_mb': 0, 'max_memory_mb': 7902, 'parallel_experiments': 1}
{'time_taken_execute': 254.341988646, 'mpi_rank': 11, 'time_taken_parameter_binding': 6.8746e-05, 'num_mpi_processes': 12, 'num_processes_per_experiments': 12, 'omp_enabled': True, 'max_gpu_memory_mb': 0, 'max_memory_mb': 7902, 'parallel_experiments': 1}
{'time_taken_execute': 254.349793982, 'mpi_rank': 8, 'time_taken_parameter_binding': 6.7763e-05, 'num_mpi_processes': 12, 'num_processes_per_experiments': 12, 'omp_enabled': True, 'max_gpu_memory_mb': 0, 'max_memory_mb': 7902, 'parallel_experiments': 1}
{'time_taken_execute': 254.330765598, 'mpi_rank': 7, 'time_taken_parameter_binding': 8.3385e-05, 'num_mpi_processes': 12, 'num_processes_per_experiments': 12, 'omp_enabled': True, 'max_gpu_memory_mb': 0, 'max_memory_mb': 7902, 'parallel_experiments': 1}
{'time_taken_execute': 254.34570099, 'mpi_rank': 9, 'time_taken_parameter_binding': 7.7303e-05, 'num_mpi_processes': 12, 'num_processes_per_experiments': 12, 'omp_enabled': True, 'max_gpu_memory_mb': 0, 'max_memory_mb': 7902, 'parallel_experiments': 1}
{'time_taken_execute': 254.376562917, 'mpi_rank': 10, 'time_taken_parameter_binding': 8.5075e-05, 'num_mpi_processes': 12, 'num_processes_per_experiments': 12, 'omp_enabled': True, 'max_gpu_memory_mb': 0, 'max_memory_mb': 7902, 'parallel_experiments': 1}
```
```
mpirun -np 12 python qv.py (with precision='single')

# return
{'time_taken_execute': 18.700498105, 'mpi_rank': 0, 'time_taken_parameter_binding': 6.6045e-05, 'num_mpi_processes': 12, 'num_processes_per_experiments': 12, 'omp_enabled': True, 'max_gpu_memory_mb': 0, 'max_memory_mb': 7902, 'parallel_experiments': 1}
{'time_taken_execute': 18.692928258, 'mpi_rank': 8, 'time_taken_parameter_binding': 6.7943e-05, 'num_mpi_processes': 12, 'num_processes_per_experiments': 12, 'omp_enabled': True, 'max_gpu_memory_mb': 0, 'max_memory_mb': 7902, 'parallel_experiments': 1}
{'time_taken_execute': 18.693168002, 'mpi_rank': 9, 'time_taken_parameter_binding': 6.8851e-05, 'num_mpi_processes': 12, 'num_processes_per_experiments': 12, 'omp_enabled': True, 'max_gpu_memory_mb': 0, 'max_memory_mb': 7902, 'parallel_experiments': 1}
{'time_taken_execute': 18.693202822, 'mpi_rank': 10, 'time_taken_parameter_binding': 7.5983e-05, 'num_mpi_processes': 12, 'num_processes_per_experiments': 12, 'omp_enabled': True, 'max_gpu_memory_mb': 0, 'max_memory_mb': 7902, 'parallel_experiments': 1}
{'time_taken_execute': 18.68571332, 'mpi_rank': 11, 'time_taken_parameter_binding': 7.7855e-05, 'num_mpi_processes': 12, 'num_processes_per_experiments': 12, 'omp_enabled': True, 'max_gpu_memory_mb': 0, 'max_memory_mb': 7902, 'parallel_experiments': 1}
{'time_taken_execute': 18.694737099, 'mpi_rank': 2, 'time_taken_parameter_binding': 6.7442e-05, 'num_mpi_processes': 12, 'num_processes_per_experiments': 12, 'omp_enabled': True, 'max_gpu_memory_mb': 0, 'max_memory_mb': 7902, 'parallel_experiments': 1}
{'time_taken_execute': 18.708436667, 'mpi_rank': 4, 'time_taken_parameter_binding': 7.6186e-05, 'num_mpi_processes': 12, 'num_processes_per_experiments': 12, 'omp_enabled': True, 'max_gpu_memory_mb': 0, 'max_memory_mb': 7902, 'parallel_experiments': 1}
{'time_taken_execute': 18.708528842, 'mpi_rank': 5, 'time_taken_parameter_binding': 9.8083e-05, 'num_mpi_processes': 12, 'num_processes_per_experiments': 12, 'omp_enabled': True, 'max_gpu_memory_mb': 0, 'max_memory_mb': 7902, 'parallel_experiments': 1}
{'time_taken_execute': 18.70892664, 'mpi_rank': 1, 'time_taken_parameter_binding': 7.6831e-05, 'num_mpi_processes': 12, 'num_processes_per_experiments': 12, 'omp_enabled': True, 'max_gpu_memory_mb': 0, 'max_memory_mb': 7902, 'parallel_experiments': 1}
{'time_taken_execute': 18.705517224, 'mpi_rank': 7, 'time_taken_parameter_binding': 7.3351e-05, 'num_mpi_processes': 12, 'num_processes_per_experiments': 12, 'omp_enabled': True, 'max_gpu_memory_mb': 0, 'max_memory_mb': 7902, 'parallel_experiments': 1}
{'time_taken_execute': 18.702076578, 'mpi_rank': 3, 'time_taken_parameter_binding': 6.4563e-05, 'num_mpi_processes': 12, 'num_processes_per_experiments': 12, 'omp_enabled': True, 'max_gpu_memory_mb': 0, 'max_memory_mb': 7902, 'parallel_experiments': 1}
{'time_taken_execute': 18.708335952, 'mpi_rank': 6, 'time_taken_parameter_binding': 7.0024e-05, 'num_mpi_processes': 12, 'num_processes_per_experiments': 12, 'omp_enabled': True, 'max_gpu_memory_mb': 0, 'max_memory_mb': 7902, 'parallel_experiments': 1}
```
```
(qiskit) hpc@hpc1:/opt/nfsdir/qiskit_code$ mpirun -f /opt/nfsdir/mpi_host python qv.py
{'time_taken_execute': 24.252068151, 'mpi_rank': 8, 'time_taken_parameter_binding': 6.7989e-05, 'num_mpi_processes': 12, 'num_processes_per_experiments': 12, 'omp_enabled': True, 'max_gpu_memory_mb': 0, 'max_memory_mb': 7902, 'parallel_experiments': 1}
{'time_taken_execute': 24.252606005, 'mpi_rank': 9, 'time_taken_parameter_binding': 6.6392e-05, 'num_mpi_processes': 12, 'num_processes_per_experiments': 12, 'omp_enabled': True, 'max_gpu_memory_mb': 0, 'max_memory_mb': 7902, 'parallel_experiments': 1}
{'time_taken_execute': 24.252513263, 'mpi_rank': 2, 'time_taken_parameter_binding': 6.9184e-05, 'num_mpi_processes': 12, 'num_processes_per_experiments': 12, 'omp_enabled': True, 'max_gpu_memory_mb': 0, 'max_memory_mb': 7902, 'parallel_experiments': 1}
{'time_taken_execute': 24.252837196, 'mpi_rank': 6, 'time_taken_parameter_binding': 9.262e-05, 'num_mpi_processes': 12, 'num_processes_per_experiments': 12, 'omp_enabled': True, 'max_gpu_memory_mb': 0, 'max_memory_mb': 7902, 'parallel_experiments': 1}
{'time_taken_execute': 24.252357968, 'mpi_rank': 0, 'time_taken_parameter_binding': 6.9015e-05, 'num_mpi_processes': 12, 'num_processes_per_experiments': 12, 'omp_enabled': True, 'max_gpu_memory_mb': 0, 'max_memory_mb': 7902, 'parallel_experiments': 1}
{'time_taken_execute': 24.252368374, 'mpi_rank': 3, 'time_taken_parameter_binding': 6.5488e-05, 'num_mpi_processes': 12, 'num_processes_per_experiments': 12, 'omp_enabled': True, 'max_gpu_memory_mb': 0, 'max_memory_mb': 7902, 'parallel_experiments': 1}
{'time_taken_execute': 24.253160348, 'mpi_rank': 11, 'time_taken_parameter_binding': 9.9627e-05, 'num_mpi_processes': 12, 'num_processes_per_experiments': 12, 'omp_enabled': True, 'max_gpu_memory_mb': 0, 'max_memory_mb': 7902, 'parallel_experiments': 1}
{'time_taken_execute': 24.252849509, 'mpi_rank': 5, 'time_taken_parameter_binding': 6.9481e-05, 'num_mpi_processes': 12, 'num_processes_per_experiments': 12, 'omp_enabled': True, 'max_gpu_memory_mb': 0, 'max_memory_mb': 7902, 'parallel_experiments': 1}
{'time_taken_execute': 24.254177534, 'mpi_rank': 1, 'time_taken_parameter_binding': 6.3705e-05, 'num_mpi_processes': 12, 'num_processes_per_experiments': 12, 'omp_enabled': True, 'max_gpu_memory_mb': 0, 'max_memory_mb': 7902, 'parallel_experiments': 1}
{'time_taken_execute': 24.26574886, 'mpi_rank': 10, 'time_taken_parameter_binding': 6.2837e-05, 'num_mpi_processes': 12, 'num_processes_per_experiments': 12, 'omp_enabled': True, 'max_gpu_memory_mb': 0, 'max_memory_mb': 7902, 'parallel_experiments': 1}
{'time_taken_execute': 24.267585641, 'mpi_rank': 7, 'time_taken_parameter_binding': 6.8678e-05, 'num_mpi_processes': 12, 'num_processes_per_experiments': 12, 'omp_enabled': True, 'max_gpu_memory_mb': 0, 'max_memory_mb': 7902, 'parallel_experiments': 1}
{'time_taken_execute': 24.271945592, 'mpi_rank': 4, 'time_taken_parameter_binding': 7.6662e-05, 'num_mpi_processes': 12, 'num_processes_per_experiments': 12, 'omp_enabled': True, 'max_gpu_memory_mb': 0, 'max_memory_mb': 7902, 'parallel_experiments': 1}
```
```
mpirun -np 12 --hostfile /opt/nfsdir/mpi_host /opt/nfsdir/miniconda3/envs/qiskit/bin/python qv.py -quiet
{'time_taken_execute': 10.382807881, 'mpi_rank': 0, 'time_taken_parameter_binding': 7.4158e-05, 'num_mpi_processes': 12, 'num_processes_per_experiments': 12, 'omp_enabled': True, 'max_gpu_memory_mb': 0, 'max_memory_mb': 7902, 'parallel_experiments': 1}
{'time_taken_execute': 10.385085377, 'mpi_rank': 6, 'time_taken_parameter_binding': 0.004404893, 'num_mpi_processes': 12, 'num_processes_per_experiments': 12, 'omp_enabled': True, 'max_gpu_memory_mb': 0, 'max_memory_mb': 7902, 'parallel_experiments': 1}
{'time_taken_execute': 10.376054303, 'mpi_rank': 9, 'time_taken_parameter_binding': 0.004457462, 'num_mpi_processes': 12, 'num_processes_per_experiments': 12, 'omp_enabled': True, 'max_gpu_memory_mb': 0, 'max_memory_mb': 7902, 'parallel_experiments': 1}
{'time_taken_execute': 10.386729067, 'mpi_rank': 3, 'time_taken_parameter_binding': 7.2276e-05, 'num_mpi_processes': 12, 'num_processes_per_experiments': 12, 'omp_enabled': True, 'max_gpu_memory_mb': 0, 'max_memory_mb': 7902, 'parallel_experiments': 1}
{'time_taken_execute': 10.388637528, 'mpi_rank': 2, 'time_taken_parameter_binding': 7.4886e-05, 'num_mpi_processes': 12, 'num_processes_per_experiments': 12, 'omp_enabled': True, 'max_gpu_memory_mb': 0, 'max_memory_mb': 7902, 'parallel_experiments': 1}
{'time_taken_execute': 10.384976803, 'mpi_rank': 1, 'time_taken_parameter_binding': 9.9324e-05, 'num_mpi_processes': 12, 'num_processes_per_experiments': 12, 'omp_enabled': True, 'max_gpu_memory_mb': 0, 'max_memory_mb': 7902, 'parallel_experiments': 1}
{'time_taken_execute': 10.386324729, 'mpi_rank': 4, 'time_taken_parameter_binding': 6.8279e-05, 'num_mpi_processes': 12, 'num_processes_per_experiments': 12, 'omp_enabled': True, 'max_gpu_memory_mb': 0, 'max_memory_mb': 7902, 'parallel_experiments': 1}
{'time_taken_execute': 10.38589027, 'mpi_rank': 10, 'time_taken_parameter_binding': 0.001503165, 'num_mpi_processes': 12, 'num_processes_per_experiments': 12, 'omp_enabled': True, 'max_gpu_memory_mb': 0, 'max_memory_mb': 7902, 'parallel_experiments': 1}
{'time_taken_execute': 10.390739518, 'mpi_rank': 11, 'time_taken_parameter_binding': 0.004433256, 'num_mpi_processes': 12, 'num_processes_per_experiments': 12, 'omp_enabled': True, 'max_gpu_memory_mb': 0, 'max_memory_mb': 7902, 'parallel_experiments': 1}
{'time_taken_execute': 10.392316932, 'mpi_rank': 7, 'time_taken_parameter_binding': 0.003351281, 'num_mpi_processes': 12, 'num_processes_per_experiments': 12, 'omp_enabled': True, 'max_gpu_memory_mb': 0, 'max_memory_mb': 7902, 'parallel_experiments': 1}
{'time_taken_execute': 10.3880852, 'mpi_rank': 5, 'time_taken_parameter_binding': 7.2267e-05, 'num_mpi_processes': 12, 'num_processes_per_experiments': 12, 'omp_enabled': True, 'max_gpu_memory_mb': 0, 'max_memory_mb': 7902, 'parallel_experiments': 1}
{'time_taken_execute': 10.386014699, 'mpi_rank': 8, 'time_taken_parameter_binding': 0.004362279, 'num_mpi_processes': 12, 'num_processes_per_experiments': 12, 'omp_enabled': True, 'max_gpu_memory_mb': 0, 'max_memory_mb': 7902, 'parallel_experiments': 1}
```
## Research multi-node quantum circuit simulation on HPC
- [Cache Blocking Technique to Large Scale Quantum Computing Simulation on Supercomputers](https://arxiv.org/abs/2102.02957)
- [mpiQulacs: A Distributed Quantum Computer Simulator for A64FX-based Cluster Systems](https://arxiv.org/abs/2203.16044)

