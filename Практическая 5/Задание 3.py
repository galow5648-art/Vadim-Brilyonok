USD_TO_RUB = 95.50
def convert_usd_to_rub(amount_usd):
    """Переводит доллары в рубли."""
    return amount_usd * USD_TO_RUB
usd = float(input("Введите сумму в долларах: "))
rub = convert_usd_to_rub(usd)
print(f"{usd:.2f} USD = {rub:.2f} руб.")
