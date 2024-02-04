from qiskit.circuit.library import QuantumVolume
from qiskit_aer import AerSimulator
import time
from memory_profiler import profile
from memory_profiler import LogFile
import sys
import pandas as pd

data_q = []
data_t = []
seed=20
backend_Aer = AerSimulator(method='statevector', 
                        precision='double',          # "single" or "double"
                        max_parallel_threads=0,      # maximum number of CPU cores used by OpenMP for parallelization
                        max_parallel_experiments=0,  # maximum number of qobj experiments that may be executed in parallel
                        max_parallel_shots=None,     # maximum number of shots that may be executed in parallel during each experiment execution
                        blocking_enable=True,        # enables parallelization with multiple GPUs or multiple processes with MPI (CPU/GPU)
                        blocking_qubits=23,          # number of qubits of chunk size used for parallelizing with multiple GPUs or multiple processes with MPI (CPU/GPU)
                        chunk_swap_buffer_qubits=15, # number of qubits of maximum buffer size (=2^chunk_swap_buffer_qubits) used for multiple chunk-swaps over MPI processes
                        num_threads_per_device=1,    # number of threads per device
                        shot_branching_enable=False,
                        shot_branching_sampling_enable=False,
                        accept_distributed_results=None,
                        runtime_parameter_bind_enable=False,
                        statevector_parallel_threshold=25,
                        statevector_sample_measure_opt=10,
                        seed_simulator=seed,
                        shots=100, 
                        )
# print('backend opt:',backend_Aer.options)
fp=open('memory_profiler.log','w+')
@profile(stream=fp)
def quantumvolume_qc_benchmark(nb_qubits=2):
    time_start = time.perf_counter()
    qc_qv = QuantumVolume(nb_qubits,seed=seed).decompose()
    qc_qv.measure_all()
    expdata_Aer = backend_Aer.run(qc_qv).result()
    # counts_ideal_Aer = expdata_Aer.get_counts(0)
    time_end = time.perf_counter()
    times=round((time_end-time_start),3)
    data_q.append(nb_qubits)
    data_t.append(times)
    print(nb_qubits,times)

quantumvolume_qc_benchmark(1)
for q in range(1,30):
    quantumvolume_qc_benchmark(q)
    dict = {"data_q": data_q, "data_t": data_t}
    df = pd.DataFrame(dict)
    df.to_csv("qv_qc-double-data.csv")
sys.stdout = LogFile("memory_profile_log-qv_qc-double", reportIncrementFlag=True)
