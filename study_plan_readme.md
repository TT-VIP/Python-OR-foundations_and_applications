# Python for Operations Research — Study Plan

This repository documents a structured learning roadmap designed for Operations Research practitioners and PhD students aiming to improve their programming capabilities in Python. It covers foundational skills, metaheuristics, and advanced decomposition techniques using Gurobi.

---

## ⚙️ Phase 1 – Programming Foundations (2–3 weeks)

### 🌟 Objectives
- Strengthen object-oriented design
- Master NumPy and pandas
- Learn structured testing and logging

### 🔹 Actions
**Books / Resources:**
- *Effective Python* by Brett Slatkin (OOP best practices)
- pandas documentation (groupby, joins, reshaping)
- numpy documentation (broadcasting, indexing, matrix operations)

**Practice Projects:**
- Reimplement a basic scheduling or knapsack problem using OOP
- Simulate a toy production planning problem using pandas for data I/O

**Focus Topics:**
- Writing modular, reusable classes
- Data input/output using pandas
- Fast computation with numpy
- Unit testing with `pytest`
- Logging and debugging

---

## ⚙️ Phase 2 – Heuristic Algorithms (4–6 weeks)

### 🔬 Focus Algorithms
- Iterated Greedy
- Simulated Annealing
- Tabu Search
- Genetic Algorithms

### 🔹 Actions
For each method:
- Study theory with examples (e.g., scheduling, TSP)
- Implement a base version (e.g., single machine scheduling)
- Refactor using OOP: `Problem`, `Solution`, `Neighborhood`, `Evaluator`
- Test on benchmark instances (e.g., TSPLIB, OR-Library)

### ⏰ Suggested Schedule
| Week | Algorithm           | Problem Type         | Enhancement                             |
|------|---------------------|----------------------|------------------------------------------|
| 1    | Iterated Greedy     | Flow shop scheduling | Apply destruction/reconstruction         |
| 2    | Simulated Annealing | TSP                  | Add cooling schedule & acceptance rule   |
| 3    | Tabu Search         | QAP or scheduling    | Introduce adaptive tabu list             |
| 4–5 | Genetic Algorithm    | VRP                  | Include mutation, crossover, selection   |

---

## 🧮 Phase 3 – Exact Methods (6–8 weeks)

### 🔹 Algorithms
- Column Generation
- Benders Decomposition
- Branch-and-Cut
- Branch-and-Price

These methods will be implemented in Python using Gurobi.

### 🔹 Actions
- Learn Gurobi Python API in detail (modeling, callbacks, lazy constraints)
- Implement classic problems with subproblem/master logic

### ⏰ Suggested Schedule
| Week | Method              | Problem                  | Focus                                  |
|------|---------------------|---------------------------|-----------------------------------------|
| 1–2 | Column Generation    | Cutting stock / Set cover | LP relaxation, subproblem generation    |
| 3–4 | Benders Decomposition| Facility location         | Feasibility and optimality cuts         |
| 5–6 | Branch-and-Cut       | TSP                       | Subtour elimination via callback        |
| 7–8 | Branch-and-Price     | Bin packing / VRP         | Knapsack/shortest path pricing problems |

### 🔧 Tools
- Gurobi with `gurobipy`
- Custom callbacks (esp. lazy constraints)
- Use `dataclasses` and class hierarchies to organize subproblem/master logic

---

## 📘 Additional Learning Tips

### 🎓 Courses
- MIT OR Tools (OCW)
- Coursera: *Discrete Optimization* by Pascal Van Hentenryck
- Gurobi webinars and documentation

### 📚 Reading
- *Metaheuristics* by Gendreau & Potvin
- *Integer Programming* by Laurence Wolsey
- *Network Flows* by Ahuja, Magnanti, Orlin

### 💼 Project Ideas
- Course timetabling
- Multi-stage production planning
- Vehicle routing with time windows

---

## 🛠️ Tooling & Development Workflow
- Use **Jupyter Notebooks** for prototyping
- Use **VSCode or PyCharm** for modular development
- Version control with **git**, use `black` + `flake8` for formatting
- Write unit tests using `pytest`

---

## 📊 Milestones
- ✅ Month 1: Solid in OOP, numpy, pandas
- ✅ Month 2: Implement & benchmark 3 metaheuristics
- ✅ Month 3–4: Implement 3 decomposition/branch-based methods
- 🌟 Final Project: Hybrid method combining heuristics + exact (e.g. matheuristics for scheduling)

---

Happy modeling!

