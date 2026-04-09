import abc
from numbers import Integral
import numpy as np


class Grid(abc.ABC):

    def __init__(self, start, end, num_points):
        if hasattr(start, '__len__'):
            self.dimension = len(start)
        else:
            self.dimension = 1
            start = start,
            end = end,
            num_points = [num_points]

        axes = []
        for i in range(self.dimension):
            if num_points[i] < 2:
                raise ValueError("Number of points must be at least 2")
            if start[i] >= end[i]:
                raise ValueError("Start value must be less than end value")
            if not isinstance(num_points[i], Integral):
                raise TypeError("Number of points must be an integer")
            axis = np.linspace(start[i], end[i], num_points[i])
            axes.append(axis)

        self.coords = np.meshgrid(*axes)
        self.start = start
        self.end = end

    def __str__(self):
        class_name = type(self).__name__
        return f"{class_name}(start={self.start}, end={self.end}, size={self.size})"

    @property  # decorator func/class annotieren
    def size(self):
        my_size = 1
        for i in range(self.dimension):
            my_size *= self.coords[0].shape[i]
        return my_size

    @property
    def spacing(self):
        my_spacing = []
        for i in range(self.dimension):
            my_spacing.append(self.coords[i][1] - self.coords[i][0])
        return my_spacing

    def __eq__(self, other):
        all_close = True
        i = 0
        while all_close and i < self.dimension:
            if self.coords[i].shape == other.coords[i].shape:
                all_close = np.allclose(self.coords[i], other.coords[i])
            else:
                return False
            i += 1
        return all_close


class Grid1D(Grid):
    pass  # simplest class no properties
    # constructor : __init__.py (methode zum initialisieren einer funktion)"""


class Grid2D(Grid):
    pass  # simplest class no properties
    # constructor : __init__.py (methode zum initialisieren einer funktion)"""
