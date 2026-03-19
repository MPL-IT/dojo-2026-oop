import numpy as np
import pytest

from dojo.field import ScalarField1D, IncompatibleGridError
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


def test_scalarfield1d_return_value():
    #arrange
    grid = Grid1D(0, 1, 100)
    values = np.linspace(0, 10, 100)
    scalar = ScalarField1D(grid, values)

    #act
    actual = scalar.values

    #assert
    assert np.allclose(values, actual)


def test_scalarfield1d_to_string_conversion():
    #arrange
    grid = Grid1D(0, 1, 100)
    values = np.linspace(0, 10, 100)
    scalar = ScalarField1D(grid, values)

    #act
    actual = str(scalar)

    #assert
    expected = f"ScalarField1D(grid = {str(grid)}, minval = {np.min(values)} , maxval = {np.max(values)})"
    assert actual == expected

def test_scalarfield1dequalvalues():
    #arrange
    grid = Grid1D(0, 1, 100)
    values1 = np.linspace(0, 10, 100)
    scalar1 = ScalarField1D(grid, values1)
    scalar2 = ScalarField1D(grid, 3*values1)
    scalar3 = ScalarField1D(grid, values1)

    #assert
    assert (scalar1 == scalar2) is False
    assert (scalar1 == scalar3) is True

def test_scalarfield1dadd():
    #arrange
    grid = Grid1D(0, 1, 100)
    values1 = np.ones(100)
    values2 = np.ones(100)*2
    scalar1 = ScalarField1D(grid, values1)
    scalar2 = ScalarField1D(grid, values2)

    #assert
    assert scalar1 + scalar1 == scalar2

def test_Exceptions():
    #arrange
    grid = Grid1D(0,1,100)
    grid2 = Grid1D(0,1,99)
    values1 = np.ones(100)
    values2 = np.ones(99)
    scalar1 = ScalarField1D(grid, values1)
    scalar2 = ScalarField1D(grid2, values2)

    #assert
    with pytest.raises(IncompatibleGridError):
        scalar1 + scalar2