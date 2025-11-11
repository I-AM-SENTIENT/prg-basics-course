def bubblesort(array):
    dl = len(array)
    for i in range(dl):
        for j in range(0, dl-i-1):
            if array[j] > array[j+1]:
                array[j], array[j+1] = array[j+1], array[j]
    return array


list = [64, 34, 25, 12, 22, 11, 90]
print(bubblesort(list))