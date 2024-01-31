n = int(input("Введите положительное число  "))
if n==0:
    print("Факториал числа 0 равен 1")
elif n>0:
    factorial=1
    for i in range(1,n+1):
        factorial *= i
    print(f"Факториал числа {n} равен {factorial}")
else: print("Число должно быть положительным")