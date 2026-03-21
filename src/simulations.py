import numpy as np
from qiskit_aer import AerSimulator
from .entanglement_measures import *
from .circuit_builder import *

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
            log_negv = log_negativity(dm, list(range(int(L / 2))))
            log_negv_runs.append(log_negv)

        final_log_negv.append(log_negv_runs)

    avg_log_negv = np.mean(final_log_negv, axis=0)
    std_log_negv = np.std(final_log_negv, axis=0)
    return p, avg_log_negv, std_log_negv
import numpy as np
from qiskit_aer import AerSimulator
from .entanglement_measures import *
from .circuit_builder import *

def run_p_experiments(p, L, num_runs, time_steps):
    sim = AerSimulator()
    final_log_negv = []

    for _ in range(num_runs):
        circuit = random_brickwork_circuit(L, p)
        job = sim.run(circuit)
        result = job.result().data()

        log_negv_runs = []
        for t in time_steps:
            dm = result.get(f"dm_{t}")
            log_negv = log_negativity(dm, list(range(int(L / 2))))
            log_negv_runs.append(log_negv)

        final_log_negv.append(log_negv_runs)

    avg_log_negv = np.mean(final_log_negv, axis=0)
    std_log_negv = np.std(final_log_negv, axis=0)
    return p, avg_log_negv, std_log_negv
