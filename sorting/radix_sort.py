import operator

def radix_sort(lst):

    limit = len(str(max(lst)))

    buckets = [[] for i in range(len(lst))]
    unsorted = {}

    for i in range(len(buckets)):
        tmp = get_digit(lst[i], 1)
        buckets[i].append(tmp)
        #print(tmp, lst[i])
        unsorted[lst[i]] = buckets[i]

    print(unsorted)




def sort_values(d):
    return sorted(d.items(), key=operator.itemgetter(1))

def get_digit(number, n):
    return number // 10**n % 10


if __name__ == '__main__':
    lst = [25, 10, 7]
    radix_sort(lst)