import time
from memory_profiler import profile
from memory_profiler import LogFile
import sys
import pandas as pd
from qiskit import *
from qiskit.circuit.library import *
from qiskit_aer import *

data_q = []
data_t = []

fp=open('qv_qc-double-memory_profiler.log','w+')
@profile(stream=fp)
def quantumvolume_qc_benchmark(nb_qubits=2,be,bq):
    time_start = time.perf_counter()
    sim = AerSimulator(method='statevector',device='CPU', blocking_enable=be, blocking_qubits=bq)
    circuit = transpile(QuantumVolume(nb_qubits, nb_qubits, seed=20),backend=sim,optimization_level=0)
    circuit.measure_all()
    result = execute(circuit,sim,shots=100,seed_simulator=20,blocking_enable=be, blocking_qubits=bq).result()
    dict=result.to_dict()
    meta = dict['metadata']
    time_end = time.perf_counter()
    times=round((time_end-time_start),3)
    data_q.append(nb_qubits)
    data_t.append(times)
    print(nb_qubits,times,meta)

quantumvolume_qc_benchmark(1,0,0)
for q in range(1,35):
    quantumvolume_qc_benchmark(q,0,0)
    dict = {"data_q": data_q, "data_t": data_t}
    df = pd.DataFrame(dict)
    df.to_csv("qv_qc-double-data.csv")
sys.stdout = LogFile("memory_profile_log", reportIncrementFlag=False)
