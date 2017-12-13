"""Class for sorting algorithms."""


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

        if len(arr) ==1:
            return arr

        mid = len(arr)//2
        left = arr[mid:]
        right = arr[:mid]

        left = merge_sort(left)
        right = merge_sort(right)

        output = []

        while left and right:
            if right[0] < left[0]:
                output.append(right[0])
                right.pop()
            elif left[0] < right[0]:
                output.append(left[0])
                left.pop()

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


if __name__ == '__main__':
    s = Sortings([])
    arr = [10,7,2,6,12]
    t = s.quick_sort(arr)
    print(t)
    #tl = s.insert_sort()
    #print(s.sort_list)
