def quick_sort(lst):
        """Quick sort."""
        if len(lst) <= 1:
            return lst

        pivot = lst[0]
        left = []
        right = []

        for i in lst[1:]:

            if i < pivot:
                left.append(i)

            elif i > pivot:
                right.append(i)

        left = quick_sort(left)
        right = quick_sort(right)

        return left + [pivot] + right


if __name__ == '__main__':

    import timeit
    setup = 'from quicksort import quick_sort'

    print(min(timeit.Timer('quick_sort([10, 5, 7, 8, 12])', setup=setup).repeat(7, 1000))) 