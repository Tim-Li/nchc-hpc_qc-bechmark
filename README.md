# nchc-hpc_qc-bechmark
## Resource
- https://hackmd.io/tu_fk2RDQSyukJiLVBNzhg#Login-information
- https://github.com/chunyulin/hpc_snippet/wiki/QSim

## Hardware
![image](https://github.com/Tim-Li/nchc-hpc_qc-bechmark/assets/34836120/2f37d6f3-59b8-49bd-b047-796f44b39a6e)
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

## QC
1. XACC
2. Intel-QS
3. qiskit

## Buildup Qiskit Env
- install miniconda and create env for qiskit
  ```
  wget https://repo.continuum.io/miniconda/Miniconda3-latest-Linux-x86_64.sh
  sh Miniconda3-latest-Linux-x86_64.sh
  conda config --set auto_activate_base false
  conda create --name qiskit python=3.10
  ```
- install qiskit
  ```
  pip install qiskit==0.46.0
  pip install qiskit-aer==0.13.2
  pip install qiskit-machine-learning==0.7.1
  ```
