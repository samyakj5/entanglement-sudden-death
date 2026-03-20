# Entanglement Sudden Death in Interacting Quantum Circuits

![Poster](assets/poster.png)

## Abstract

The theoretical aspects of entanglement dynamics in quantum circuits have been at the forefront of quantum information theory research. In particular, random unitary circuit models provide a simple platform for studying entanglement dynamics in generic quantum circuits. Here, we study quantum entanglement dynamics in a random Clifford circuit model, interspersed with single-qubit noise described by quantum channels. We study entanglement dynamics in the presence of noise and competing unitary evolution numerically using Qiskit. The simulation presents numerical evidence that the dissipation time in noisy Clifford circuits is the same as that of noisy circuits. Our work lays the foundation for developing a generalized mathematical proof for the critical time at which a quantum state becomes fully separable when subject to noisy unitary dynamics. If proven, such a theory can be applied to real-world quantum devices and algorithms, assisting with developing fault-tolerant code and hardware.

## Getting Started

```
git clone https://github.com/samyakj5/entanglement-sudden-death
cd entanglement-sudden-death
python -m venv venv
source venv/bin/activate
pip install -r requirements.txt
jupyter notebook
```

## Contents

- Simulation of random Clifford circuits with noise
- Computation of entanglement using logarithmic negativity
- Analysis of entanglement sudden death