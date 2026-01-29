from itertools import *

count = 0

for elem in product(range(16), repeat = 5): #product(string.printable[:16] ...)
    if elem[0] != 0 and all(elem.count(i) <= 2 for i in elem) and elem.count(1) + elem.count(4) + elem.count(9) >= 1:
        count += 1
print(count)

from itertools import *

count = 0

for elem in product('ДГИАШЭ', repeat = 5):
    if elem[0] not in 'ИАЭ' and elem[-1] not in 'ДГШ':
        count += 1

print(count)

from itertools import *

count = 0

for elem in product('КОТБУС', repeat = 8):
    elem = ''.join(elem)
    if 'КОТ' in elem and elem[0] not in 'ОУ':
        count += 1

print(count)

from itertools import *

count = 0

for elem in product('01*3*5*', repeat = 7):
    elem = ''.join(elem)
    if elem[0] != '0' and elem.count('*') + elem.count('0') == 2:
        count += 1

print(count)

from itertools import *

count = 0

for elem in product('0+*+*+6+*', repeat = 7):
    elem = ''.join(elem)
    elem2 = elem.replace('0', '*').replace('6', '*')
    if elem[0] != '0' and elem.count('6') == 1 and '**' not in elem2 and '++' not in elem2:
        count += 1

print(count)

from itertools import *

count = 0

for elem in permutations('++++++****'):
    elem = ''.join(elem)
    if '+++' not in elem and '***' not in elem:
        count += 1

print(count // 4)

from itertools import *

count = 0

for elem in permutations('+++++*АА'):
    elem = ''.join(elem)
    if 'АА' not in elem:
        count += 1

print(count // 2)


