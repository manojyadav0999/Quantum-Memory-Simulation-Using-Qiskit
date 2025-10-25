# Quantum-Memory-Simulation-Using-Qiskit

---

## 📘 Project Overview

This project simulates a **Quantum Memory System** using **Qiskit**, where users can manually input parameters such as:

* Number of qubits
* Noise probability
* Relaxation time (T1)
* Gate operation time
* Number of simulation shots

The simulation demonstrates how **quantum information degrades due to noise and decoherence**, reflecting the real-world behavior of quantum memory.

---

## 🧾 Features

✅ Manual user input for simulation parameters
✅ Simulates noise (Depolarizing & Relaxation errors)
✅ Displays quantum measurement results as a graph
✅ Demonstrates quantum superposition and decoherence
✅ Educational project for beginners in Quantum Computing

---

## 🧰 Technologies Used

* **Python 3.12+**
* **Qiskit** – For creating and simulating quantum circuits
* **Qiskit Aer** – For noise modeling and simulation backend
* **Matplotlib** – For visualizing results

---

## 🧩 Installation

### Step 1: Clone the repository

```bash
git clone https://github.com/<your-username>/quantum-memory-simulation.git
cd quantum-memory-simulation
```

### Step 2: Create a virtual environment (optional)

```bash
python -m venv venv
venv\Scripts\activate    # Windows
source venv/bin/activate # Linux/Mac
```

### Step 3: Install dependencies

```bash
pip install -r requirements.txt
```

*(or manually run)*

```bash
pip install qiskit matplotlib
```

---

## ▶️ How to Run

Run the simulation file:

```bash
python quantum_memory.py
```

You will be prompted to enter:

```
Enter number of qubits (e.g., 1 or 2): 1
Enter number of simulation shots (e.g., 1024): 1024
Enter depolarizing error probability (0.0 - 1.0): 0.05
Enter relaxation time (T1, in microseconds, e.g., 50): 50
Enter gate time (in microseconds, e.g., 0.1): 0.1
```

The program will:

1. Build a quantum circuit
2. Apply the given noise model
3. Run the simulation
4. Display a **bar graph** of measured quantum states (|0⟩ and |1⟩)

---

## 📊 Example Output

```
Measurement Counts: {'0': 531, '1': 493}
```

The graph will show how often each state was measured — demonstrating the effects of noise on quantum memory.

---

## ⚙️ Project Structure

```
quantum-memory-simulation/
│
├── quantum_memory.py     # Main simulation code
├── README.md             # Project documentation
└── requirements.txt      # Dependencies
```

---

## 🧪 Concept Explanation

* **Hadamard Gate (H):** Creates a superposition state for each qubit.
* **Noise Model:** Simulates environmental interference using:

  * *Depolarizing Error* – randomizes qubit state.
  * *Relaxation Error* – simulates energy loss over time (T1 decay).
* **AerSimulator:** Executes the circuit with the defined noise model.
* **Matplotlib Plot:** Displays how the noise affects measurement probabilities.

---

## 🔬 Applications

* Research in **Quantum Memory and Error Correction**
* **Forensic Data Preservation** using quantum principles
* Quantum communication and cryptography
* Educational demonstrations of decoherence

---

## 🧾 References

* [Qiskit Documentation](https://qiskit.org/documentation/)
* IBM Quantum Lab
* Nielsen & Chuang — *Quantum Computation and Quantum Information*

---
### 👨‍💻 Author: **Manoj Yadav**
---
## 📜 License

This project is open-source under the **MIT License** — you are free to use, modify, and share for educational purposes.

---

Would you like me to generate the matching **`requirements.txt`** file now (so GitHub users can install everything in one command)?
