"""Test class for sorting algorithms."""

from random import randint


def test_sortings_test_none_list():
    """Test none list."""
    from bubble_sort import bubble_sort
    s = bubble_sort()
    assert s == []


def test_bubble_sort_empty_list():
    """Test Bubble sort on empty list."""
    from bubble_sort import bubble_sort
    s = bubble_sort([])
    assert s == []


def test_list_one_element_bubble_sort():
    """Test Bubble sort on one element."""
    from bubble_sort import bubble_sort
    s = bubble_sort([1])
    assert s == [1]


def test_simple_list_bubble_sort():
    """Test Bubble sort on basic list."""
    from bubble_sort import bubble_sort
    s = bubble_sort([5, 4, 3, 2, 1])
    assert s == [1, 2, 3, 4, 5]


def test_sort_random_list():
    """Test random list of integers."""
    from bubble_sort import bubble_sort
    x = [randint(0, 9) for p in range(0, 9)]
    s = bubble_sort(x)
    x.sort()
    assert s == x


def test_insert_sort_empty_list():
    """Test Insert sort on empty list."""
    from insert_sort import insert_sort
    s = insert_sort()
    assert s == []


def test_list_one_element_insert_sort():
    """Test insert sort on one element."""
    from insert_sort import insert_sort
    s = insert_sort([1])
    assert s == [1]


def test_simple_list_insert_sort():
    """Test insert sort on basic list."""
    from insert_sort import insert_sort
    s = insert_sort([5, 4, 3, 2, 1])
    assert s == [1, 2, 3, 4, 5]


def test_insert_sort_random_list():
    """Test insert sort on random list of integers."""
    from insert_sort import insert_sort
    x = [randint(0, 9) for p in range(0, 9)]
    s = insert_sort(x)
    x.sort()
    assert s == x


def test_merge_sort_empty_list():
    """Test merge sort on empty list."""
    from merge_sort import merge_sort
    s = merge_sort([])
    assert s == []


def test_list_one_element_merge_sort():
    """Test merge sort on one element."""
    from merge_sort import merge_sort
    s = merge_sort([1])
    assert s == [1]


def test_merge_sort_simple_list():
    """Test Merge sort on basic list."""
    from merge_sort import merge_sort
    x = [10, 5, 7, 2, 12]
    s = merge_sort(x)
    x.sort()
    assert s == x


def test_merge_sort_rand_list():
    """Test merge sort on random list."""
    from merge_sort import merge_sort
    import random
    x = random.sample(range(100), 10)
    k = merge_sort(x)
    x.sort()
    assert k == x


'''




def test_quick_sort_empty_list():
    """Quick sort on empty list."""
    from sortings import Sortings
    s = Sortings()
    x = s.quick_sort([])
    assert x == []


def test_quick_sort_list_len_one():
    """Quick sort on one element list."""
    from sortings import Sortings
    s = Sortings()
    x = s.quick_sort([1])
    assert len(x) == 1


def test_quick_sort_simple_list():
    """Quick sort on basic list."""
    from sortings import Sortings
    s = Sortings()
    x = [10, 5, 7, 2, 12]
    k = s.quick_sort(x)
    x.sort()
    assert k == x


def test_quick_sort_rand_list():
    """test quick sort on random list."""
    from sortings import Sortings
    import random
    s = Sortings()
    x = random.sample(range(100), 10)
    k = s.quick_sort(x)
    x.sort()
    assert k == x



'''