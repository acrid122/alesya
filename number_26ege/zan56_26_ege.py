with open('26_23383 (1).txt') as f:
    N = int(f.readline())
    sp = set(tuple(map(int, line.split())) for line in f) #удалить дубликаты


sp = sorted(sp, key = lambda x: (x[1], x[0])) 

new_sp = [0] * 10 ** 6
'''
9
41 3
50 33
41 125
42 125
43 125
42 126
43 126
50 126
42 127
'''

'''
42 126
43 126
50 126
'''
count = 0
for i in range(len(sp) - 1):
    x, y = sp[i], sp[i + 1]
    if x[1] == y[1]:
        if y[0] - x[0] == 1:
            count += 1
        else:
            count += 1
            if count >= new_sp[x[1]]:
                new_sp[x[1]] = count
            count = 0
    else:
        count += 1
        if count >= new_sp[x[1]]:
                new_sp[x[1]] = count
        count = 0
    if i == len(sp) - 2:
        count += 1
        if count >= new_sp[y[1]]:
                new_sp[y[1]] = count
        count = 0
print(max(new_sp), new_sp.index(max(new_sp)))

with open('26_22127.txt') as f:
    N = int(f.readline())
    sp = list(tuple(map(int, line.split())) for line in f)

sp.sort(key = lambda x: (x[0], x[1]))
""" sp = [(10, 50), (100, 150), (110, 155), (120, 160), (130, 170), (151, 170)] """
count, summa = 0, 0
day = 24 * 60 * 60 * 1000

if sp[0][0] > 0:
     count += 1
     summa += sp[0][0]

cur = sp[0][1]
for start, end in sp[1:]:
     if start > cur + 1:
          count += 1
          summa += start - cur - 1
          cur = end
     else:
          cur = max(cur, end) 

if cur < day - 1:
     count += 1
     summa += day - cur - 1

     
print(count, summa)

