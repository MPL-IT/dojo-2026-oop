import numpy as np

from dojo.field import ScalarField1D
from dojo.grid import Grid1D


def test_scalarfield1d_initialisation():
    # arrange
    grid = Grid1D(0, 1, 100)
    values = np.sin(grid.coords)

    # act
    scalar = ScalarField1D(grid, values)

    # assert
    assert scalar is not None
