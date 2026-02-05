import numpy as np
import pytest

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

def test_scalarfield1d_size_values_grid():
    #arrange
    grid = Grid1D(0, 1, 100)
    values = np.linspace(0, 10, 98)

    #act
    #scalar = ScalarField1D(grid, values)

    #assert
    with pytest.raises(ValueError):
        scalar = ScalarField1D(grid, values)

def test_scalarfield1d_returngrid():
    #arrange
    grid = Grid1D(0, 1, 100)
    values = np.linspace(0, 10, 100)

    #act
    scalar = ScalarField1D(grid, values)
    actual = scalar.grid

    #assert
    assert grid == actual

def test_scalarfield1d_gridproperty():
    #arrange
    grid = Grid1D(0, 1, 100)
    values = np.linspace(0, 10, 100)
    scalar = ScalarField1D(grid, values)


    #assert
    with pytest.raises(AttributeError):
        scalar.grid = 10

def test_scalarfield1d_reassigngrid():
    #arrange
    grid1 = Grid1D(0, 1, 100)
    grid2 = Grid1D(1, 2, 100)
    values = np.linspace(0, 10, 100)
    scalar = ScalarField1D(grid1, values)

    #act
    scalar.grid = grid2

    #assert
    assert scalar.grid is grid2