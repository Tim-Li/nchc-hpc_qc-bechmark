from qiskit_experiments.library import QuantumVolume
from qiskit_aer import AerSimulator, StatevectorSimulator
import time
from memory_profiler import profile
from memory_profiler import LogFile
import sys

seed=20
backend_Aer = AerSimulator(method='statevector', 
                        precision='double',          # "single" or "double"
                        max_parallel_threads=0,      # maximum number of CPU cores used by OpenMP for parallelization
                        max_parallel_experiments=1,  # maximum number of qobj experiments that may be executed in parallel
                        max_parallel_shots=None,     # maximum number of shots that may be executed in parallel during each experiment execution
                        blocking_enable=False,       # enables parallelization with multiple GPUs or multiple processes with MPI (CPU/GPU)
                        blocking_qubits=0,           # number of qubits of chunk size used for parallelizing with multiple GPUs or multiple processes with MPI (CPU/GPU)
                        chunk_swap_buffer_qubits=15, # number of qubits of maximum buffer size (=2^chunk_swap_buffer_qubits) used for multiple chunk-swaps over MPI processes
                        batched_shots_gpu=False,     # enables batched execution of multiple shot simulations on GPU devices
                        batched_shots_gpu_max_qubits=16,
                        num_threads_per_device=1,    # number of threads per device
                        shot_branching_enable=False,
                        shot_branching_sampling_enable=False,
                        accept_distributed_results=None,
                        runtime_parameter_bind_enable=False,
                        statevector_parallel_threshold=25,
                        statevector_sample_measure_opt=10,
                        seed_simulator=seed, 
                        )
fp=open('memory_profiler.log','w+')
@profile(stream=fp)
def quantumvolume_qc_benchmark(nb_qubits = 2):
    time_start = time.perf_counter()
    qubits = tuple(range(nb_qubits))
    qv_exp = QuantumVolume(qubits, seed=seed, trials=2)
    qc = qv_exp.circuits()
    qc_qv = qc[0].decompose()
    # print('backend opt:',backend_Aer.options)
    expdata_Aer = backend_Aer.run(qc_qv).result()
    # counts_ideal_Aer = expdata_Aer.get_counts(0)
    time_end = time.perf_counter()
    print(nb_qubits,round((time_end-time_start),3))

quantumvolume_qc_benchmark(1)
for q in range(1,4):
    quantumvolume_qc_benchmark(q)
sys.stdout = LogFile("memory_profile_log", reportIncrementFlag=True)