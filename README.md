[README.md](https://github.com/user-attachments/files/26455212/README.md)
# Critical Failure Thresholds and Resilience Dynamics in Stochastic Supply Networks

This repository contains the full computational framework used in the manuscript:

“Critical Failure Thresholds and Resilience Dynamics in Stochastic Supply Networks under Probabilistic Disruptions”

submitted to *Reliability Engineering & System Safety*.

---

## 🔬 Overview

This work develops a fully reproducible, simulation-based and analytically grounded framework for studying stability and collapse dynamics in stochastic supply networks under probabilistic disruptions.

The repository provides:

- Closed-form validation of the failure threshold  
- Estimation of critical scaling behavior near instability  
- Statistical characterization of collapse times  
- Robustness analysis across simulation parameters  

---

## 🧠 Key Results (Reproducible)

- Failure threshold: p* = 1 − λ/C  
- Critical dynamics: τ ∼ (p − p*)^(-ν)  
  - ν ≈ 0.84  
  - ν_full ≈ 0.90  
- Collapse time distribution: Weibull β ≈ 0.60  
- Robust across T and N  

---

## ⚙️ Installation

pip install -r requirements.txt

Dependencies:
- numpy==1.24.4  
- scipy==1.10.1  
- matplotlib==3.7.1  
- numba==0.57.1  

---

## ▶️ Reproducing Results

python run_all.py

---

## 📊 Outputs

Figures:
- Figure 1: Threshold validation  
- Figure 2: Scaling behavior  
- Figure 3: Weibull distribution  
- Figure C1: Robustness  

Data:
- threshold.csv  
- figure2_loglog.csv  
- weibull.csv  
- appendix_C_robustness.csv  

---

## 🔁 Reproducibility

- Seed fixed (42)  
- Deterministic pipeline  
- Fully mapped to manuscript  

---

## 📄 License

MIT

---

## 📬 Contact

Anonymous submission
