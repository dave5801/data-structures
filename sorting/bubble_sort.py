"""Bubble sort implementation."""


def bubble_sort(lst=[]):
    """Bubble sort."""
    for i in range(len(lst) - 1):
        for j in range(len(lst) -1):
            if lst[j] > lst[j+1]:
                temp = lst[j]
                lst[j]= lst[j+1]
                lst[j + 1] = temp
    return lst


if __name__ == '__main__':

    import timeit
    setup = 'from bubble_sort import bubble_sort'

    print(min(timeit.Timer('bubble_sort([10, 5, 7, 8, 12])', setup=setup).repeat(7, 1000))) 
