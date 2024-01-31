x = int(input("Введите любое число: "))
i = 0
if x>= 0:
    while i<=x:
        if i%2 == 0:
            print(i, end=" ")
        i += 1
else: print("Число должно быть положительное")