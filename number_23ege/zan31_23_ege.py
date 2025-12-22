def f(x, y):
    #x - какое-то текущее значение, y - конечное значение
    if x == y:
        return 1 #это показатель того, что мне последовательность команд подошла
    if x > y or x == 43:
        return 0 #это показатель того, что мне последовательность команд не подошла
    #рекурсивный случай
    return f(x + 2, y) + f(x + x - 1, y) + f(x + x + 1, y)

print(f(7, 63))

def f1(x, y):
    if x == y:
        return 1
    if x > y or x == 21:
        return 0
    return f1(x + 1, y) + f1(x * 3, y) + f1(x * 4, y)

print(f1(2, 16) * f1(16, 60))

def f2(x, y):
    if x == y:
        return 1
    if x > y + 100 or x % 3 == 0:
        return 0
    return f2(x - 1, y) + f2(x + 3, y) + f2(x * 2, y)

print(f2(5, 100))

def f3(x, y, s = ''):
    if x > y + 2 or s == 'AAA':
        return 0
    if x == y:
        return 1
    return f3(x - 1, y, s[-2:] + 'A') + f3(x + 5, y, s[-2:] + 'B') + f3(x * 2, y, s[-2:] + 'C')

print(f3(5, 34))

def f4(x, y, s = ''):
    if x < y or (len(s) == 3 and any(s.count(i) == 3 for i in {'A', 'B'})):
        return 0
    if x == y:
        return 1
    if x % 2 == 0:
        return f4(x - 2, y, s[-2:] + 'A') + f4(x // 2, y, s[-2:] + 'B')
    else:
        return f4(x - 2, y, s[-2:] + 'A') + f4(x - 7, y, s[-2:] + 'B')
    
print(f4(40, 1))

def f5(x, y, count = 0):
    if x in {40, 30, 20}:
        count += 1
    if x == y and count >= 2:
        return 1
    if x < y:
        return 0
    return f5(x - 1, y, count) + f5(x - 3, y, count) + f5(x // 3, y, count)

print(f5(49, 12))