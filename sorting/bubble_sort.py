def bubble_sort(l):
    for i in range(len(l)-1):
        if l[i] > l[i+1]:
            temp = l[i]
            l[i] = l[i+1]
            l[i+1] = temp
            print(l)



if __name__ == '__main__':
    bubble_sort([5,4,3,2,1])