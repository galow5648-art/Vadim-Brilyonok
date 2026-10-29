
start = int(input("Введите число A: "))
end = int(input("Введите число B: "))

even_sum = 0
odd_sum = 0


number = start
while number <= end:


    if number % 2 == 0:
        even_sum = even_sum + number
    else:
        odd_sum = odd_sum + number
    number = number + 1


print(even_sum - odd_sum)
