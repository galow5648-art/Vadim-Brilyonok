COFFEE = 120
TEA = 80
JUICE = 100
WATER = 50
LEMONADE = 90
print("☕ МЕНЮ КАФЕ ☕")
print("1. Кофе ☕ -", COFFEE, "руб")
print("2. Чай 🍵 -", TEA, "руб")
print("3. Сок 🧃 -", JUICE, "руб")
print("4. Вода 💧 -", WATER, "руб")
print("5. Лимонад 🥤 -", LEMONADE, "руб")
drink = input("Введите номер напитка (1-5) или название: ")
match drink:
    case "1" | "кофе":
        name = "Кофе ☕"
        price = COFFEE
    case "2" | "чай":
        name = "Чай 🍵"
        price = TEA
    case "3" | "сок":
        name = "Сок 🧃"
        price = JUICE
    case "4" | "вода":
        name = "Вода 💧"
        price = WATER
    case "5" | "лимонад":
        name = "Лимонад 🥤"
        price = LEMONADE
    case _:
        name = ""
        print("❌ Ошибка: такого напитка нет в меню")
        exit()

count = input("Введите количество порций: ")
if count.isdigit() and int(count) > 0:
    count = int(count)
    code = input("Введите код скидки (если нет, нажмите Enter): ")


# ---
    if count % 100 >= 11 and count % 100 <= 14:
        word = "порций"
    else:
        match count % 10:
            case 1:
                word = "порция"
            case 2 | 3 | 4:
                word = "порции"
            case _:
                word = "порций"
# ---


    total = price * count
    discount = 0
    match code:
        case "STUDENT":
            discount = total * 20 // 100
        case _:
            discount = 0
    print()
    print("╔═══════════════════════╗")
    print("║     КВИТАНЦИЯ КАФЕ    ║")
    print("╚═══════════════════════╝")
    print()
    print("Товар:", name)
    print("Цена за порцию:", price, "руб")
    print("Количество:", count, word)
    print("Сумма:", total, "руб")


    if discount > 0:
        print()
        print("Скидка STUDENT (20%): -", discount, "руб")
    print("═════════════════════════")
    print("💰 К ОПЛАТЕ:", total - discount, "руб")
    print("═════════════════════════")
else:
    print("❌ Ошибка: количество должно быть целым числом больше 0")
