p = 3 * 17 ** 777 + 15 * 17 ** 250 - 6 * 17 ** 100 + 2
s = set()
while p > 0:
    if (p % 17) % 2 == 0:
        s.add(p % 17)
    p //= 17
print(len(s))


for x in range(2005, 0, -1):
    p = 4 ** 163 * 5 + 12 ** 62 - x
    count_1, count_4 = 0, 0
    while p > 0:
        if p % 5 == 1:
            count_1 += 1
        if p % 5 == 4:
            count_4 += 1
        p //= 5
    if count_1 < count_4:
        print(x)
        break
        
mas = []
for x in range(2025, 1, -1):
    count = 0
    p = 5 ** 2025 + 5 ** 200 - x
    while p > 0:
        if p % 5 == 4:
            count += 1
        p //= 5
    mas.append((x, count))
    #mas.append((count, x))
mas.sort(key = lambda x: (-x[1], -x[0]))
#mas.sort(reverse = True)
print(mas[0])
def f(x, a):
    return sum(x[i] * a **(len(x) - i - 1) for i in range(len(x)))
for p in range(7, 100):
    for x in range(1, p):
        for y in range(1, p):
            for z in range(p):
                ch1 = f([y, 4, y], p)
                ch2 = f([y, 6, 5],  p)
                ch3 = f([x, z, 3, 3], p)
                if ch1 + ch2 == ch3:
                    res = f([x, y, z], p)
                    print(res)
                    exit()


