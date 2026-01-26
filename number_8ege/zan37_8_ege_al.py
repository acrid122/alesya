from itertools import *
num = 0
for elem in product('АВИЙКПС', repeat = 6):
    elem = ''.join(elem)
    elem2 = elem.replace('И', 'А')
    if 'АА' in elem2:
        num += 1
        if elem == 'КАКААА':
            print(num)
            break

from itertools import *

num = 0
for number, elem in enumerate(product('АБИЛМСУЦЯ', repeat = 5), 1):
    elem = ''.join(elem)
    if number % 2 != 0 and elem[-1] != 'Я' and sum(elem.count(j) for j in 'АИУЯ') == 2:
        num = number
print(num)

from itertools import *

sp = []
for number, elem in enumerate(product('*В*КПРЧ*', repeat = 5),  1):
    elem = ''.join(elem)
    if number % 5 != 0:
        sp.append(elem)

for number, elem in enumerate(sp, 1):
    elem = ''.join(elem)
    if '*' not in elem and len(elem) == len(set(elem)):
        print(number)
        break


from itertools import *

num1, num2 = 0, 0
for number, elem in enumerate(product('АЕЛМНОРЬ', repeat = 6), 1):
    elem = ''.join(elem)
    if elem.startswith('НОРМ') and num1 == 0:
        num1 = number
    if elem.startswith('НЕНОРМ') and num2 == 0:
        num2 = number
print(abs(num2 - num1) - 1)

from itertools import *

num = 0
for number, elem in enumerate(product('АБРШ', repeat = 5), 1):
    elem = ''.join(elem)
    if sum(elem.count(i) for i in 'БРШ') <= 3 and len(elem) == len(set(elem)) + 1:
        num = number

print(num)

from itertools import * 

sp = list(product('АИКЛМЬ', repeat = 6))
for number, elem in enumerate(sp, 1):
    elem = ''.join(elem)
    if elem[0] == 'К' and elem[-1] == 'Ь' and len(elem) == len(set(elem)) and 