
import operator

'''
set buckets to keys of 1-10 - they remain fixed
assign unique numbers to values of these buckes
'''

def radix_sort(lst):

    limit = len(str(max(lst)))

    buckets = [[] for i in range(len(lst))]
    unsorted = {}
    sorted_nums = []

    n = 1

    while n < limit:
        for i in range(len(buckets)):
            tmp = get_digit(lst[i], n)
            buckets[i].append(tmp)
            unsorted[lst[i]] = buckets[i]

        unsorted = sort_values(unsorted)

        for j in unsorted:
            sorted_nums.append(j[0])
        
        print(sorted_nums)
        n +=1




def sort_values(unsorted):
    print("unsorted", unsorted)
    sort_vals = sorted(unsorted.items(), key=operator.itemgetter(1))
    print ("sort vals", sort_vals)
    return sorted(unsorted.items(), key=operator.itemgetter(1))

def get_digit(number, n):
    return number // 10**n % 10


if __name__ == '__main__':
    lst = [25, 10, 7, 30, 3, 6]
    radix_sort(lst)

 '''

    def radix_sort(self, arr):

        x = len(str(max(arr)))
        str_list = ['%0*d' % (x, i) for i in arr]
        print(str_list)


        to be continued...

        '''

