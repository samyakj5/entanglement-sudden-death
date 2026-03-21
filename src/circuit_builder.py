import random
from qiskit import QuantumCircuit
from qiskit.quantum_info import random_clifford, random_quantum_channel

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
