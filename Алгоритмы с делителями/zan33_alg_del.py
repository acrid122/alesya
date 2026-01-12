#Общий подсчет делителей числа

#36: 1, 2, 3, 4, 6, 9, 12, 18, 36 = 9 штук

def bad_count_dels(x): #принимает одно число (то число, количество делителей которого надо посчитать)
    count = 0
    for d in range(1, x + 1):
        if x % d == 0:
            count += 1
    return count

print(bad_count_dels(36))

'''
36

1 | 36
2 | 18
3 | 12
4 | 9
6

Главная оптимизация заключается в том, чтобы рассматривать диапазон делителей до корня числа. 
Если мы идем до корня, то можно найти абсолютно все делители.
'''

def good_count_dels(x):
    count = 0
    for d in range(1, int(x ** .5) + 1):
        if x % d == 0:
            if d != x // d:
                count += 2
            else:
                count += 1
    return count

print(good_count_dels(36))


#Если важно знать все делители или какую-то часть

def good_find_dels(x):
    s = set() #лучше использовать множества, так как это коллекция уникальных объектов
    for d in range(1, int(x ** .5) + 1):
        if x % d == 0:
            s.add(d)
            s.add(x // d)
    return s, len(s), sum(s)

print(good_find_dels(36))


#Алгоритм проверки числа на простоту

def is_prime(x):
    if x % 2 == 0 and x != 2: #любое четное число за исключением 2
        return False
    for d in range(3, int(x ** .5) + 1, 2): #проверяем только нечетные делители
        if x % d == 0:
            return False
    return x >= 2

print(is_prime(2), is_prime(109), is_prime(59757))

#Взаимно простые - те числа, у которых НОД = 1

def good_find_dels(x):
    s = set() #лучше использовать множества, так как это коллекция уникальных объектов
    for d in range(1, int(x ** .5) + 1):
        if x % d == 0:
            s.add(d)
            s.add(x // d)
    return s


def relatively_prime(s1, s2):
    return (s1 & s2) == {1} #& - пересечение множеств


s1 = good_find_dels(5)
s2 = good_find_dels(7)
print(relatively_prime(s1, s2))


#Факторизация - алгоритм разложения на простые множители

#36 = 2 ^ 2 * 3 ^ 2

from collections import defaultdict


def fact(x):

    '''
    Обычный словарь:

    p = {
        'A': 20,
        'Б': 30,
        'В': 10
    }

    p['Г'] - будет ошибка, так как ключа не существует
    '''

    #defaultdict решает эту проблему, так как у несуществующих ключей есть значения по умолчанию
    #int - тип значения по умолчанию, если int, то 0.
    '''
    factors = {
        2: 10,
        3: 5,
        5: 1
        ...
    }
    {простой множитель: степень}
    '''
    factors = defaultdict(int)
    d = 2
    while x % d == 0:
        factors[d] += 1
        x //= d

    for d in range(3, int(x ** .5) + 1, 2):
        while x % d == 0:
            factors[d] += 1
            x //= d
    
    if x > 1:
        factors[x] = 1

    return factors

print(fact(36))
#defaultdict(<class 'int'>, {2: 2, 3: 2})

#Подсчет количества делителей числа
'''
Математическая формула:

N = 2 ** p * e1 ** p1 * e2 ** p2 ...  en ** pn

Количество = (p + 1) * (p1 + 1) * (p2 + 1) * ... * (pn + 1)

36 = 2 ** 2 * 3 ** 2

Количество_36 = (2 + 1) * (2 + 1) = 3 * 3 = 9

Количество_нечетных_36 = (2 + 1) = 3 | 1, 3, 9

Количество_четных_36 = 2 * (2 + 1) = 6 = Количество_36 - Количество_нечетных_36 = 9 - 3 = 6
'''

def count_divisors_from_fact(x):
    factors = fact(x) #в factors будет словарь
    total_divisors = 1
    for exponent in factors.values(): #factors.values() - возвращает список значений из словаря
        total_divisors *= (exponent + 1)

    #18 = 2 * 3 ** 2
    #18 |1, 3, 9 - нечетные
    #Всего 6 делителей, нечетные = 6 // 2 ** p, где p - степень 2; 6 // 2 = 3.

    odd_divisors = total_divisors // (factors[2] + 1)
    even_divisors = total_divisors - odd_divisors

    return total_divisors, odd_divisors, even_divisors

print(count_divisors_from_fact(36))

'''
Надо найти число, у которого ровно 4 нечетных делителя

N = 2 ** p * e1 ** p1 * e2 ** p2 ...  en ** pn

odd_divisors = (e1 + 1) * (e2 + 1) * ... * (en + 1) = 4
'''

'''
Представить число в виде N = 2 ** m * 3 ** n, где m - число четное, n - число нечетное.
'''

start = 10 ** 9
finish = 2 * 10 ** 9

count = 0
for m in range(0, 33, 2):
    for n in range(1, 33, 2):
        if 10 ** 9 <= 2 ** m * 3 ** n <= 2 * 10 ** 9:
            count += 1
print(count)

'''
Найти все числа, у которых ровно три нетривиальных делителя. Нетривиальными делителями обычно считаются
делители, отличные от 1 и самого числа.

N = 2 ** p * e1 ** p1 * e2 ** p2 ...  en ** pn

all_divisors = (p + 1) * (e1 + 1) * (e2 + 1) ... = 5
-> понимаем, что только 1 множитель в 4 степени.
'''
for ch in range(10 ** 9, 2 * 10 ** 9):
    if ch ** (1/ 4) == int(ch ** (1/ 4)):
        break

#НОД и НОК
from math import gcd, lcm

#gcd - НОД
#lcm - НОК

print(gcd(36, 12))
print(lcm(36, 12))