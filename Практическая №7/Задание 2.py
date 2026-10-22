import random
status = input("Введите статус заказа (pending, processing, shipped, delivered, cancelled): ")
print()
print("╔════════════════════════════════╗")
print("║   СТАТУС ВАШЕГО ЗАКАЗА       ║")
print("╚════════════════════════════════╝")
print()
match status:
    case "pending":
        print("Статус: В ожидании ⏳")
        print("Описание: Ваш заказ принят и ожидает обработки")
        print("Примерное время:", random.randint(1, 24), "ч")
    case "processing":
        print("Статус: В обработке ⚙️")
        print("Описание: Ваш заказ собирается на складе")
        print("Примерное время:", random.randint(1, 3), "дн")
    case "shipped":
        print("Статус: Отправлено 🚚")
        print("Описание: Ваш заказ находится в пути к вам")
        print("Примерное время:", random.randint(2, 5), "дн")
    case "delivered":
        print("Статус: Доставлено ✅")
        print("Описание: Ваш заказ доставлен, спасибо за покупку")
        print("Примерное время: 0 дн")
    case "cancelled":
        print("Статус: Отменено ❌")
        print("Описание: Ваш заказ был отменён")
        print("Возврат средств:", random.randint(1, 5), "дн")
    case _:
        print("❌ Ошибка: Неизвестный статус", status)
        print("Доступные статусы: pending, processing, shipped, delivered, cancelled")
