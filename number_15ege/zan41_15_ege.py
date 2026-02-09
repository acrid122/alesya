B = range(170, 221)
count = 0

for a in range(1, 1000):
    for x in range(1, 1000):
        if not((x % a == 0) or ((x in B) <= (x % 24 != 0))):
            break
    else:
       count += 1

print(count) 

for a in range(1000):
    fl = True
    for x in range(1, 1000):
        for y in range(1, 1000):
            if not((x - 3 * y < a) or (y > 400) or (x > 56)):
                fl = False
                break
        if not fl:
            break
    if fl:
        print(a)
        break

for a in range(2000, 0, -1):
    for x in range(1, 10000):
        if not((x & a != 0) <= ((x & 698 == 0) <= (x & 321 != 0))):
            break
    else:
        print(a)
        break

""" for a in range(2000, 0, -1):
    if all(((x & a != 0) <= ((x & 698 == 0) <= (x & 321 != 0))) == True for x in range(1, 10000)):
        print(a)
        break """

def f(x, a1, a2):
    P = 10 <= x <= 150
    Q = 160 <= x <= 250
    R = 240 <= x <= 300
    A = a1 <= x <= a2
    return (Q <= P) or ((not A) <= R)

gr = sorted(i for x in (10, 150, 160, 240, 300) for i in (x, x + 0.2, x - 0.2))
min_s = float('inf')

for a1 in gr:
    for a2 in gr:
        if a1 <= a2 and all(f(x, a1, a2) for x in range(-1000, 1000)):
            min_s = min(min_s, round(a2 - a1))

print(min_s)