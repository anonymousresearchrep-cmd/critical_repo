
from experiments.threshold_validation import run as f1
from experiments.figure2_loglog import run as f2
from experiments.weibull_analysis import run as f3
from experiments.experiment_appendix_C_robustness import run as fC

print("Running full pipeline...")
f1()
f2()
f3()
fC()
print("Done.")
