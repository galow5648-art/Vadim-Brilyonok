
data = input("Введите вес (кг) и рост (м) через пробел: ")
weight, height = map(float, data.split())
bmi = weight / (height * height)
print(f"Ваш ИМТ: {bmi:.1f}")
