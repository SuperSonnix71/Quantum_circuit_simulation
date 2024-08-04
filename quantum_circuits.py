import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from qiskit import QuantumCircuit
from qiskit_aer import Aer
from qiskit.visualization import plot_histogram, circuit_drawer

def create_and_run_circuit(num_qubits, num_bits):
    circuit = QuantumCircuit(num_qubits, num_bits)
    circuit.h(0)
    circuit.cx(0, 1)
    circuit.measure(range(num_qubits), range(num_bits))

    backend = Aer.get_backend('qasm_simulator')
    job = backend.run(circuit, shots=1000)
    results = job.result()
    counts = results.get_counts(circuit)

    return circuit, counts

def create_teleportation_circuit():
    teleportation_circuit = QuantumCircuit(3, 3)
    teleportation_circuit.h(1)
    teleportation_circuit.cx(1, 2)
    teleportation_circuit.cx(0, 1)
    teleportation_circuit.h(0)
    teleportation_circuit.measure([0, 1], [0, 1])
    teleportation_circuit.cx(1, 2)
    teleportation_circuit.cz(0, 2)
    teleportation_circuit.measure(2, 2)

    return teleportation_circuit

def run_teleportation_circuit(teleportation_circuit):
    backend = Aer.get_backend('qasm_simulator')
    teleportation_job = backend.run(teleportation_circuit, shots=1000)
    teleportation_results = teleportation_job.result()
    teleportation_counts = teleportation_results.get_counts(teleportation_circuit)

    return teleportation_counts

def save_histogram(counts, filename):
    fig = plot_histogram(counts)
    fig.savefig(filename)
    plt.close(fig)

def save_circuit_diagram(circuit, filename):
    fig = circuit_drawer(circuit, output='mpl', plot_barriers=False)
    fig.savefig(filename)
    plt.close(fig)

def print_ascii_circuit(circuit, name):
    print(f"\nASCII representation of {name}:")
    print(circuit.draw(output='text'))

def main():
    # Simple quantum circuit
    circuit, counts = create_and_run_circuit(2, 2)
    print("Measurement counts:", counts)
    save_histogram(counts, 'measurement_histogram.png')
    save_circuit_diagram(circuit, 'circuit_diagram.png')
    print_ascii_circuit(circuit, "Simple Quantum Circuit")

    # Teleportation circuit
    teleportation_circuit = create_teleportation_circuit()
    teleportation_counts = run_teleportation_circuit(teleportation_circuit)
    print("Teleportation results:", teleportation_counts)
    save_histogram(teleportation_counts, 'teleportation_histogram.png')
    save_circuit_diagram(teleportation_circuit, 'teleportation_circuit_diagram.png')
    print_ascii_circuit(teleportation_circuit, "Quantum Teleportation Circuit")

    print("\nAll plots have been saved as PNG files in the current directory.")

if __name__ == "__main__":
    main()