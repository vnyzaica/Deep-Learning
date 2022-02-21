# Почти двойной факториал
#
#
# Реализуйте функцию almost_double_factorial(n), вычисляющую произведение всех нечётных натуральных чисел, не превосходящих nnn.
# В качестве аргумента ей передаётся натуральное (ноль -- натуральное) число n⩽100n \leqslant 100n⩽100.
# Возвращаемое значение - вычисленное произведение.
#
# В случае, если n = 0, требуется вернуть 1.

def almost_double_factorial(number):
    Z=1
    if number == 0:
        Z=1
    else:
        n=1
        while (n<=number):
            Z=Z*n
            n=n+2
    return Z

x = int(input("Введите число "))
print(almost_double_factorial(x))
