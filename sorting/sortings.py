"""Class for sorting algorithms."""




'''
class Sortings(object):
    """A general class for sorting algorithms."""

    def __init__(self, sort_list=None):
        """Take in empty list."""
        if sort_list is None:
            self.sort_list = []
        else:
            self.sort_list = sort_list

    def bubble_sort(self):
        """Bubble sort."""
        for i in range(len(self.sort_list) - 1):
            for j in range(len(self.sort_list) - 1):
                if self.sort_list[j] > self.sort_list[j + 1]:
                    temp = self.sort_list[j]
                    self.sort_list[j] = self.sort_list[j + 1]
                    self.sort_list[j + 1] = temp

    def insert_sort(self):
        """Insertion sort."""
        for i in range(len(self.sort_list)):

            k = self.sort_list[i]

            j = i

            while j > 0 and k < self.sort_list[j-1]:
                self.sort_list[j] = self.sort_list[j-1]
                j -= 1

            self.sort_list[j] = k

    def merge_sort(self, arr):
        """Merge Sort."""

        if len(arr) <=1:
            return arr

        mid = len(arr)//2
        left = arr[mid:]
        right = arr[:mid]

        left = self.merge_sort(left)
        right = self.merge_sort(right)

        output = []

        while left and right:
            if right[0] < left[0]:
                output.append(right[0])
                right.pop(0)
            elif left[0] < right[0]:
                output.append(left[0])
                left.pop(0)

        return output + left + right



    def quick_sort(self, arr):
        """Quick sort."""
        if len(arr) <= 1:
            return arr

        pivot = arr[0]
        left = []
        right = []

        for i in arr[1:]:

            if i < pivot:
                left.append(i)

            elif i > pivot:
                right.append(i)

        left = self.quick_sort(left)
        right = self.quick_sort(right)

        return left + [pivot] + right

    def radix_sort(self, arr):

        x = len(str(max(arr)))
        str_list = ['%0*d' % (x, i) for i in arr]
        print(str_list)
'''


if __name__ == '__main__':
    s = Sortings([])
    arr = [5, 102, 48, 10, 2, 500]
    t = s.radix_sort(arr)
    print(t)
    #tl = s.insert_sort()
    #print(s.sort_list)
