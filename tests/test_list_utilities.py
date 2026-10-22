"""Tests for the list utility functions."""

from utilities.list_utilities import list_flattener, EmbeddedList

def test_list_flattener_simple_list() -> None:
    """Ensure when a int list is passed a list with same values is returned."""

    data: EmbeddedList = [1,2,3,4,5]
    expected: list[int] = [1,2,3,4,5]

    result = list_flattener(data)

    assert result == expected

def test_list_flattener_empty_list() -> None:
    """Ensure when a empty list is passed in a empty list is returned"""
    data: EmbeddedList = []
    expected: list[int] = []

    result = list_flattener(data)
    assert result == expected

def test_list_flattener_empty_sublist() -> None:
    """Ensure when input only contains empty sublist should return an empty list"""
    data: EmbeddedList = [[]]
    expected: list[int] = []

    result = list_flattener(data)
    assert result == expected

def test_list_flattener_with_sublist() -> None:
    """Ensure when input with only sublist with values should return a list with values of sublist."""
    data: EmbeddedList = [[1,2,3,4,5]]
    expected: list[int] = [1,2,3,4,5]

    result = list_flattener(data)
    assert result == expected

def test_list_flattener_values_and_sublist() -> None:
    """Ensure when input has values and sublist with values should return list with all values."""
    data: EmbeddedList = [1,2,[3,4],5]
    expected: list[int] = [1,2,3,4,5]

    result = list_flattener(data)
    assert result == expected

def test_list_flattener_values_and_multiple_sublist() -> None:
    """Ensure when input has values and sublists with values should return list with all values."""
    data: EmbeddedList = [1,2,[3,4],[5,6],7]
    expected: list[int] = [1,2,3,4,5,6,7]

    result = list_flattener(data)
    assert result == expected

def test_list_flattener_values_and_multple_layers_of_sublist() -> None:
    """Ensure when input has values and multiple layers of sublists with values should return list with all values."""
    data: EmbeddedList = [1,[],[2, [],[3,[4,[5,[6,[7]]]]]]]
    expected: list[int] = [1,2,3,4,5,6,7]

    result = list_flattener(data)
    assert result == expected
