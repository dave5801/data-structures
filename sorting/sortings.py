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


if __name__ == '__main__':
    s = Sortings([10, 5, 4, 8, 12, 1])
    tl = s.insert_sort()
    print(s.sort_list)
