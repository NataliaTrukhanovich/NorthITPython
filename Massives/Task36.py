import random
j=0
array = [[random.randint(1, 100) for _ in range(10)] for _ in range(10)]
for row in array:
    for j in row:
        print(j,end=" ")
    print()
print("Главная диагональ:")
for i in range(10):
    for j in range(10):
        if i==j:
            print(array[i][j], end=" ")