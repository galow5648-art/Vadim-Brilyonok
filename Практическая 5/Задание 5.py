BILLS = [5000, 2000, 1000, 500, 200, 100]
money = int(input("Введите сумму для снятия (кратную 100): "))
print("Будет выдано:")
for bill in BILLS:
    count = money // bill
    money = money % bill
    if count > 0:
        print(f"Купюр по {bill} руб.: {count} шт.")
