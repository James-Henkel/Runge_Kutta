# -*- coding: utf-8 -*-
"""
Created on Tue Sep 22 15:58:22 2026

@author: james
"""
import numpy as np
import matplotlib.pyplot as plt
from scipy import integrate
from R2_function import *

def main():
    y0 = np.array([0])
    t0 = 0
    tf = 20
    n = 200
    t = np.linspace(t0,tf,n)
    
    for (v,r,l) in [(10,50,100), (20,70,115)]:
        result = integrate.solve_ivp(fun=differential_rl,
                                     t_span=(t0, tf),  # Initial and final times
                                     y0=y0, # Initial state
                                     method="RK45",  # Integration method
                                     t_eval=t,
                                     args=(v,r,l))
        I_exact = exact_solution_rl(v, r, l, t)

        plt.plot(result.t, result.y[0], '.', label=f"V={v}, R={r}, L={l}")
        plt.plot(result.t, I_exact, '.', label=f"Exact Solution")
    
    
    plt.xlabel("Time (s)")
    plt.ylabel("Values")
    plt.legend()
    plt.show()


if __name__ == '__main__':
    main()
