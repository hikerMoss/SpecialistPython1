# По данному числу n закончите фразу «На лугу пасется...» одним из возможных продолжений:
# «n коров», «n корова», «n коровы», правильно склоняя слово «корова».
# Формат входных данных
# Дано целое положительное число n
# Формат выходных данных
# Программа должна вывести введенное число n и одно из слов (на латинице):
# коров, корова или коровы
# Например, 1 корова, 2 коровы, 5 коров, 125 коров.

# TODO: your code here

n = int(input("На лугу пасутся? Укажите число"))

var1 = ("ОШИБКА! УКАЖИТЕ ЧИСЛО БОЛЬШЕ 0!")
var2 = ("корова")
var3 = ("коровы")
var4 = ("коров")

if n < 1:
    print(var1)

elif n >= 11 and n <= 14:
    print(n, var4)

elif n == 1 or n % 10 == 1:
    print(n, var2)

elif n >= 2 and n <= 4 or n % 10 >= 2 and n % 10 <= 4:
    print(n, var3)

else:
    print(n, var4)
