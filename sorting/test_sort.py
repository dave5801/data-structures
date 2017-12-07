import random


def test_bubble_test_none_list():
    from sortings import Sortings
    s = Sortings()
    s.bubble_sort()
    assert s.sort_list == []

def test_empty_list():
    """Test Create a Tree Node."""
    from sortings import Sortings
    s = Sortings([])
    s.bubble_sort()
    assert s.sort_list == []