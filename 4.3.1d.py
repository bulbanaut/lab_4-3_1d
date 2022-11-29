#! /usr/bin/python3
import math
e, length, summ = int(input('Введите число e: ')), int(input('Введите длинну числовой последовательности: ')), 0
for n in range(0, length):
    a = (10**n) / (math.factorial(n))
    if math.fabs(a) >= e:
        summ = summ + a
if summ != 0:
    print('Сумма: ', a)
else:
    print('Подходящих членов нет')