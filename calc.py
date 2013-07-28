import math
import numpy as np


def add_two_numbers(num1=6, num2=3):
    return num1 + num2


def sine_wave(magnitude=2, period=math.pi/2):
    """Returns the x and y values of a sine wave"""
    x = np.arange(0, period, period/100)
    y = magnitude * np.sin(x)
    return x.tolist(), y.tolist()
