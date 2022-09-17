# Вычислить число c заданной точностью d
from math import pi

d =  int(input("Введите число для заданной точности числа Пи:\n"))
print(f'{round(pi, d)}')