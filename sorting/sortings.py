
class Sortings(object):
    
    def __init__(self, sort_list=None):
        
        if sort_list == None:
            self.sort_list = []
        else:
            self.sort_list = sort_list


    def bubble_sort(self):
        for i in range(len(self.sort_list)-1):
            for j in range(len(self.sort_list)-1):
                if self.sort_list[j] > self.sort_list[j+1]:
                    temp = self.sort_list[j]
                    self.sort_list[j] = self.sort_list[j+1]
                    self.sort_list[j+1] = temp


if __name__ == '__main__':
    #bubble_sort([5,4,3,2,1])
    s = Sortings([5,4,3,2,1])
    tl = s.bubble_sort()
    print(s.sort_list)
 