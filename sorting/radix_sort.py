import operator

def radix_sort(lst):

    limit = len(str(max(lst)))

    buckets = [[] for i in range(len(lst))]
    unsorted = {}
    sorted_nums = []

    for i in range(len(buckets)):
        tmp = get_digit(lst[i], 1)
        buckets[i].append(tmp)
        unsorted[lst[i]] = buckets[i]

    unsorted = sort_values(unsorted)

    for j in unsorted:
        sorted_nums.append(j[0])
    
    print(sorted_nums)




def sort_values(unsorted):
    return sorted(unsorted.items(), key=operator.itemgetter(1))

def get_digit(number, n):
    return number // 10**n % 10


if __name__ == '__main__':
    lst = [25, 10, 7]
    radix_sort(lst)