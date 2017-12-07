"""Test class for sorting algorithms."""

from random import randint


def test_bubble_test_none_list():
    """Test none list."""
    from sortings import Sortings
    s = Sortings()
    s.bubble_sort()
    assert s.sort_list == []


def test_empty_list():
    """Bubble sort on empty list."""
    from sortings import Sortings
    s = Sortings([])
    s.bubble_sort()
    assert s.sort_list == []


def test_list_one_element_bubble_sort():
    """Bubble sort on one element."""
    from sortings import Sortings
    s = Sortings([1])
    s.bubble_sort()
    assert s.sort_list == [1]


def test_simple_list_bubble_sort():
    """Bubble sort on basic list."""
    from sortings import Sortings
    s = Sortings([5, 4, 3, 2, 1])
    s.bubble_sort()
    assert s.sort_list == [1, 2, 3, 4, 5]


def test_sort_random_list():
    """Test random list of integers."""
    from sortings import Sortings
    x = [randint(0,9) for p in range(0, 9)]
    s = Sortings(x)
    s.bubble_sort()
    x.sort()
    assert s.sort_list == x
