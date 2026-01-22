""" # 25 номер
def find_3_del(x):
    s = set()
    for d in range(1, int(x ** .5) + 1):
        if x % d == 0:
            if d % 2 == 0:
                s.add(d)
            if (x // d) % 2 == 0:
                s.add(x // d)
            if len(s) > 3:
                return []
    return sorted(s) if len(s) == 3 else []
k = 0
for x in range(113 * 10 ** 6, 114 * 10 ** 6 + 1):
    if k == 7:
        break
    s = find_3_del(x)
    if s:
        k += 1
        print(x, s[1]) 

'''
N = 2 ** p * e1 ** p1 * e2 ** p2 * ... * en ** pn

Количество = (p + 1) * (p1 + 1) * (p2 + 1) * ... * (pn + 1)
Количество_нечетных = (p1 + 1) * (p2 + 1) * ... * (pn + 1)
Количество_четных = Количество - количество_нечетных = p * (p1 + 1) * (p2 + 1) * ... * (pn + 1)

36 = 2 ** 2 * 3 ** 2

Количество_четных = 3 = p * (p1 + 1) * (p2 + 1) * ... * (pn + 1) = 3, p - при степени 2.

p * (p1 + 1) * (p2 + 1) * ... * (pn + 1) = 3
p = 3, p1 ... pn = 0
p = 1, p1 = 2
'''

def find_3_del(x):
    s = set()
    for d in range(1, int(x ** .5) + 1):
        if x % d == 0:
            if d % 2 == 0:
                s.add(d)
            if (x // d) % 2 == 0:
                s.add(x // d)
            if len(s) > 3:
                return []
    return sorted(s) if len(s) == 3 else []
k = 0
for x in range(113 * 10 ** 6, 114 * 10 ** 6 + 1):
    if k == 7:
        break
    if int(x ** (1/3)) == x ** (1/3) or (int((x // 2) ** (1/2)) == (x // 2) ** (1/2)):
        s = find_3_del(x)
        if s:
            k += 1
            print(x, s[1])

def fact(x):

    factors = defaultdict(int)
    d = 2

    while d ** 2 <= x: #d <= sqrt(x); d <= int(x ** .5)
        if x % d == 0 and '2' in str(d): #содержит в своей записи ровной одну цифру 2
            factors[d] += 1
            x //= d
        else:
            d += 1

    factors[x] += 1
    '''
    factors = {2: 2, 3: 2, 5: 3}
    (len(factors) == 2 and all(i == 1 for i in factors.values())) or (len(factors) == 1 and list(factors.values())[0] == 2)


    '''
    return factors

def is_prime(x):
    if (x % 2 == 0 and x != 2) or x < 2:
        return False
    for d in range(3, int(x ** .5) + 1, 2):
        if x % d == 0:
            return False
    return True

def sum_of_del(x):
    s = set()
    for d in range(2, int(x ** .5) + 1):
        if x % d == 0:
            if is_prime(d):
                s.add(d)
            if is_prime(x // d):
                s.add(x // d)            
    return sum(s)

for x in range(33333, 55556):
    s = sum_of_del(x)
    if s > 250 and x % s == 0:
        print(x, s)
print(sum_of_del(38086)) """

with open('17_25356 (1).txt') as f:
    sp = list(map(int, f)) #чтобы получить список чисел

count, max_s = 0, float('-inf') #максимум инициализируем минимальным значением, а минимум - максимальным
max_30 = max(i for i in sp if abs(i) % 100 == 30) #все остатки от деления берем от модуля числа, так как остатки от отрицательных чисел в математике берутся иначе


def check_four(x):
    return 1000 <= abs(x) <= 9999

#1 способ. по индексам
for i in range(len(sp) - 2): #чтобы не было ошибки - отсекаем лишние индексы
    x, y, z = sp[i:i+3] #sp[i], sp[i + 1], sp[i + 2] 
    '''
    5 способ, как посчитать кол-ов 4-значных.

    Вынести в отдельную функцию проверку на 4-значность.

    Вызвать функцию для каждого числа. Сложить результаты.

    Логические значения можно складывать между собой. True + True = 2

    (check_four(x) + check_four(y) + check_four(z)) == 0
    '''
    if (check_four(x) + check_four(y) + check_four(z)) == 0 and (x + y + z) > max_30:
        count += 1
        max_s = max(x + y + z, max_s)
print(count, max_s)

with open('17_18257.txt') as f:
    sp = list(map(int, f))
count = 0
ras = float('inf')
max_in_sp = max(sp)
for i in range(len(sp) - 1):
    for j in range(i + 1, len(sp)):
        x, y = sp[i], sp[j]
        if (i + j + 2) % 10 == max_in_sp % 10:
            count += 1
            ras = min(abs((x + y) - (i + j + 2)), ras) #номер = индекс + 1
print(count, ras)

'''
1, 2, 3, 4, 5

1, 2, 3
2, 3, 4
3, 4, 5

4, 5, ... - нет

1, 2, 3, 4

1, 2
2, 3
3, 4

1, 2, 3, 4, 1, 2
'''

s = '123433'
print(len(s) == len(set(s)))
'''
set(s) = {'1', '2', '3', '4'}
'''

with open('17_9070.txt') as f:
    sp = list(map(int, f))

count, min_s = 0, float('inf')

min_tr = min(i for i in sp if len(str(i)) == len(set(str(i))) == 3)

#1, 2, 3, 4 -> len(sp) = 4, 4 // 2 = 2

#1, 2, 3, 4, 5 -> len(sp) = 5, 5 // 2 = 2
for i in range(0, len(sp) // 2):
    x, y = sp[i], sp[len(sp) - i - 1] #симметричные пары
    if x * y % min_tr == 0:
        count += 1
        min_s = min(min_s, x + y)

print(count, min_s)

with open('17_7848 (1).txt') as f:
    sp = list(map(int, f))

count, min_s = 0, float('inf')

#невозрастание = убывание с повторениями
#строгое убывание = убывание без повторений

s = '321'

print(list(s) == sorted(s, reverse = True) and len(s) == len(set(s)))

sum_min = sum(map(int, str(min(i for i in sp if list(str(i)) == sorted(str(i), reverse = True) and len(str(i)) == len(set(str(i)))))))

#sum(map(int, s)) - сумма цифр числа

def sort_increase(i):
    return list(str(i)) == sorted(str(i)) and len(str(i)) == len(set(str(i)))

for i in range(len(sp) - 1):
    x, y = sp[i : i + 2]
    if (sort_increase(x) + sort_increase(y)) == 1 and x * y % sum_min == 0:
        count += 1
        min_s = min(min_s, x + y)

print(count, min_s)