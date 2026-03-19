import numpy as np

class ScalarField1D:
    """captures the notion of a scalar field
      on a one-dimensional domain (i.e. grid)"""

    def __init__(self, grid, values):
        self._grid = grid
        self._values = values
        self._validate_attributes()

    def _validate_attributes(self):
        if self._grid.size != self._values.size:
            raise ValueError("values must have same size as grid")

    @property
    def grid(self):
        return self._grid

    @grid.setter
    def grid(self, newgrid):
        self._grid = newgrid
        self._validate_attributes()

    @property
    def values(self):
        return self._values

    def __str__(self):
        return f"ScalarField1D(grid = {self.grid}, minval = {np.min(self.values)} , maxval = {np.max(self._values)})"

    def __eq__(self, other):
        if self._grid.size == other._grid.size:
            return np.allclose(self._values, other._values)
        else:
            return False