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
## Install mpich
- 

## Install openmpi
## Setup ssh no-password 
- install ssh

## 建立共同資料夾
## 測試多節點計算

---
## Buildup Qiskit Env



## Install qiskit-aer from source