#bin() - из 10 СС в 2 СС
#oct() - из 10 СС в 8 сс
#hex() - из 10 СС в 16 сс

#Немного модифицированная функция перевода из 10 СС в 2 СС

import string

print(string.printable)

def f(x, a):
    s = ''
    while x > 0:
        s = string.printable[x % a] + s
        x //= a
    return s

print(f(99, 25))

def rec_f(x, a):
    return '' if x == 0 else rec_f(x // a, a) + string.printable[x % a]

'''
rec_f(99, 25) = '3o'
rec_f(99 // 25, 25) = '3' + 'o' = '3o'
rec_f(3 // 25, 25) = '' + '3' = '3'
rec_f(0, 25) = ''
'''

print(rec_f(99, 25))


mas = []

for n in range(2, 1000):
    str_n = str(n)
    s1 = sum(map(lambda x: int(x) if int(x) % 2 == 0 else 0, str_n))
    s2 = sum(map(int, str_n[1::2]))
    r = abs(s1 - s2)
    if r == 9:
        mas.append(n)

print(min(mas))


def f(x, a):
    return '' if x == 0 else rec_f(x // a, a) + string.printable[x % a]


mas = []

for n in range(1, 1000):
    n_5 = f(n, 5)
    if int(n_5[-1]) % 2 == 0:
        n_5 += '2'
    else:
        n_5 = '2' + n_5 + '3'
    
    r = int(n_5, 5)
    if r < 1000:
        mas.append(n)

print(max(mas))


mas = []

for n in range(10, 1000):
    str_n = str(n)
    pairs = list(map(lambda x: int(''.join(x)), zip(str_n, str_n[1:])))
    max_p, min_p = max(pairs), min(pairs)
    r = max_p + min_p
    if r == 137:
        mas.append(n)

print(min(mas))
#p = '1234567'
'''
'1234567' = p
'234567' = p[1:]

zip(p, p[1:])

('1', '2'), ('2', '3'), ('3', '4') ...

map(lambda x: int(''.join(x)), zip(p, p[1:]))
'''


def f(x, a):
    return '' if x == 0 else f(x // a, a) + string.printable[x % a]

mas = []
for n in range(1, 10000):
    dev = f(n, 9)
    for i in range(5):
        if dev.count('5') == dev.count('7'):
            dev += dev[-1]
        else:
            dev += sorted(dev, key = lambda x: dev.count(x))[-1]
    r = hex(int(dev, 9))
    if 'bac' in r:
        mas.append(n)
        
print(max(mas))