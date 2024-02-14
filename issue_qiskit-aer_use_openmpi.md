## Install openmpi
### Resource
- [Install OpenMPI](https://edu.itp.phys.ethz.ch/hs12/programming_techniques/openmpi.pdf)
- [youtube：OpenMPI Tutorials#](https://www.youtube.com/watch?v=4l2Urt1EkA8)
- 安裝相關套件
```
sudo apt-get install build-essential
```
- Download [openmpi-4.1.6.tar.gz](https://www.open-mpi.org/software/ompi/v4.1/)
- 安裝 openmpi from source
```
tar xf openmpi-4.1.6.tar.gz
cd openmpi-4.1.6
mkdir build
cd build
../configure --prefix=/opt/nfsdir/openmpi-4.1.6
sudo make -j 4 && sudo make install
```
- 加入環境變數
```
sudo nano ~/.bashrc
export PATH=$PATH:$HOME/opt/nfsdir/openmpi-4.1.6/bin
export LD_LIBRARY_PATH=\$LD_LIBRARY_PATH:\$HOME/opt/nfsdir/openmpi-4.1.6/lib
source ~/.bashrc
sudo ldconfig
```
or
```
echo "export PATH=\$PATH:\$HOME/opt/nfsdir/openmpi-4.1.6/bin" >> $HOME/.bashrc
echo "export LD_LIBRARY_PATH=\$LD_LIBRARY_PATH:\$HOME/opt/nfsdir/openmpi-4.1.6/lib" >> $HOME/.bashrc
source ~/.bashrc
sudo ldconfig
```
- 驗證是否安裝成功
```
mpirun -V
ompi_info
```
- `hello_world_c.c`
```
cd /opt/nfsdir/openmpi-4.1.6/exmaple
ls -l
nano hello_c.c
mpicc hello_c.c -o hello_c
mpirun hello_c
# Hello, world, I am 0 of 1, (Open MPI v4.1.6, package: Open MPI root@hpc1 Distribution, ident: 4.1.6, repo rev: v4.1.6, Sep 30, 2023, 104)
```
## 測試 openmpi 多節點計算
- 關閉防火牆
```
sudo systemctl stop ufw
sudo systemctl disable ufw
```
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
mpirun --hostfile /opt/nfsdir/mpi_host hello_c
```
```
# return
Hello, world, I am 2 of 8, (Open MPI v4.1.6, package: Open MPI root@hpc1 Distribution, ident: 4.1.6, repo rev: v4.1.6, Sep 30, 2023, 104)
Hello, world, I am 0 of 8, (Open MPI v4.1.6, package: Open MPI root@hpc1 Distribution, ident: 4.1.6, repo rev: v4.1.6, Sep 30, 2023, 104)
Hello, world, I am 3 of 8, (Open MPI v4.1.6, package: Open MPI root@hpc1 Distribution, ident: 4.1.6, repo rev: v4.1.6, Sep 30, 2023, 104)
Hello, world, I am 1 of 8, (Open MPI v4.1.6, package: Open MPI root@hpc1 Distribution, ident: 4.1.6, repo rev: v4.1.6, Sep 30, 2023, 104)
Hello, world, I am 6 of 8, (Open MPI v4.1.6, package: Open MPI hpc@hpc2 Distribution, ident: 4.1.6, repo rev: v4.1.6, Sep 30, 2023, 103)
Hello, world, I am 7 of 8, (Open MPI v4.1.6, package: Open MPI hpc@hpc2 Distribution, ident: 4.1.6, repo rev: v4.1.6, Sep 30, 2023, 103)
Hello, world, I am 4 of 8, (Open MPI v4.1.6, package: Open MPI hpc@hpc2 Distribution, ident: 4.1.6, repo rev: v4.1.6, Sep 30, 2023, 103)
Hello, world, I am 5 of 8, (Open MPI v4.1.6, package: Open MPI hpc@hpc2 Distribution, ident: 4.1.6, repo rev: v4.1.6, Sep 30, 2023, 103)
```
## uninstall openmpi
- [OpenMPI Install from Source and Uninstall](https://github.com/aws/aws-parallelcluster/wiki/OpenMPI-Install-from-Source-and-Uninstall)
```
sudo apt-get remove openmpi
or 
sudo yum remove openmpi
```