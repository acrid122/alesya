with open('26_27779 (2).txt') as f:
    N = int(f.readline())
    sp = list(map(int, f))

sp.sort(reverse=True)

big = sp[0]
count, min_cookie = 1, 0

for cookie in sp:
    if big - cookie >= 8:
        count += 1
        big = cookie
        min_cookie = cookie

print(count, min_cookie)

with open('26_27779 (2).txt') as f:
    N = int(f.readline())
    sp = list(map(int, f))

sp.sort(reverse=True)
count, min_cookie = 1, 0

for i in range(N): #перебираем различные стартовые коржи
    big = sp[i]
    count_i, min_cookie_i = 1, 0
    for j in range(i + 1, N):
        if big - sp[j] >= 8:
            count_i += 1
            big = sp[j]
            min_cookie_i = sp[j]
    if count_i > count:
        count = count_i
        min_cookie = min_cookie_i

print(count, min_cookie)

#[1, 2, 3] - [1, 2], [1, 3], [2, 3]
'''
for i in range(len(sp)):
    for j in range(i + 1, len(sp)):
        print(sp[i], sp[j])
'''

with open('26_27636 (2).txt') as f:
    S, N = map(int, f.readline().split())
    sp = list(map(int, f))

sp.sort()

summa, count = 0, 0

for cont in sp:
    if summa + cont <= S:
        summa += cont
        count += 1

print(N - count, sum(sp) - summa)

with open('26_25363 (3).txt') as f:
    N = int(f.readline())
    sp = list(map(lambda x: tuple(map(int, x.split())), f))

print(sp[0])
#(979, 1257)

new_sp = [(ind, 1, x) if x < y else (ind, 2, y) for ind, (x, y) in enumerate(sp, 1)] #x, y - заключаем в скобки, так как без них в цикле будет 3 элемента, а у нас всего 2 объекта

#(110, 220) -> (1, (110, 220)) -> ind = 1, x = 110, y = 220 -> x < y == О < A -> (ind, 1, x) == (1, 1, 110)

new_sp.sort(key = lambda x: x[2]) #сортируем по времени

start, end = 0, N + 1

for elem in new_sp:
    if elem[1] == 1:
        start += 1
    else:
        end -= 1

print(new_sp[-1][0], N - end)

from collections import defaultdict

""" with open('26_24897 (2).txt') as f:
    N = int(f.readline())
    sp = list(map(lambda x: tuple(map(int, x.split())), f))

sp.sort(key = lambda x: (x[1], x[2], -x[0]))
'''
1 1 345
1 1 100
1 2 346
1 3 343
1 3 324
'''

d = defaultdict(list) # номер_дома: [num_падика1: min_ID1, num_падика2: min_ID2, ...]

for elem in sp: #elem = (ID, номер_дома, номер_падика)
    #Что текущего подъезда еще нет в словаре с домами
    #Если текущий подъезд уже есть, то добавить минимальный ID
    #Подъезды должны подряд идущими
    '''
    Я в первый дом добавил элемент, связанный с первым подъездом. Тогда, если я встречу первый подъезд еще раз, мне надо проверять ID добавляемый с ID, который уже есть.
    Поскольку ID надо брать минимальный
    '''
    if  """



with open('26_23283 (1).txt') as f:
    K = int(f.readline()) #количество окон
    N = int(f.readline()) #количество граждан
    sp = list(map(lambda x: tuple(map(int, x.split())), f))

windows = [0] * K
sp.sort()
count, maxs = 0, 0
for start, end in sp:
    '''
    [0, 0]

    30 60
    40 100
    59 60
    61 100
    101 144
    
    1:
    30 60, 61 100, 101 144

    2:
    40 100
    '''
    for i in range(K):
        if windows[i] <= start:
            windows[i] = end + 1
            count += 1
            maxs = i + 1
            break
print(count, maxs)