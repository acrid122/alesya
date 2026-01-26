from itertools import *

#product - генерация всех возможных сочетаний с повторениями, где порядок элементов важен. декартово произведение

'''
[('A', 'A'), ('A', 'B'), ('A', 'C'), ('A', 'D'), ('B', 'A'), ('B', 'B'), ('B', 'C'), ('B', 'D'), ('C', 'A'), ('C', 'B'), 
('C', 'C'), ('C', 'D'), ('D', 'A'), ('D', 'B'), ('D', 'C'), ('D', 'D')]
'''
print(list(product('ABCD', repeat = 2)))

#permutations - генерация всех возможных перестановок без повторений, где порядок элементов важен.


'''
[('A', 'B'), ('A', 'C'), ('A', 'D'), ('B', 'A'), ('B', 'C'), ('B', 'D'), ('C', 'A'), ('C', 'B'), ('C', 'D'), ('D', 'A'), ('D', 'B'), ('D', 'C')]
'''
print(list(permutations('ABCD', r = 2)))

#combinations - генерация всех возможных комбинаций без повторений, где порядок элементов не важен.

'''
[('A', 'B'), ('A', 'C'), ('A', 'D'), ('B', 'C'), ('B', 'D'), ('C', 'D')]
'''
print(list(combinations('ABCD', r = 2)))

a = [5, 65, 78, 3]
print(list(enumerate(a, 1)))
#[(0, 5), (1, 65), (2, 78), (3, 3)]

from itertools import *

for number, elem in enumerate(product('АГИНРТ', repeat = 6), 1):
    elem = ''.join(elem)
    if number % 2 != 0 and elem[0] not in 'АИГ' and elem.count('А') == 1:
        print(number)
        break

from itertools import *

summa = 0
for number, elem in enumerate(product('АВИКЛОРТ', repeat = 6), 1):
    elem = ''.join(elem)
    if elem in ('ВИКТОР', 'КИРИЛЛ'):
        summa += number

print(summa)

from itertools import *

num = 0
for number, elem in enumerate(product('ДИКМО', repeat = 5), 1):
    elem = ''.join(elem)
    if elem.count('М') == 2 and 'ММ' not in elem:
        num = number

print(num)

from itertools import *

count = 0

for number, elem in enumerate(product('ЕЛОПРСТ', repeat = 5), 1):
    elem = ''.join(elem)
    if number % 2 != 0 and elem[-1] in 'ЕО' and sum(elem.count(j) for j in 'ПРСТЛ') <= 3:
        count += 1

print(count)


from itertools import *

sp = []

for number, elem in enumerate(product('ЕКОФ', repeat = 5), 1):
    elem = ''.join(elem)
    #есть два способа
    # заменить при помощи replace 
    elem = elem.replace('К', 'Ф')
    if elem.count('О') == 1 and 'ОФ' not in elem and 'ФО' not in elem:
        sp.append(number)

print(sp[0] + sp[-1])


from itertools import *

sp = []
#второй способ: заменить при генерации
for number, elem in enumerate(product('Е*О*', repeat = 5), 1):
    elem = ''.join(elem)
    if elem.count('О') == 1 and 'О*' not in elem and '*О' not in elem:
        sp.append(number)

print(sp[0] + sp[-1])


from itertools import *

num = 0
for number, elem in enumerate(product('Д*ЙНПТЬ*', repeat = 4), 1):
    elem = ''.join(elem)
    if '*' not in elem and len(elem) == len(set(elem)):
        num = number

print(num)


from itertools import *

count, elem1 = 0, ''

for elem in product('012345678', repeat = 6):
    elem = ''.join(elem)
    if elem[0] != '0':
        count += 1
        elem2 = elem.replace('3', '1').replace('5', '1').replace('7', '1')
        if '11' not in elem2 and count % 10 == 5:
            elem1 = elem

print(elem1)