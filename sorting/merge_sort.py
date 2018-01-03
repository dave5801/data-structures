"""Merge Sort implementation."""


def merge_sort(lst):
    """Merge Sort."""
    if len(lst) <= 1:
        return lst

    mid = len(lst) // 2
    left = lst[mid:]
    right = lst[:mid]

    left = merge_sort(left)
    right = merge_sort(right)

    output = []

    while left and right:
        if right[0] < left[0]:
            output.append(right.pop(0))
        elif left[0] < right[0]:
            output.append(left.pop(0))

    return output + left + right

if __name__ == '__main__':

    import timeit
    setup = 'from merge_sort import merge_sort'

    #a longer reverse ordered list seems to be the better time, largely because of how the insertions work
    print("Awesome-ist time", min(timeit.Timer('merge_sort([10, 5, 7, 8, 12])', setup=setup).repeat(7, 1000))) 
    print("I guess pretty good time", min(timeit.Timer('merge_sort([10, 9, 8, 7, 6, 5, 4, 3, 2, 1])', setup=setup).repeat(7, 1000))) 
    print("Appears bad timing", min(timeit.Timer('merge_sort([1,2,3,4,5])', setup=setup).repeat(7, 1000))) 
    