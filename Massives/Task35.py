#Для примера массив с уникальными значениями
#array = [30, 42, -9, -2, 20, -1, 102, -3, -80, -8, -11, 90, 103]
array = [30, 42, 80, 30, 0, 1, 80, 30, 42, 30, 80, 1, 42]
currentCount = 0
count = 0
chislo = array[0]
for i in range(0, len(array)-1):
    for j in range(i+1, len(array)):
        if array[i] == array[j]:
            currentCount += 1
    if ((currentCount>0) and (currentCount>count)):
        count=currentCount
        chislo=array[i]
    elif ((currentCount == count) and (array[i]>chislo)):
        chislo=array[i]
    currentCount=0
if count == 0:
    print("Повторяющихся чисел в массиве нет")
else:
    print(f"Наиболее часто встречающееся число {chislo}")