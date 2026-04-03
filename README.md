
[README.md](https://github.com/user-attachments/files/26455286/README.md)

# Critical Failure Thresholds and Resilience Dynamics in Stochastic Supply Networks

This repository contains the full computational framework used in the manuscript:

**“Critical Failure Thresholds and Resilience Dynamics in Stochastic Supply Networks under Probabilistic Disruptions”**

submitted to *Reliability Engineering & System Safety*.

---

## 📌 Scientific Contribution

This work provides:

- A closed-form stability condition for stochastic supply networks  
- A quantitative early-warning indicator based on critical slowing down  
- A probabilistic characterization of collapse dynamics with heavy-tailed risk  

The results bridge analytical theory and large-scale simulation, providing actionable insights for resilience engineering.

---

## 🔬 Overview

A fully reproducible, simulation-based and analytically grounded framework to study stability and collapse dynamics in stochastic supply networks under probabilistic disruptions.

Includes:

- Closed-form validation of the failure threshold  
- Estimation of critical scaling behavior near instability  
- Statistical characterization of collapse times  
- Robustness analysis across simulation parameters  

---

## 🧠 Key Results (Reproducible)

- **Failure threshold:**  p* = 1 − λ/C  
- **Critical dynamics:**  τ ∼ (p − p*)^(-ν)  
  - Asymptotic exponent: ν ≈ 0.84  
  - Finite-sample estimator: ν_full ≈ 0.90  
- **Collapse time distribution:** Weibull with β ≈ 0.60 (heavy-tailed)  
- **Robustness:** stable across T and N  

---

## ⚙️ Installation

```bash
pip install -r requirements.txt
```

Dependencies:

- numpy==1.24.4  
- scipy==1.10.1  
- matplotlib==3.7.1  
- numba==0.57.1  

---

## ▶️ Reproducing All Results

```bash
python run_all.py
```

Typical runtime:

- CPU: 4–8 cores recommended  
- RAM: ≥ 8 GB  
- Runtime: ~2–4 hours (N = 10,000, T = 2,000)

---

## 📊 Outputs

### Figures (`/figures/`)

| Figure | Manuscript Reference | Description |
|------|---------------------|------------|
| Figure 1 | Section 4 / Table 2 | Empirical vs theoretical threshold validation |
| Figure 2 | Section 5.2 / Table 3 | Log-log scaling (ν_full estimation) |
| Figure 3 | Section 5.3 / Table 4 | Collapse time distribution (Weibull β ≈ 0.60) |
| Figure C1 | Appendix C | Robustness analysis across T and N |

---

### Data (`/data/`)

| File | Description |
|-----|------------|
| threshold.csv | Empirical vs theoretical p* |
| figure2_loglog.csv | Scaling data |
| weibull.csv | Raw collapse times |
| appendix_C_robustness.csv | Robustness results |

---

## 🧪 Experiments

| Script | Purpose |
|-------|--------|
| threshold_validation.py | Threshold validation |
| figure2_loglog.py | Critical exponent estimation |
| weibull_analysis.py | Distribution fitting |
| experiment_appendix_C_robustness.py | Robustness analysis |

---

## 🔁 Reproducibility Guarantees

- Fixed random seed (42) across all experiments  
- Deterministic pipeline (NumPy + Numba)  
- Version-pinned dependencies  
- No external data dependencies  
- Direct mapping: code ↔ figures ↔ manuscript  

---

## ✅ Quick Verification

```bash
python experiments/figure2_loglog.py
```

Expected:

- Output: data/figure2_loglog.csv  
- Slope ≈ 0.8–0.9  

```bash
python experiments/threshold_validation.py
```

Expected:

- Points align near diagonal (p*_emp ≈ p*_theo)

---

## 📄 License

MIT

---

## 📬 Contact

Anonymous submission (double-blind review)
