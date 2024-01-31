import random
array = [[random.randint(1, 10) for _ in range(5)] for _ in range(5)]
for row in array:
    for j in row:
        print(j,end=" ")
    print()
currentSum = 0
maxSum = 0
for j in range(5):
    for i in range(5):
        currentSum += array[i][j]
    if currentSum > maxSum: maxSum = currentSum
    currentSum = 0
print(f"Наибольшая сумма элементов столбца: {maxSum}")