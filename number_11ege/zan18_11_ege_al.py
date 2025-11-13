from math import log2, ceil

for k in range(1, 10 ** 5):
    i = ceil(log2(25))
    V = ceil(k * i / 8)
    if 947 * V > 6 * 2 ** 10:
        print(k)
        break

i1 = ceil(log2(26))
i2 = ceil(log2(99999))
V12 = ceil((10 * i1 + i2) / 8)
V3 = 13
print(1800 // (V12 + V3))

for k in range(1, 10000):
    i = ceil(log2(37))
    V = ceil(k * i / 8)
    if V * 3548 > 12 * 2 ** 10:
        print(k)
        break

for V2 in range(10000, 0, -1):
    i = ceil(log2(132))
    V1 = ceil(18 * i / 8)
    V = V1 + V2
    if V * 2000 <= 100 * 2 ** 10:
        print(V2)
        break

for n in range(10 ** 5, 0, -1):
    i = ceil(log2(n))
    V = ceil(257 * i / 8)
    if V * 295740 <= 33 * 2 ** 20:
        print(n)
        break


i = ceil(log2(1030))
V1 = ceil(156 * i / 8)
print(ceil(V1 * 7168 / 2 ** 10))

'''
for p in range(10 ** 8, 0, -1):
    i = ceil(log2(10 + 26 + 32724))
    V = ceil(223 * i / 8)
    if V * p <= 17 * 2 ** 30:
        print(p)
        break
'''

i1 = ceil(log2(62))
V1 = ceil(12 * i1 / 8)
i2 = ceil(log2(1000))
V2 = ceil(i2 / 8)
V3 = 60
print(V1 + V2 + V3)

for k in range(10 ** 5, 0, -1):
    i = ceil(log2(36 + 476))
    V = ceil(k * i / 8)
    if V * 5000 <= 1 * 2 ** 20:
        print(k)
        break

for dop in range(1, 10000):
    i = ceil(log2(520))
    V1 = ceil(99 * i / 8)
    V = dop + V1
    if V * 4322 > 543 * 2 **  10:
        print(dop)
        break


for k in range(10000, 0, -1):
    i = ceil(log2(62 + 963))
    V = ceil(k * i / 8)
    if V * 2000 <= 693 * 2 ** 10:
        print(k)
        break

for k in range(1, 10000):
    i = ceil(log2(486))
    V = ceil(k * i / 8)
    if V * 708 > 213 * 2 ** 10:
        print(k)
        break

i = ceil(log2(4090))
V = ceil(79 * i / 8)
print(ceil(65536 * V / 2 ** 10))

i1 = ceil(log2(26))
i2 = ceil(log2(3000))
V1 = ceil((i1 * 20 + i2) / 8)
dop = 2500 // 50 - V1
print(dop)


for zag in range(1, 10 ** 5):
    i = ceil(log2(63))
    V1 = ceil(35 * i / 8)
    V2 = ceil(27 * i / 8)
    V = 9 * zag + 4 * V1 + 5 * V2
    if V > 320:
        print(zag)
        break


for p in range(10000, 0, -1):
    i = ceil(log2(66 + p))
    V = ceil(21 * i / 8)
    if V * 1300 <= 25 * 2 ** 10:
        print(p)
        break