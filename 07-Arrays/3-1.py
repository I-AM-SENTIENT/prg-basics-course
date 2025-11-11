array = [34,7,19,4,21,8]


index = 0
even = 0
dl = len(array)
while index < dl:
    if array[index] % 2 == 0:
        even+=1
        index+=1
    else:
        index+=1


print(even)