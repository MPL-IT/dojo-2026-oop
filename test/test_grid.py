import numpy as np
from dojo.grid import Grid1D, Grid, Grid2D
import pytest


def test_grid1D_initialization():
    # arrange part
    start = 0
    end = 1
    num_points = 100

    # act part
    grid = Grid1D(start, end, num_points)

    # assert part
    assert grid is not None
    assert grid.size == num_points


def test_grid1d_invalid_number_of_points():
    # arrange part
    start = 0
    end = 1
    num_points = 1

    # act part
    with pytest.raises(ValueError):
        grid = Grid1D(start, end, num_points)  # should raise ValueError because of invalid number of points


def test_grid1d_invalid_start_and_end():
    # arrange part
    start = 2
    end = 1
    num_points = 5

    # act part
    with pytest.raises(ValueError):
        grid = Grid1D(start, end, num_points)  # should raise ValueError because of invalid number of points


def test_grid1d_invalid_data_type_num_points():
    # arrange part
    start = 0
    end = 1
    num_points = 5.5

    # act part
    with pytest.raises(TypeError):
        grid = Grid1D(start, end, num_points)


def test_grid1d_representation():  # arrange part
    start = 0.0
    end = 1.0
    num_points = 100

    # act part
    grid = Grid1D(start, end, num_points)
    actual = str(grid)

    # assert part
    expected = f"Grid1D(start={(start,)}, end={(end,)}, size={num_points})"
    assert actual == expected


def test_grid1d_coords_property():
    # arrange part
    start = 0
    end = 1
    num_points = 100

    # act part
    grid = Grid1D(start, end, num_points)
    actual = grid.coords

    # assert part
    expected = (np.linspace(start, end, num_points),)
    assert np.array_equal(actual, expected)


def test_grid1d_correct_coords():
    # arrange part
    grid1 = Grid1D(0, 1, 100)
    grid2 = Grid1D(start=0, end=1, num_points=100)
    grid3 = Grid1D(1, 2, 150)

    # assert part
    assert grid1 == grid2  # == selben attribute
    assert grid1 != grid3
    assert grid1 is not grid2  # is -> selbe object


def test_grid1d_spacing_property():
    # arrange
    start = 0
    end = 1
    number_points = 100

    # act
    grid = Grid1D(start, end, number_points)
    actual = grid.spacing

    # assert
    expected = (end - start) / (number_points - 1)
    assert np.isclose(actual, expected)


def test_grid_cannotbeinstantiated():
    with pytest.raises(Exception):
        grid = Grid()


def test_grid1D_isagrid():
    # arrange
    grid = Grid1D(0, 100, 100)

    # assert
    assert isinstance(grid, Grid)


def test_grid2D_initialization():
    # arrange part
    start = (0, 0)
    end = (1, 1)
    num_points = (100, 100)

    # act part
    grid = Grid2D(start, end, num_points)

    # assert part
    assert grid is not None
    assert grid.size == num_points[0] * num_points[1]


def test_grid2d_coords_property():
    # arrange part
    start = (0, 0)
    end = (1, 2)
    num_points = (2, 3)

    # act part
    grid = Grid2D(start, end, num_points)
    actual = grid.coords

    # assert part
    expected = (np.array([[0., 1.], [0., 1.], [0., 1.]]),
                np.array([[0., 0.], [1., 1.], [2., 2.]]))
    assert np.array_equal(actual, expected)
