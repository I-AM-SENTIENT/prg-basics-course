matrix = [
   [0,0,0],
   [0,0,0],
   [0,0,0]
]


for x in range(3):
    for y in range(3):
        if x == y:
            matrix[x][y] = 1


for x in matrix:
    print(x)