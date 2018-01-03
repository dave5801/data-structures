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

    #a longer reverse ordered list seems to be the better time, largely because of how the insertions work
    print("Betterer time", min(timeit.Timer('insert_sort([10, 9, 8, 7, 6, 5, 4, 3, 2, 1])', setup=setup).repeat(7, 1000))) 
    print("Not so bad", min(timeit.Timer('insert_sort([1,2,3,4,5])', setup=setup).repeat(7, 1000))) 
    print("Worser time", min(timeit.Timer('insert_sort([10, 5, 7, 8, 12])', setup=setup).repeat(7, 1000))) 
