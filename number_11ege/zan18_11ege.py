from math import ceil, log2

for n in range(1, 10 ** 5):
    i = ceil(log2(n))
    V = ceil(2783 * i / 8)
    if V * 3_845_627 >= 11 * 2 ** 30:
        print(n)
        break


for k in range(10 ** 5, 0, -1):
    i = ceil(log2(82))
    V1 = ceil(25 * i / 8)
    V = V1 + 30
    if V * k <= 2 ** 20:
        print(k)
        break

count = 0
for n in range(1, 10 ** 5):
    i = ceil(log2(n))
    V = ceil(157 * i / 8)
    if 30 * 2 ** 20 <= V * 233700 <= 31 * 2 ** 20:
        count += 1
print(count)