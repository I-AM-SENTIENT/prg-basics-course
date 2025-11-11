list = [15, 8, 31, 47, 2, 19]


def average(array):
    avg = 0
    index = 0
    dl = len(array)
    while index < dl:
        avg = avg + array[index]
        index+=1
    avg = avg / dl   
    return avg




print(list)
print(average(list))