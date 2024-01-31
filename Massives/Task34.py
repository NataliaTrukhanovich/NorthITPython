array = [56, 8, -8, 0, 34, 6, 10, -5, 18, 20]
max = array[0]
for i in range(0, len(array)-1):
    if max<array[i+1]:
        max=array[i+1]
print(f"Наибольший элемент массива = {max}")