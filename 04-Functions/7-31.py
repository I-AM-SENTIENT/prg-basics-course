def power(x,n):
    if n >1:
        value = x * power(x,n-1)
        return value
    elif n == 1:
        value = x
        return value
    else:
        print('shit is bad')
print(power(2,4))