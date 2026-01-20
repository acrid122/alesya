with open('17_23905.txt') as f:
    sp = list(map(int, f))
count = 0
summa_four = 0
max_37 = max(i for i in sp if i % 100 == 37)
for x, y, z, w in zip(sp, sp[1:], sp[2:], sp[3:]):
    if sum(1 for i in (x, y, w, z) if i > max_37) == 2 and sum(1 for i in (x, y, w, z) if str(i)[-1] == str(i)[-2]) == 1:
        count += 1
        summa_four += sum(i for i in (x, y, w, z) if str(i)[-1] == str(i)[-2])
print(count, summa_four)


with open('17_23563.txt') as f:
    sp = list(map(int, f))
count = 0
sum_max = float('-inf')
min_35 = min(i for i in sp if abs(i) % 35 == 0 and i > 0)
for x, y in zip(sp, sp[1:]):
    if x != y and abs(x - y) % min_35 == 0:
        count += 1
        sum_max = max(x + y, sum_max)
print(count, sum_max)

with open('17_17636.txt') as f:
    sp = list(map(int, f))
max_3 = max(i for i in sp if abs(i) % 10 == 3 and 100 <= abs(i) <= 999)
count = 0
summa = 0
for x, y, z in zip(sp, sp[1:], sp[2:]):
    if sum(1 for i in (x, y, z) if abs(i) % 10 == 3 and 100 <= abs(i) <= 999) >= 1 \
    and x + y + z < max_3:
        count += 1
        summa = max(x + y + z, summa)
print(count, summa)