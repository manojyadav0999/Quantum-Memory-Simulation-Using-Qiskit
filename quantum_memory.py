# quantum_memory.py
# Author: Manoj Yadav
# Project: Quantum Memory Simulation Using Qiskit (with Manual Input)

from qiskit import QuantumCircuit
from qiskit_aer import AerSimulator
from qiskit_aer.noise import NoiseModel, depolarizing_error, thermal_relaxation_error
import matplotlib.pyplot as plt

print("\n🧠 Quantum Memory Simulation Using Qiskit 🧠")
print("--------------------------------------------")

# Step 1: Manual Inputs from User
try:
    num_qubits = int(input("Enter number of qubits (e.g., 1 or 2): "))
    shots = int(input("Enter number of simulation shots (e.g., 1024): "))
    depol_prob = float(input("Enter depolarizing error probability (0.0 - 1.0): "))
    relax_time = float(input("Enter relaxation time (T1, in microseconds, e.g., 50): "))
    gate_time = float(input("Enter gate time (in microseconds, e.g., 0.1): "))
except ValueError:
    print("Invalid input! Please enter numeric values only.")
    exit()

print("\n🔧 Building the Quantum Circuit...")

# Step 2: Create Quantum Circuit
qc = QuantumCircuit(num_qubits, num_qubits)

# Apply Hadamard gate to all qubits to create superposition
for i in range(num_qubits):
    qc.h(i)

# Measurement for all qubits
qc.measure_all()

# Step 3: Define Noise Model
noise_model = NoiseModel()

# Create depolarizing and relaxation errors
depol_error = depolarizing_error(depol_prob, 1)
relax_error = thermal_relaxation_error(relax_time, relax_time, gate_time)

# Add combined errors to single-qubit operations
noise_model.add_all_qubit_quantum_error(depol_error, ['h', 'x', 'y', 'z'])
noise_model.add_all_qubit_quantum_error(relax_error, ['h', 'x', 'y', 'z'])

# Step 4: Run the Simulation
simulator = AerSimulator(noise_model=noise_model)
print("\n🚀 Running Simulation... Please wait...")

result = simulator.run(qc, shots=shots).result()
counts = result.get_counts()

# Step 5: Display Results
print("\n✅ Simulation Complete!")
print("Measurement Counts:", counts)

# Step 6: Plot Results
plt.bar(counts.keys(), counts.values(), color='purple')
plt.xlabel("Measured State")
plt.ylabel("Counts")
plt.title("Quantum Memory Simulation Result")
plt.show()

print("\n📊 Observation:")
print("- If the distribution is close to 50-50, memory is stable.")
print("- If it's highly skewed, noise and decoherence have affected the memory.")
print("\nSimulation finished successfully ✅")
