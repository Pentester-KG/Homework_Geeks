my_list = [64, 34, 25, 12, 22, 11, 90]
def selection_sort(arr):
    len_1 = len(arr)
    for i in range(len_1):
        min_index = i
        for j in range(i+1, len_1):
            if arr[j] < arr[min_index]:
                min_index = j
        arr[i], arr[min_index] = arr[min_index], arr[i]
    return arr


print(selection_sort(my_list))



import  random
n = 5000
ResultOK = False
first = 1
last = n - 1
stop = True
pos = 0

def binary_search(target):
    global n, ResultOK, first, last, stop, pos
    while stop :
        if first < last:
            middle = (first + last) // 2
            if target == middle:
                first = middle
                last = first
                ResultOK = True
                pos = middle

            else:
                if target > middle:
                    first = middle + 1
                else:
                    last = middle - 1

        else:
            if ResultOK:
                print('True')
                print(pos)
                stop = False
            else:
                print('False')
                stop = False


target = random.randint(first, n)
print(target)
binary_search(target)
