
categories = ["Food", "Transport", "Rent","Entertainment"]
expenses = [500, 150, 1000, 200]

res = max(expenses)
index = expenses.index(res)


print('Most expensive was:',categories[index])