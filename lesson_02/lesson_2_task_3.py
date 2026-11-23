import math


def square(side):
    area = side * side
    return math.ceil(area)


side = float(input('Введите длинну одной стороны: '))
result = square(side)
print(f"Площадь квадрата равна: {result}")
