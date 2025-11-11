list = [2, 6, 4, 9, 7]

def print_stars(array):
    for x in array:
        string = ''
        for i in range(x):
            string = string + '*'
        print(f'{x}:{string}')



print_stars(list)