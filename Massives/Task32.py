array = [56, 8, -8, 0, 34, 6, 100, -5, 18]
sum = 0
for i in range(0, len(array), 2):
    sum = sum + array[i]
print(f"Сумма элементов с чётными индексами = {sum}")