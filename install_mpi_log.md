# openmpi 
## From apt-get 
```
sudo apt-get install openmpi-bin openmpi-doc libopenmpi-dev -y
```
## From `source` 
- Download [OpenMPI](https://www.open-mpi.org/)
- Install
```
sudo apt-get install build-essential
wget https://download.open-mpi.org/release/open-mpi/v4.0/openmpi-4.0.3.tar.gz
tar xfz openmpi-4.0.3.tar.gz
cd openmpi-4.0.3
mkdir build
cd build
../configure --prefix=/usr/local
sudo make -j 4 && sudo make install
```
- add PATH
```
sudo nano ~/.bashrc
export PATH="$PATH:/usr/local/bin"
export LD_LIBRARY_PATH="$LD_LIBRARY_PATH:/usr/local/lib/"
source ~/.bashrc
```
- Check install
```
mpiexec --version
which mpicc mpiexec mpirun
ompi_info
```
- Demo：`hello.c`
```
cd /opt/nfsdir/mpich-4.2.0/exmaple
ls -l
nano hello.c
mpicc hello.c -o hello
mpirun hello
# Hellow world, I am 0 of 2, (hpc1)
# Hellow world, I am 1 of 2, (hpc1)
```
-  Demo：`multi-node`
```
# firewell
sudo systemctl stop ufw
sudo systemctl disable ufw
``` 
```
# create `mpi_host` file
sudo nano /opt/nfsdir/mpi_host
# add
hpc1
hpc2
```
```
mpirun -np 8 -f /opt/nfsdir/mpi_host ./hel|sort
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
```
# uninstall
sudo apt-get remove openmpi-bin 
sudo apt-get remove --auto-remove openmpi-bin 
sudo apt-get purge openmpi-bin 
sudo apt-get purge --auto-remove openmpi-bin 
```
# mpich 
## From apt-get 
```
sudo apt-get install mpich libmpich-dev -y
```
## From `source` 
- Download [MPICH](https://www.mpich.org/downloads/)
- Install
```
sudo apt-get install build-essential
wget https://www.mpich.org/static/downloads/4.2.0/mpich-4.2.0.tar.gz
tar xfz mpich-4.2.0.tar.gz
cd mpich-4.2.0
mkdir build
cd build
../configure --prefix=/usr/local --disable-fortran
sudo make -j 4 && sudo make install
```
- add PATH
```
sudo nano ~/.bashrc
export PATH=/opt/nfsdir/mpich-4.2.0/bin:$PATH
export LD_LIBRARY_PATH=/opt/nfsdir/mpich-4.2.0/lib:$LD_LIBRARY_PATH
source ~/.bashrc
```
- Check install
```
mpiexec --version
which mpicc mpiexec mpirun
```
- Demo：`hello.c`
```
cd /opt/nfsdir/mpich-4.2.0/exmaple
ls -l
nano hello.c
mpicc hello.c -o hello
mpirun hello
# Hellow world, I am 0 of 2, (hpc1)
# Hellow world, I am 1 of 2, (hpc1)
```
-  Demo：`multi-node`
```
# firewell
sudo systemctl stop ufw
sudo systemctl disable ufw
``` 
```
# create `mpi_host` file
sudo nano /opt/nfsdir/mpi_host
# add
hpc1
hpc2
```
```
mpirun -np 8 -f /opt/nfsdir/mpi_host ./hel|sort
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
```
# uninstall
sudo apt-get remove mpich 
sudo apt-get remove --auto-remove mpich 
```