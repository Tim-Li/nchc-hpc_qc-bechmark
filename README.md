# nchc-hpc_qc-bechmark
## Resource
- https://hackmd.io/tu_fk2RDQSyukJiLVBNzhg#Login-information
- https://github.com/chunyulin/hpc_snippet/wiki/QSim

## Hardware
![alt text](figure/orm67ua2.png)
```
cat /proc/cpuinfo
srun lsblk
```

## Software
- OS：RHEL8.7
- Toolchain
  1. GCC 8.5.0(default)
  2. Intel oneAPI
  3. NVHPC

## Quantum Computing Tools
1. **qiskit**
2. Intel-QS
3. XACC

## Buildup Qiskit Env
- install miniconda and create env for qiskit
```
# install miniconda
wget https://repo.continuum.io/miniconda/Miniconda3-latest-Linux-x86_64.sh
sh Miniconda3-latest-Linux-x86_64.sh
# set path /opt/nfsdir/miniconda3
conda config --set auto_activate_base false
# create env
conda create --name qiskit python=3.10
# env activate
conda activate qiskit
```
- install qiskit
```
pip install qiskit==0.46.0
pip install qiskit-aer==0.13.2
pip install qiskit-machine-learning==0.7.1
pip install qiskit-experiments==0.5.4
```
- others
```
pip install -U memory_profiler
```
### install qiskit-aer from source
```
python ./setup.py bdist_wheel -- -DAER_MPI=True -DAER_DISABLE_GDR=True
```
### install python from source
- https://ubuntuhandbook.org/index.php/2021/10/compile-install-python-3-10-ubuntu/
- https://stackoverflow.com/questions/8097161/how-would-i-build-python-myself-from-source-code-on-ubuntu


## Twnia-4 HPC QC bechmarking

