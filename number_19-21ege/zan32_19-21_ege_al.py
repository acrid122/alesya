def f(x, y, m):
    if x * y >= 541:
        return m % 2 == 0
    if m == 0:
        return 0
    sp = [f(x + 10, y, m - 1), f(x * 2, y, m - 1), 
          f(x, y + 10, m - 1), f(x, y * 2, m - 1)]
    return any(sp) if m % 2 != 0 else all(sp)
print(19, [i for i in range(1, 91) if f(i, 6, 2)])
print(20, [i for i in range(1, 91) if not f(i,6, 1) and f(i,6,3)])
print(21, [i for i in range(1, 91) if not f(i,6,2) and f(i,6,4)])

def f1(x,m):
    if x <= 116:
        return m % 2 == 0
    if m == 0:
        return 0
    sp = [f1(x - 7, m - 1), f1(x // 3, m - 1)]
    return any(sp) if m % 2 != 0 else all(sp)
print(19, max([i for i in range(117, 10001) if f1(i,3)]))
print(20, [i for i in range(117, 10001) if not f1(i, 1) and f1(i, 3)])
print(21, [i for i in range(117,10001) if not f1(i,2) and f1(i,4)])