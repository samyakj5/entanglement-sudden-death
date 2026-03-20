import math
from qiskit.quantum_info import DensityMatrix, negativity

def log_negativity(dm, subsystem):
    rho = DensityMatrix(dm)
    negv = negativity(rho, subsystem)
    return (math.log(2 * negv + 1, 2))