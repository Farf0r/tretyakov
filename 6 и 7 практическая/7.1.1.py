import math


def tr(x, y, z):
    p = (x + y + z) / 2
    tr = math.sqrt(p * (p - x) * (p - y) * (p - z))
    return tr


t = []
print('Введите стороны треугольника')
a = int(input('a = '))
b = int(input('b = '))
c = int(input('c = '))
t.append(tr(a, b, c))
print('Площадь треугольника: ', t)


def kv(x):
    s = x ** 2
    return s


y = []
print('Введите сторону квадрата')
d = int(input())
y.append(kv(d))
print('Площадь квадрата: ', y)


def pr(x, y):
    s = x * y
    return s


u = []
print('Введите стороны прямоугольника')
e = int(input('a = '))
f = int(input('b = '))
u.append(pr(e, f))
print('Площадь прямоугольника: ', u)
