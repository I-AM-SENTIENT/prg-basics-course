age = int(input("Age: "))
if age <13:
    group = 'Child'
elif age >=13 and age <=19:
    group = 'Teen'
elif age >19 and age <=64:
    group = 'Adult'
elif age>=65:
    group = 'Senior'


print(group)