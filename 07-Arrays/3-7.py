list = ['Genowefa', 'Onufry', 'Celestyna', 'Alojzy', 'Pankracy']


def longest_name(array):
    longest_index = None
    longest_word = 0
    for x in array:
        if len(x) > longest_word:
            longest_word = len(x)
            longest_index = x
    return longest_index


print(longest_name(list))