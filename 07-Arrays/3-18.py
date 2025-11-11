def second_largest(array):
    sorted_array = bubblesort(array)
    return sorted_array[-2]


def diff_max_min(array):
    sorted_array = bubblesort(array)
    return sorted_array[-1] - sorted_array[0]


def median(array):
    length = get_length(array)
    sorted_array = bubblesort(array)
    if length % 2 != 0:
        return sorted_array[length//2]
    else:
        sum = sorted_array[length//2] + sorted_array[length//2 + 1]
        sum_div = sum / 2
        return sum_div
    

def get_length(array):
    length = 0
    for x in array:
        length +=1
    return length


def max_and_maxminus1(array):
    sorted_array = bubblesort(array)
    new_array = [sorted_array[0],sorted_array[get_length(sorted_array)-1]]
    return new_array

def convert_to_string(array):
    string =''
    for x in array:
        string += str(x)+'-'
    return string[:-1]



def bubblesort(array):
    copy_array = array.copy()
    dl = len(copy_array)
    for i in range(dl):
        for j in range(0, dl-i-1):
            if copy_array[j] > copy_array[j+1]:
                copy_array[j], copy_array[j+1] = copy_array[j+1], copy_array[j]
    return copy_array


list1 = [7,3,8,5,2]

print(second_largest(list1))
print(median(list1))
print(diff_max_min(list1))
print(max_and_maxminus1(list1))
print(convert_to_string(list1))


