"""Merge Sort implementation."""


def merge_sort(lst):
    """Merge Sort."""
    if len(lst) <= 1:
        return lst

    mid = len(lst)//2
    left = lst[mid:]
    right = lst[:mid]

    left = merge_sort(left)
    right = merge_sort(right)

    output = []

    while left and right:
        if right[0] < left[0]:
            output.append(right[0])
            right.pop(0)
        elif left[0] < right[0]:
            output.append(left[0])
            left.pop(0)

    return output + left + right

if __name__ == '__main__':

    import timeit
    setup = 'from merge_sort import merge_sort'

    print(min(timeit.Timer('merge_sort([10, 5, 7, 8, 12])', setup=setup).repeat(7, 1000))) 