index = int(input("Введите индекс числа Фибоначчи  "))
a, b = 0, 1
print(f"Последовательность Фибоначчи: {a}", end=" ")
for _ in range(1,index):
    a, b = b, a+b
    print(a, end=" ")
print(f"\nЧисло Фибоначчи под индексом {index} = {a}")