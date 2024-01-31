import random
array = [[random.randint(1, 100) for _ in range(10)] for _ in range(10)]
for row in array:
    for j in row:
        print(j,end=" ")
    print()
print("Побочная диагональ:")
for i in range(10):
    for j in range(10):
        if (j==10-i-1):
            print(array[i][j], end=" ")