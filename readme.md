# Quantum Circuit Simulator

This project demonstrates basic quantum computing concepts using Qiskit, including a simple quantum circuit and a quantum teleportation circuit.

## Table of Contents
1. [Installation](#installation)
2. [Usage](#usage)
3. [Features](#features)
4. [Output](#output)
5. [Contributing](#contributing)
6. [License](#license)

## Installation

To run this project, you need Python 3.7 or later. Follow these steps to set up the project:

1. Clone this repository:
https://github.com/SuperSonnix71/Quantum_circuit_simulation
cd Quantum_circuit_simulation

2. (Optional) Create and activate a virtual environment:
python -m venv venv
source venv/bin/activate # On Windows, use venv\Scripts\activate

3. Install the required packages:
pip install qiskit matplotlib

## Usage

Run the main script:
python quantum_circuits.py

This will execute both the simple quantum circuit and the quantum teleportation circuit, display results, and save visualizations.

## Features

- Simulates a simple two-qubit quantum circuit demonstrating superposition and entanglement.
- Implements and simulates a quantum teleportation circuit.
- Generates and saves histograms of measurement outcomes.
- Creates and saves visual representations of quantum circuits.
- Displays ASCII art representations of circuits in the console.

## Output

The script produces the following output:

1. Console output:
   - Measurement counts for the simple circuit
   - ASCII representation of the simple quantum circuit
   - Teleportation results
   - ASCII representation of the quantum teleportation circuit

2. Image files (saved in the project directory):
   - `measurement_histogram.png`: Histogram of the simple circuit outcomes
   - `circuit_diagram.png`: Visual diagram of the simple quantum circuit
   - `teleportation_histogram.png`: Histogram of the teleportation circuit outcomes
   - `teleportation_circuit_diagram.png`: Visual diagram of the teleportation circuit

## Contributing

Contributions to this project are welcome! Please fork the repository and submit a pull request with your changes.

## License

This project is open source and available under the [MIT License](LICENSE).