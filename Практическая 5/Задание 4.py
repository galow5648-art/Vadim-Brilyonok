import math
def calculate_rectangle_area(width, height):
    """Возвращает площадь прямоугольника."""
    return width * height
def calculate_circle_area(radius):
    """Возвращает площадь круга."""
    return math.pi * radius ** 2
width, height = map(float, input("Введите ширину и высоту через пробел: ").split())
print(f"Площадь прямоугольника: {calculate_rectangle_area(width, height):.2f}")
radius = float(input("Введите радиус круга: "))
print(f"Площадь круга: {calculate_circle_area(radius):.2f}")
