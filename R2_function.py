# code courtesy of Adam Dempsey
# modified for PHY1055 by Oisín Creaner

# This file isn't a complete template, but rather gives an outline of what you need the function to do.
# If you're feeling ambitious, you can keep these functions in a separate file and import them.
# Look up how to do so for yourself, or experiment based on what you see in library imports
import numpy as np

def differential_rl(t, i, v, r, l):
    """
    Calculates the change in current over time from the formula
    L(dI/dt) = V - RI
    :param v: Float for voltage
    :param r:
    :param l:
    :param i:
    :return:
    """
    didt = (v-(r*i))/l
    # complete the docstring
    # do some maths to calculate the difference
    # return the difference
    return didt # this is a placeholder. Replace it with a return value


def exact_solution_rl(v, r, l, t):
    """
    Calculates the change in current over time from the formula
    """
    I = (v/r)*(1-np.exp(-r*t/l))
    return I
    
    # complete the docstring
    # do some maths to calculate the exact solution at a given time
    # return the difference

