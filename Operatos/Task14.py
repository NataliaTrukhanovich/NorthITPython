print("Введите четыре числа")
a = int(input())
b = int(input())
c = int(input())
d = int(input())
polozhitelnie = 0
otricatelnie = 0
if (a>0): polozhitelnie += 1
elif (a<0): otricatelnie += 1
if (b>0): polozhitelnie += 1
elif (b<0): otricatelnie += 1
if (c>0):polozhitelnie += 1
elif (c<0): otricatelnie += 1
if (d>0): polozhitelnie += 1
elif (d<0): otricatelnie += 1
print(f"Количество положительных чисел: {polozhitelnie}")
print(f"Количество отрицательных чисел: {otricatelnie}")