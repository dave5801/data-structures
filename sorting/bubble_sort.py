"""Bubble sort implementation."""


def bubble_sort(lst=[]):
    """Bubble sort."""
    for i in range(len(lst) - 1):
        for j in range(len(lst) - 1):
            if lst[j] > lst[j + 1]:
                lst[j], lst[j + 1] = lst[j + 1], lst[j]
    return lst


if __name__ == '__main__':
    import timeit
    setup = 'from bubble_sort import bubble_sort'

    print("Better time", min(timeit.Timer('bubble_sort([1,2,3,4,5])', setup=setup).repeat(7, 1000))) 
    print("Worser time", min(timeit.Timer('bubble_sort([10, 5, 7, 8, 12])', setup=setup).repeat(7, 1000))) 
    print("Not so bad time", min(timeit.Timer('bubble_sort([10, 9, 8, 7, 6, 5, 4, 3, 2, 1])', setup=setup).repeat(7, 1000))) 
