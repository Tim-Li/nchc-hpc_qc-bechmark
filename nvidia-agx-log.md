```
wget https://repo.anaconda.com/miniconda/Miniconda3-latest-Linux-aarch64.sh
sh Miniconda3-latest-Linux-aarch64.sh
conda create -n qiskit_aer python=3.9
```
```
conda install -c conda-forge cuquantum-python cuquantum
```


```
sudo apt-get install git build-essential libopenblas-dev -y
git clone https://github.com/Qiskit/qiskit-aer
cd qiskit-aer
pip install -r requirements-dev.txt
pip install pybind11 auditwheel

python ./setup.py bdist_wheel -- -DAER_MPI=True -DAER_DISABLE_GDR=True -DAER_THRUST_BACKEND=CUDA

python ./setup.py bdist_wheel -- -DAER_THRUST_BACKEND=CUDA -DCUQUANTUM_ROOT=path_to_cuQuantum -DCUTENSOR_ROOT=path_to_cuTENSOR -DAER_ENABLE_CUQUANTUM=true -DCUQUANTUM_STATIC=true --

python ./setup.py bdist_wheel -- -DAER_THRUST_BACKEND=CUDA -DCUQUANTUM_ROOT=/mnt/0df939d1-330b-4358-a893-4975b2b57037/nvagx_qc/miniconda3/envs/qiskit_aer/lib -DCUTENSOR_ROOT=/mnt/0df939d1-330b-4358-a893-4975b2b57037/nvagx_qc/miniconda3/envs/qiskit_aer/lib -DAER_ENABLE_CUQUANTUM=true -DCUQUANTUM_STATIC=true


python ./setup.py bdist_wheel -- -DAER_THRUST_BACKEND=CUDA -DCUQUANTUM_ROOT=/mnt/0df939d1-330b-4358-a893-4975b2b57037/nvagx_qc/miniconda3/envs/qiskit_aer/lib/libcustatevec.so -DCUTENSOR_ROOT=/mnt/0df939d1-330b-4358-a893-4975b2b57037/nvagx_qc/miniconda3/envs/qiskit_aer/lib/libcutensornet.so -DAER_ENABLE_CUQUANTUM=true -DCUQUANTUM_STATIC=true

pip install -U dist/qiskit_aer*.whl
```