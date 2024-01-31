print("Меню")
menu = {"хлеб": 100.08, "молоко": 123.90, "вода": 81.15}
print(menu)
print("____________________________")
tovar = input("Введите название товара, который хотите купить:  ").lower()
if tovar in menu: 
    money = float(input("Введите сумму денег  "))
    if money == menu.get(tovar): 
        print("Спасибо за покупку!")
    elif money < menu.get(tovar): 
        print("Денег не хватает!")
    else: 
        sdacha = money - menu.get(tovar)
        print(f"Ваша сдача: {sdacha:.2f} руб.")
else:
    print("Данного товара в магазине нет")