
def run():
    import os, numpy as np, matplotlib.pyplot as plt
    from core.simulation import simulate

    BASE=os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    DATA=os.path.join(BASE,"data"); FIG=os.path.join(BASE,"figures")
    os.makedirs(DATA,exist_ok=True); os.makedirs(FIG,exist_ok=True)

    C=100; lam=80; T=2000; N=10000; X_c=50
    ps=np.linspace(0.05,0.4,15)
    tau_means=[]

    for p in ps:
        taus=simulate(C,lam,p,N,T,X_c,42)
        tau_means.append(np.mean(taus))

    tau_means=np.array(tau_means)
    np.savetxt(os.path.join(DATA,"threshold.csv"),
               np.column_stack((ps,tau_means)),delimiter=",")

    plt.figure()
    plt.plot(ps,tau_means,'o-')
    plt.xlabel("p"); plt.ylabel("Mean collapse time")
    plt.savefig(os.path.join(FIG,"figure1_threshold.png"),dpi=300)
    plt.close()
