from numbers import Integral
import numpy as np


class Grid1D:
    # pass # simplest class no properties
    # constructor : __init__.py (methode zum initialisieren einer funktion)
    def __init__(self, start, end, num_points=100): #erstes argument innerhalb von class ist immer self
        if num_points < 2:
            raise ValueError("Number of points must be at least 2")
        if start >= end:
            raise ValueError("Start value must be less than end value")
        if not isinstance(num_points, Integral):
            raise TypeError("Number of points must be an integer")
        self.coords = np.linspace(start, end, num_points)
        # self.start = start
        # self.end = end
        # self.size = num_points

    def __str__(self):
        return f"Grid1D(start={self.coords[0]}, end={self.coords[-1]}, size={self.size})"

    @property # decorator func/class annotieren
    def size(self):
        return len(self.coords)

    def __eq__(self, other):
        if self.coords.shape == other.coords.shape:
            return np.allclose(self.coords,other.coords)
        else:
            return False
