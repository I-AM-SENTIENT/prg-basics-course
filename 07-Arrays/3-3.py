def second_power(array):
    dl =len(array)
    index = 0
    while index < dl:
        array[index] = array[index]*array[index]
        index+=1
    return array


list = [8,2,5,1,9]


print(second_power(list))
