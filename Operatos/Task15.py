print("Введите три числа")
a = int(input())
b = int(input())
c = int(input())
if (a>b): temp = a
else: temp = b
if (temp>c): max = temp
else: max = c
print(f"Самое большое число = {max}")
#Или ещё проще с помощью функции:
#print(max(a,b,c))