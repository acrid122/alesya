from functools import cache
@cache
def f(x, y, count = 0):
    if x in {24, 32}:
        count += 1
    if x == y and count == 1:
        return 1
    if x > y:
        return 0
    return f(x + 1, y, count) + f(x + 2, y, count) + f(x + 4, y, count) + f(x + 8, y, count)
print(f(16,48))

def f1(x, y, count = 0):
    if x in {9, 12}:
        count += 1
    if x == y and count == 2:
        return 1
    if x > y:
        return 0
    return f1(x + 1, y, count) + f1(x + 3, y, count) + f1(x * 2, y, count)
print(f1(3,20))

def f2(x, y):
    if x == y:
        return 1
    if x > y:
        return 0
    return f2(x + 1, y) + f2(2 * x + 1, y) + f2(2 * x, y) + f2(x * 10, y)
print(f2(1, 15))

def f3(x, y):
    if x == y:
        return 1
    if x > y:
        return 0   
    return f3(x + 1, y) + 