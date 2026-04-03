
def run():
    import os, numpy as np, matplotlib.pyplot as plt
    from core.simulation import simulate

    BASE=os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    DATA=os.path.join(BASE,"data"); FIG=os.path.join(BASE,"figures")
    os.makedirs(DATA,exist_ok=True); os.makedirs(FIG,exist_ok=True)

    C=100; lam=95; T=2000; N=10000; X_c=50
    p_star=1-lam/C
    deltas=np.array([0.005,0.01,0.02])
    tau_means=[]

    for dp in deltas:
        taus=simulate(C,lam,p_star+dp,N,T,X_c,42)
        tau_means.append(np.mean(taus))

    tau_means=np.array(tau_means)
    np.savetxt(os.path.join(DATA,"figure2_loglog.csv"),
               np.column_stack((deltas,tau_means)),delimiter=",")

    log_x=np.log(deltas); log_y=np.log(tau_means)
    coef=np.polyfit(log_x,log_y,1)

    plt.figure()
    plt.scatter(log_x,log_y)
    plt.plot(log_x,np.poly1d(coef)(log_x))
    plt.savefig(os.path.join(FIG,"figure2_loglog.tiff"),dpi=300)
    plt.close()
