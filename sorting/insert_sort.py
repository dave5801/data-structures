"""Insert Sort Implementation."""


def insert_sort(lst):
    """Insert sort."""
    for i in range(len(lst)):

        k = lst[i]
        j = i

        while j > 0 and k < lst[j - 1]:
            lst[j] = lst[j - 1]
            j -= 1

        lst[j] = k

    return lst

if __name__ == '__main__':

    import timeit
    setup = 'from insert_sort import insert_sort'

    print(min(timeit.Timer('insert_sort([10, 5, 7, 8, 12])', setup=setup).repeat(7, 1000))) 