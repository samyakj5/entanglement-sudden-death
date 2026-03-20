import random
import math
import numpy as np
from qiskit import QuantumCircuit
from qiskit_aer import AerSimulator
from qiskit.quantum_info import DensityMatrix, negativity, random_clifford, random_quantum_channel


def GHZ_state(circuit, L):
    circuit.h(0)
    for qubit in range(1, L):
        circuit.cx(0, qubit)


def rqc(circuit, L, p_rqc):
    for i in range(L):
        if random.random() < p_rqc:
            depolarizingchannel = random_quantum_channel(2)
            circuit.append(depolarizingchannel, [i])


def random_brickwork_circuit(L, p_rqc):
    circuit = QuantumCircuit(L, L**2)
    GHZ_state(circuit, L)

    for t in range(L * 2):
        rqc(circuit, L, p_rqc)
        if t % 2 == 0:
            for i in range(int(L / 2)):
                gate = random_clifford(2)
                circuit.unitary(gate, [2 * i, 2 * i + 1], label=" ")
        else:
            for i in range(int(L / 2)):
                gate = random_clifford(2)
                if 2 * i == L - 2:
                    circuit.unitary(gate, [L - 1, 0], label=" ")
                else:
                    circuit.unitary(gate, [2 * i + 1, 2 * i + 2], label=" ")

        circuit.save_density_matrix(label=f"dm_{t}")
    return circuit


def calculate_log_negativity(dm, subsystem):
    rho = DensityMatrix(dm)
    negv = negativity(rho, subsystem)
    log_negv = math.log(2 * negv + 1, 2)
    return log_negv


def process_p(p, L, num_runs, time_steps):
    sim = AerSimulator()
    final_log_negv = []

    for _ in range(num_runs):
        circuit = random_brickwork_circuit(L, p)
        job = sim.run(circuit)
        result = job.result().data()

        log_negv_runs = []
        for t in time_steps:
            dm = result.get(f"dm_{t}")
            log_negv = calculate_log_negativity(dm, list(range(int(L / 2))))
            log_negv_runs.append(log_negv)

        final_log_negv.append(log_negv_runs)

    avg_log_negv = np.mean(final_log_negv, axis=0)
    std_log_negv = np.std(final_log_negv, axis=0)
    return p, avg_log_negv, std_log_negv