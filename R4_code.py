# -*- coding: utf-8 -*-
"""
Created on Tue Sep 22 20:42:06 2026

@author: james
"""

import numpy as np
import matplotlib.pyplot as plt
from scipy import integrate
from R4_function import *


def phase_space(result):
    """Plot velocity against position (phase portrait)."""
    x = result[0]
    v = result[1]
    plt.subplot(1, 2, 2)
    plt.plot(x, v, 'k')       # x on x-axis, v on y-axis
    plt.axis('equal')
    plt.xlabel("Position (m)")
    plt.ylabel("Velocity (m/s)")


def main():
    x0 = 0
    v0 = 1
    y0 = (x0, v0)
    t0 = 0
    tf = 39 * np.pi
    n = 1001
    t = np.linspace(t0, tf, n)

    result = integrate.solve_ivp(fun=damped_pendulum,
                                 t_span=(t0, tf),
                                 y0=y0,
                                 method="RK45",
                                 t_eval=t)

    x, v = result.y
    t = result.t

    plt.figure(figsize=(10, 4))

    # left panel — time series
    plt.subplot(1, 2, 1)
    plt.plot(t, x, label=r"$x(t)$")
    plt.plot(t, v, label=r"$v(t)$")
    plt.xlabel("Time (s)")
    plt.ylabel("Position (m)")
    plt.legend()               # attached to the LEFT panel

    # right panel — phase portrait
    phase_space(result.y)

    plt.tight_layout()
    plt.show()


if __name__ == '__main__':
    main()