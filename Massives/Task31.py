array = [56, 8, -8, 0, 34, 6, 100, -5]
polozhitelnie=0
otricatelnie=0
for i in array:
    if i>0:
        polozhitelnie +=1
    elif i<0:
        otricatelnie +=1
print(f"Положительных чисел в массиве {polozhitelnie}")
print(f"Отрицательных чисел в массиве {otricatelnie}")