from qiskit import *
from qiskit.circuit.library import *
from qiskit_aer import *
sim = AerSimulator(method='statevector',device='CPU', blocking_enable=True, blocking_qubits=10)
shots = 100
depth=10
qubits =  25
circuit = transpile(QuantumVolume(qubits, depth, seed=0),backend=sim,optimization_level=0)
circuit.measure_all()
result = execute(circuit,sim,shots=shots,seed_simulator=12345, blocking_enable=True, blocking_qubits=10).result()
dict=result.to_dict()
meta = dict['metadata']
myrank = meta['mpi_rank']
data = dict['results'][0]['data']['counts']
print(meta)