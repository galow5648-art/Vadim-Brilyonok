temperature = float(input())
pressure = int(input())
pulse = int(input())
if not (35 <= temperature <= 38 and 105 <= pressure <= 140 and 55 <= pulse <= 110):
    print("Требуется врач")
elif 36 <= temperature <= 37 and 110 <= pressure <= 130 and 60 <= pulse <= 100:
    print("Нормальное состояние")
else:
    print("Легкое недомогание")
