from fnmatch import fnmatch

'''
print(help(fnmatch))


    *       matches everything
    ?       matches any single character    
    [seq]   matches any character in seq    
    [!seq]  matches any char not in seq  


for i in range(0, 10 ** 10, 1917):
    if fnmatch(str(i), '3?12?14*5'):
        print(i, i // 1917)


for i in range(103, 123456789 + 1, 103):
    if str(i) == ''.join(sorted(set(str(i)))):
        print(i, i // 103)

def find_even_divisiors(x):
    s = set() if x % 2 != 0 else {x}
    for d in range(2, int(x ** .5) + 1):
        if x % d == 0:
            if d % 2 == 0:
                s.add(d)
            if x // d % 2 == 0:
                s.add(x // d)
    return len(s) if len(s) % 2 != 0 else False

count = 0
for k in range(2, 50_000, 2):
    p = find_even_divisiors(750_000 + k)
    if p and count < 5:
        count += 1
        print(k, p)
    if count == 5:
        break


def is_prime(x):
    if (x % 2 == 0 and x != 2) or x < 2:
        return False
    for d in range(3, int(x ** .5) + 1, 2):
        if x % d == 0:
            return False
    return True

from collections import defaultdict

def fact(x):

    factors = defaultdict(int)
    d = 2

    while d ** 2 <= x: #d <= sqrt(x); d <= int(x ** .5)
        if x % d == 0:
            factors[d] += 1
            x //= d
        else:
            d += 1

    factors[x] += 1

    return factors

count = 0
for i in range(12_365_266 + 1, 10 ** 10):
    p = fact(i)
    if count < 5 and len(p) == 5 and is_prime(sum(p.keys())) \
        and all(v == 1 for v in p.values()):
        count += 1
        print(i, sum(p.keys()))
    if count == 5:
        break


from fnmatch import fnmatch

for i in range(0, 10 ** 8, 153):
    if fnmatch(str(i), '1*2[02468]3*45'):
        if all(int(j) % 2 != 0 for j in str(i)[1:str(i).index('2')]):
            if all(int(j) % 2 != 0 for j in str(i)[str(i).index('2') + 3:str(i).rindex('4')]):
                print(i, i // 153)
'''
#1 способ

def is_prime(x):
    if (x % 2 == 0 and x != 2) or x < 2:
        return False
    for d in range(3, int(x ** .5) + 1, 2):
        if x % d == 0:
            return False
    return True

def find_one_prime_divisor(x):
    s = set()
    for d in range(2, int(x ** 0.5) + 1):
        if x % d == 0:
            if is_prime(d):
                s.add(d)
            if is_prime(x // d):
                s.add(x // d)
        if len(s) > 1:
            return False
    return s if len(s) == 1 else False

count = 0
for i in range(700_000 + 1, 10 ** 10):
    d = find_one_prime_divisor(i)
    if count < 5 and d:
        count += 1
        print(i, d)
    if count == 5:
        break

#2 способ
from collections import defaultdict

def fact(x):

    factors = defaultdict(int)
    d = 2

    while d ** 2 <= x:
        if x % d == 0:
            factors[d] += 1
            x //= d
        else:
            d += 1
    
    factors[x] += 1

    return factors

count = 0
for i in range(700_000 + 1, 10 ** 10):
    p = fact(i)
    if count < 5 and len(p) == 1 and list(p.values())[0] > 1:
        count += 1
        print(i, p)
    if count == 5:
        break

#3 способ

def is_prime(x):
    if (x % 2 == 0 and x != 2) or x < 2:
        return False
    for d in range(3, int(x ** .5) + 1, 2):
        if x % d == 0:
            return False
    return True

count = 0
for d in range(2, 1001):
    for exp in range(2, 30):
        if count < 5 and is_prime(d) and d ** exp > 700_000:
            count += 1
            print(d ** exp, d)
        if count == 5:
            exit
