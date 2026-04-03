
def run():
    import os, numpy as np, matplotlib.pyplot as plt
    from scipy.stats import weibull_min, expon, lognorm
    from core.simulation import simulate

    BASE=os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    DATA=os.path.join(BASE,"data"); FIG=os.path.join(BASE,"figures")
    os.makedirs(DATA,exist_ok=True); os.makedirs(FIG,exist_ok=True)

    C=100; lam=95; T=2000; N=12000; X_c=50
    p_star=1-lam/C; p=p_star+0.01

    taus=simulate(C,lam,p,N,T,X_c,42)
    w=weibull_min.fit(taus,floc=0)
    e=expon.fit(taus,floc=0)
    l=lognorm.fit(taus,floc=0)

    np.savetxt(os.path.join(DATA,"weibull.csv"),taus,delimiter=",")

    plt.hist(taus,bins=50,density=True,alpha=0.6)
    x=np.linspace(min(taus),max(taus),200)
    plt.plot(x,weibull_min.pdf(x,*w))
    plt.plot(x,expon.pdf(x,*e))
    plt.plot(x,lognorm.pdf(x,*l))
    plt.savefig(os.path.join(FIG,"figure3_weibull.png"),dpi=300)
    plt.close()
