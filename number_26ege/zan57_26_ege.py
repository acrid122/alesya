with open('26_21598.txt') as f:
    N = int(f.readline())
    sp = list(tuple(map(int, line.split())) for line in f)

sp.sort()

new_sp = [0] * 1441
count, max_count = 0, 0
k = []

for start, end in sp:
    new_sp[start] += 1
    new_sp[end] += -1

for i in range(len(new_sp)):
    if new_sp[i] == 0:
        count += 1
    else:
        k.append(i)
        max_count = max(max_count, count + 1)
        count = 0

print(k[-2], max_count)
#1431 13

'''
0 1 2 3 4 5 6 7 8 9 10
0 0 0 0 0 0 0 0 0 0 1

0-1 = 1
1-2 = 2
2-3 = 3
3-4 = 4
4-5 = 5
5-6 = 6
6-7 = 7
7-8 = 8
8-9 = 9
9-10 = 10
'''

with open('26_22605 (1).txt') as f:
    N = int(f.readline())
    sp = list(tuple(map(int, line.split())) for line in f)

sp.sort()

new_sp = []

for i in range(len(sp) - 1):
    x, y = sp[i], sp[i + 1]
    if x[0] == y[0] and x[1] == y[1]:
        new_sp.append((y[2] - x[2], x[0] + x[1], x[0], x[1]))

new_sp.sort()
print(new_sp[:10])


#(53, 4552, 630, 3922)


with open('26.20_19726.txt') as f:
    N = int(f.readline())
    sp = list(tuple(map(int, line.split())) for line in f)


sp.sort(key = lambda x: (x[1], x[0]))

count = 1
tmp = sp[0][1]
last = tuple()

for i in sp:
    if i[0] > tmp:
        count += 1
        tmp = i[1]
        last = i

max_end = 0
for i in sp[sp.index(last):]:
    if i[0] >= last[0]:
        max_end = max(max_end, i[1])
print(count, max_end)

with open('26_24624 (4).txt') as f:
    N, K = map(int, f.readline().split())
    cinema = list(tuple(map(int, f.readline().split())) for _ in range(N))
    places = list(tuple(map(int, line.split())) for line in f)

print(cinema)

places.sort()

new_places = []

for i in range(len(places) - 1):
    for j in range(i + 1, len(places)):
        if places[i][0] == places[j][0] and \
            places[i][1] == places[j][1] - 1:
            break
    else:
        new_places.append(places[i])

print(new_places[:10])
count, min_r = 0, float('inf')

'''
[
(1, 19, 1), (1, 19, 6), (1, 19, 15), (1, 19, 18), 
(1, 19, 20), (1, 19, 21), (1, 19, 22), 
(1, 19, 23), (1, 19, 24), (1, 19, 26)]
'''

for i in range(1, len(new_places)):
    x, y = new_places[i - 1], new_places[i]
    if x[0] == y[0]: #одинаковые кинозалы
        if x[1] == y[1]: #одинаковые ряды
            if y[2] - x[2] >= 5:
                min_r = min(min_r, x[1])
                count += y[2] - x[2] - 5 + 1
        else: #разные ряды
            #для предыдущего ряда посчитать, сколько способов
            #есть посадить 5 друзей от того места до конца ряда
            if cinema[x[0] - 1][2] - x[2] >= 5:
                min_r = min(min_r, x[1])
                count += cinema[x[0] - 1][2] - x[2] - 5 + 1
            #для текущего ряда посчитать, сколько способов
            #есть посадить 5 друзей слева от текущего места 
            if y[2] - 1 >= 5:
                min_r = min(min_r, y[1])
                count += y[2] - 5
    else: #разные кинозалы
        if cinema[x[0] - 1][2] - x[2] >= 5:
                min_r = min(min_r, x[1])
                count += cinema[x[0] - 1][2] - x[2] - 5 + 1
            #для текущего ряда посчитать, сколько способов
            #есть посадить 5 друзей слева от текущего места 
        if y[2] - 1 >= 5:
            min_r = min(min_r, y[1])
            count += y[2] - 5
print(min_r, count)

