###
# Program that simulates the operation of an electronic thermometer.
#
temperature = 30
if temperature > 35:
    print("It is extermely hot")
elif temperature > 30:
    print('Its hot')
elif temperature >= 15:
    print('It is warm')
elif temperature >= 0:
    print('It is cold')
elif temperature <0:
    print('Warning, frost')