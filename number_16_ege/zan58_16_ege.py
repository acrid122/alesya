""" from functools import *

@lru_cache(maxsize=50) #@cache. на компьютерах, где мало RAM будет выдавать segmentation fault. чтобы искоренить используем lru_cache(maxsize = N) (храним N последних вызовов)
def f(n):
    if n < 10:
        return 3
    else:
        return (n + 4) * f(n - 5)

for n in range(1, 257500):
    f(n)
#RecursionError: maximum recursion depth exceeded
print((f(257487)//683 + 67 * f(257477))//f(257472))
#24994270044009

sp = []
for i in range(257500):
    if i < 10:
        sp.append(3)
    else:
        sp.append((i + 4) * sp[i - 5])
print((sp[257487]//683 + 67 * sp[257477])//sp[257472])

sp = []
for i in range(2, 257500, 5):
    if i < 10:
        sp.append(3)
    else:
        sp.append((i + 4) * sp[-1])
print((sp[(257487 - 2) // 5] // 683 + 67 * sp[(257477 - 2) // 5]) // sp[(257472 - 2) // 5])
from functools import *

@cache
def f(n):
    if n > 300000:
        return 3
    else:
        return (n + 4) * f(n + 5)

for n in range(1, 258000):
    f(n)
#RecursionError: maximum recursion depth exceeded
print((f(257487)//683 + 67 * f(257477))//f(257472)) """ 

from functools import *

@lru_cache(maxsize=31100)
def f1(n):
    if n < 31054:
        return f1(n + 4) + 3020
    return 3 * (g1(n - 2) - 15)


@lru_cache(maxsize=31100)
def g1(n):
    if n >= 28:
        return g1(n - 5) - 15
    return 3 * n - 4

#чтобы посчитать итоговое F. надо сначала узнать G

for n in range(1, 31101):
    g1(n)

for n in range(31100, 0, -1):
    f1(n)

print(f1(15))

from functools import *
@lru_cache(maxsize=700)
def f(n):
    if n >= 19:
        return f(n - 4) + 3580
    return 6 * (g(n - 7) - 36)
@lru_cache(maxsize=248200)
def g(n):
    if n >= 248045:
        return n / 20 + 28
    return g(n + 9) - 4
for n in range(248100, 0, -1):
    g(n)
for n in range(675):
    f(n)
print(f(673))

from itertools import *
@lru_cache(maxsize=2100)
def f(n):
    if n < 43:
        return g(n + 4)
    return 2 * f(n - 2) - f(n - 4) + 2
@lru_cache(maxsize=12000)
def g(n):
    if n < 11240:
        return g(n + 3) + 2
    return q(n)
@lru_cache(maxsize=11300)
def q(n):
    if n < 21:
        return n + 4
    return q(n - 4) + 2
for n in range(11246):
    q(n)

for n in range(11250, 0, -1):
    g(n)
for n in range(2050):
    f(n)
print(f(2026))

def f3(x, y, z):
    return x + y > z and y + z > x and x + z > y

for a in range(300, 0, -1):
    for x in range(1, 300):
        if not((f3(x, 10, 20) <= (max(x, 8) <= 24)) == (not f3(3, a, x))):
            break
    else:
        print(a)
        break

for a in range(0, 500):
    fl = True
    for x in range(0, 500):
        for y in range(0, 500):
            if not((2 * x + y != 150) or not(50 <= x <= 70) or (a > y)):
                fl = False
                break
        if not fl:
            break
    if fl:
        print(a)
        break