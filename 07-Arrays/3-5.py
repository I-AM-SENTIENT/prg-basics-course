list = [15, 8, 31, 47, 2, 19]

def average(array):
    avg = 0
    dl = len(array)
    for x in array:
        avg = avg + x
    avg = avg /dl
    return avg



print(list)
print(average(list))

