
import numpy as np
from numba import njit

@njit
def simulate(C, lam, p, N, T, X_c, seed):
    np.random.seed(seed)
    taus = np.zeros(N)
    for r in range(N):
        I_j = 0.0
        I_k = 0.0
        collapsed = False
        for t in range(1, T+1):
            B = 1 if np.random.rand() > p else 0
            D = np.random.poisson(lam)
            x_ij = C
            x_jk = min(C * B, I_j + x_ij)
            I_j = I_j + x_ij - x_jk
            I_k = I_k + x_jk - D
            if (not collapsed) and (I_k < -X_c):
                taus[r] = t
                collapsed = True
        if not collapsed:
            taus[r] = T + 1
    return taus
