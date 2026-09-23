# code courtesy of Adam Dempsey
# modified for PHY1055 by Oisín Creaner

import numpy as np


def damped_pendulum(t, y, b = 0.1, w0 = 1):
    x, v = y
    dxdt = v
    dvdt = -b*v-(w0**2)*x
    dydt = np.array([dxdt, dvdt])
    return dydt
