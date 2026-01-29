from itertools import *
count = 0
for elem in product('ВЗГЛЯД', repeat = 4):
    elem = ''.join(elem)
    if 1 <= elem.count('З') <= 2:
        count += 1
print(count)

from itertools import *
count = 0
for elem in permutations('+++***'):
    if elem[0] != '*':
        count += 1
print(count // 2)

from itertools import *
count = 0
for elem in product('0*+*+*+', repeat = 5):
    elem = ''.join(elem)
    elem2 = elem.replace('0', '+')
    if elem[0] != '0' and elem2.count('++') >= 2 and '+++' not in elem2:
        count += 1
print(count)

from itertools import *
count = 0
for elem in product(range(25), repeat = 4):
    if elem[0] != 0 and sum(elem.count(i) for i in range(1, 25, 2)) == 1 and sum(elem.count(i) for i in range(6)) <= 2:
        count += 1
print(count)

from itertools import *
count = 0

for elem in product('0**5***++++++', repeat = 6):
    elem = ''.join(elem)
    elem2 = elem.replace('5', '*')
    if elem[0] != '0' and elem.count('5') <= 1 and '**' not in elem2:
        count += 1
print(count)

from itertools import *
count = 0
for elem in product(range(7), repeat = 5):
    if elem.count(6) == 1 and elem[0] != 0 and sum(i for i in elem if i % 2 == 0) < sum(i for i in elem if i % 2 != 0):
        count += 1
print(count)




    