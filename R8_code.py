# -*- coding: utf-8 -*-
"""
Created on Wed Sep 23 18:00:43 2026

@author: james
"""
import numpy as np
import matplotlib.pyplot as plt
from scipy import integrate

def driven_pendulum(t, y, b, w0, A, wd):
    x, v = y
    dxdt = v
    dvdt = -b*v-(w0**2)*x-A*np.sin(wd*t)
    dydt = np.array([dxdt, dvdt])
    return dydt

def main():
    #shared constants
    x0 = 0
    t0 = 0
    v0 = 1
    y0 = (x0, v0)
    tf = 39 * np.pi
    n = 1001
    w0 = 2
    A = 1
    t = np.linspace(0.8*tf, tf, n)

    
    #section for amplitude
    for b in [0.05, 0.2, 0.5, 0.75, 1]:
        amplitudes = []
        for wd in np.linspace(0, 3*w0, 100):
            lfun = lambda t, y: driven_pendulum(t, y, b, w0, A, wd)
            result = integrate.solve_ivp(fun=lfun,
                                            t_span=(t0, tf),
                                            y0=y0,
                                            method="RK45",
                                            t_eval=t)
            x, v = result.y
            x_steady = x[len(x)//2:]
            amplitudes.append((x_steady.max() - x_steady.min()) / 2)
        plt.plot(np.linspace(0, 3*w0, 100), amplitudes, '.-', label=f"b={b}")

    plt.xlabel(r"Driving frequency $\omega_d$")
    plt.ylabel("Steady-state amplitude")
    plt.legend()
    plt.tight_layout()
    plt.show()


if __name__ == '__main__':
    main()