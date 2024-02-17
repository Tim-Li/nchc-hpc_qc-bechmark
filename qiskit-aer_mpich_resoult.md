```
python qv.py
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
```
[u2892567@ilgn01 qiskit_aer_simulation]$ /home/u2892567/miniconda3/envs/qiskit_aer/bin/python qv.py
{'time_taken_execute': 3930.274547489, 'mpi_rank': 0, 'time_taken_parameter_binding': 8.0592e-05, 'num_mpi_processes': 1, 'num_processes_per_experiments': 1, 'omp_enabled': True, 'max_gpu_memory_mb': 0, 'max_memory_mb': 257361, 'parallel_experi ments': 1}
```