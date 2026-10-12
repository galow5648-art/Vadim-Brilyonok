pocket = int(input())
if not 0 <= pocket <= 36:
    print("ошибка ввода")
elif pocket == 0:
    print("зеленый")
elif (1 <= pocket % 18 <= 10) == (not pocket % 2 == 0):
    print("красный")
else:
    print("черный")
