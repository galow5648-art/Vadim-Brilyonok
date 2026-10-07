
TAX = 0.13
income = float(input("Введите годовой доход: "))
tax = income * TAX
net = income - tax
print("Общая сумма дохода:", round(income, 2), "руб.")
print("Сумма налога:", round(tax, 2), "руб.")
print("Сумма на руки:", round(net, 2), "руб.")
