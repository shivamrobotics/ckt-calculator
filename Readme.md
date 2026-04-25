# 🔥 Heat Exchanger Circuit Distribution Tool

A constraint-based engineering tool for calculating balanced circuit distributions in plate-type heat exchanger systems.

This tool was developed to eliminate manual trial-and-error calculations commonly performed during heat exchanger circuit design.

---

## 🚀 Problem Statement

During heat exchanger design, circuit distribution must satisfy:

- Total plate geometry constraints (V × H)
- Dummy hole adjustments
- Parity constraints (Even / Odd / Both)
- Minimum holes per circuit
- Balanced distribution across circuits

Manual calculation is time-consuming and error-prone.

This tool solves the constraint system programmatically.

---

## ⚙️ Features

✅ Balanced circuit distribution  
✅ Even-only / Odd-only enforcement  
✅ Two-step distribution solver (s and s+2 logic)  
✅ Minimum hole constraint  
✅ Dummy hole feasibility validation  
✅ Clean CLI-based interface  
✅ No external dependencies  

---

## 🧮 Mathematical Model

Given:

Total holes:
```
T = V × H
```

Usable holes:
```
U = T − Dummy
```

We solve the constraint:

```
s·x + (s+2)·y = U
x + y = N
```

Subject to:
- Parity constraints
- Minimum hole requirements
- Integer feasibility

---

## 🛠 Installation

No external libraries required.

Clone the repository:

```bash
git clone https://github.com/your-username/heat-exchanger-distribution.git
cd heat-exchanger-distribution
```

Run:

```bash
python heat_exchanger_tool.py
```

---

## ▶️ Example Input

```
Vertical holes: 48
Horizontal holes: 2
Number of circuits: 14
Dummy holes: 14
Parity: even
Minimum holes per circuit: 2
```

---

## ✅ Example Output

```
Total Holes: 96
Dummy Holes: 14
Usable Holes: 82
Total Circuits: 14

Distribution:
  6 circuits with 6 holes
  8 circuits with 8 holes
```

---

## 🧠 Engineering Value

This tool demonstrates:

- Constraint solving
- Integer feasibility modeling
- Domain-driven engineering automation
- Applied mathematics in mechanical systems
- Software-driven design optimization

---

## 🔮 Future Improvements

- GUI version (Tkinter / PyQt)
- Web deployment (Flask / FastAPI)
- Optimization-based solver
- Integration with CAD workflow
- API version for design automation pipelines

---

## 👨‍💻 Author

Mechanical Engineer transitioning into Robotics & Applied AI  
Building intelligent engineering systems.

---

## 📜 License

Open-source and free for engineering use.