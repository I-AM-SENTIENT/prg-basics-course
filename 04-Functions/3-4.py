def sum_digits(number):
    total = 0
    number = abs(number)
    str_number = str(number)

    for x in str_number:
        x = int(x)
        total = total + x
    return total

any_number = int(input('Enter integer number: '))
result = sum_digits(any_number)
print('The sum of the digits in the number',any_number, 'is', result)