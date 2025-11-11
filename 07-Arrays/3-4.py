def maximum(array):
    dl = len(array)
    index = 0
    max = 0
    while index < dl:
        if array[index]>max:
            max = array[index]
            index+=1
        else:
            index+=1
    return max

def minimum(array):
    dl = len(array)
    index = 0
    min = 0
    while index < dl:
        if array[index]<min:
            min = array[index]
            index+=1
        else:
            index+=1
    return min


list = [-15, 8, -31, 47, -2, 19]


print(maximum(list))
print(minimum(list))