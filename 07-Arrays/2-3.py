# Weekly expenses for different categories
# [Food, Transport, Utilities]
monthly_expenses = [
   [200, 50, 100],  # Week 1
   [180, 60, 110],  # Week 2
   [220, 55, 105],  # Week 3
   [210, 65, 95]    # Week 4
]

# Calculates expenses
# Use loop statements
total_food = 0
total_transport = 0
total_utilities = 0
week1 = 0
week2 = 0
week3 = 0
week4 = 0

for i in range(3):
    week1 += monthly_expenses[0][i]
    week2 += monthly_expenses[1][i]
    week3 += monthly_expenses[2][i]
    week4 += monthly_expenses[3][i]


for week in monthly_expenses:
    total_food += week[0]
    total_transport += week[1]
    total_utilities += week[2]


# Print expenses
print('MONTHLY EXPENSES')
print('----------------')
print('Food:', total_food)
print('Transport:',total_transport)
print('Utilities:',total_utilities)
print('Week 1:',week1)
print('Week 2:',week2)
print('Week 3:',week3)
print('Week 4:',week4)
print('---------------')
print('TOTAL:', total_food + total_transport + total_utilities)