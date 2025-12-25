def f(x, m):
    if x >= 125:
        return m % 2 == 0
    if m == 0:
        return 0
    sp = [f(x + 2, m - 1), f(x + 4, m - 1), f(x * 2, m - 1)]
    return any(sp) if m % 2 != 0 else all(sp)

print(19, [i for i in range(1, 125) if f(i, 2)])
print(20, [i for i in range(1, 125) if not f(i, 1) and f(i, 3)])
print(21, [i for i in range(1, 125) if not f(i, 2) and f(i, 4)])