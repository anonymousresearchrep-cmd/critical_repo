
def run():
    import os, numpy as np, matplotlib.pyplot as plt
    from scipy.stats import weibull_min
    from core.simulation import simulate

    BASE=os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    DATA=os.path.join(BASE,"data"); FIG=os.path.join(BASE,"figures")
    os.makedirs(DATA,exist_ok=True); os.makedirs(FIG,exist_ok=True)

    C=100; lam=95; X_c=50
    p_star=1-lam/C

    T_values=[500,1000,2000,4000]
    N_values=[1000,5000,10000,50000]
    deltas=np.array([0.005,0.01,0.02])

    results=[]

    for T in T_values:
        for N in N_values:
            tau_means=[]
            for dp in deltas:
                taus=simulate(C,lam,p_star+dp,N,T,X_c,42)
                tau_means.append(np.mean(taus))

            coef=np.polyfit(np.log(deltas),np.log(tau_means),1)
            nu=-coef[0]

            taus=simulate(C,lam,p_star+0.01,N,T,X_c,42)
            beta=weibull_min.fit(taus,floc=0)[0]

            results.append([T,N,nu,beta])

    results=np.array(results)
    np.savetxt(os.path.join(DATA,"appendix_C_robustness.csv"),
               results,delimiter=",",header="T,N,nu,beta")

    results_T=results[np.isclose(results[:,1],10000)]
    results_N=results[np.isclose(results[:,0],2000)]

    fig,ax=plt.subplots(2,2,figsize=(10,8))
    ax[0,0].plot(results_T[:,0],results_T[:,2],'o-')
    ax[0,1].plot(results_T[:,0],results_T[:,3],'s-')
    ax[1,0].plot(results_N[:,1],results_N[:,2],'o-')
    ax[1,1].plot(results_N[:,1],results_N[:,3],'s-')

    for a in ax.flat: a.grid()

    plt.tight_layout()
    plt.savefig(os.path.join(FIG,"figure_C1.tiff"),dpi=300)
    plt.close()
