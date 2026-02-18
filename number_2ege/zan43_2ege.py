from itertools import *

def f(x, y, w, z):
    return (x or y) and not(y == z) and not w

for x1, x2, x3, x4 in product([0, 1], repeat = 4):
    table = [
        (1, x1, 1, x2), 
        (0, 1, x3, 0),
        (x4, 1, 1, 0)
    ]
    if len(table) == len(set(table)):
        for p in permutations("xywz"):
            if all(f(**dict(zip(p, line))) for line in table):
                print(*p)


a = [1, 2, 3, 4, 5]
b = [6, 7, 8, 9, 0]
c = [10, 11, 12]

p = "xywz"
l = [1, 0, 1, 0]

def f_prob(x, y, w, z):
    return x, y, w, z

print(f_prob(**dict(zip(p, l))))
print(f_prob(x = 1, y = 0, w = 1, z = 0))

def oll(a, b):
    return a, b

bb = {
    'a': 100,
    'b': 50
}
print(oll(**bb)) #print(oll(a = 100, b = 50))

#print(oll(*bb))

from itertools import *

def f1(x, y, w, z):
    return (z <= y) or ((w <= x) <= y)

for x1, x2, x3, x4, x5, x6 in product([0, 1], repeat = 6):
    table = [
        (x1, 0, 0, x2), 
        (x3, x4, 1, x5), 
        (x6, 1, 1, 1)
    ]
    if len(table) == len(set(table)):
        for p in permutations("xywz"):
            if all(not(f1(**dict(zip(p, line)))) for line in table):
                print(*p)


from itertools import *

def f2(x, y, w, z):
    return (((not y) <= (not w)) <= (not z)) <= x

for x1, x2, x3, x4, x5 in product([0, 1], repeat = 5):
    table = [
        (x1, 1, x2, 1, 0),
        (0, 1, x3, 0, 1), 
        (x4, x5, 1, 0, 0)
    ]
    if len(table) == len(set(table)):
        for p in permutations("xywz"):
            if all(f2(**dict(zip(p, line))) == line[-1] for line in table):
                print(*p)