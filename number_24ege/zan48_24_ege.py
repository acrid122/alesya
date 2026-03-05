with open('24_26549.txt') as f:
    s = f.readline().strip()

l, count_2025, count_y = 0, 0, 0
maxs = float('-inf')

for r in range(len(s)):
    if s[r - 4: r] == '2025':
        count_2025 += 1
    if s[r] == 'Y':
        count_y += 1
    
    if count_2025 == 50:
        if count_y >= 140:
            maxs = max(maxs, r - l)
        while count_2025 == 50:
            if s[l : l + 4] == '2025':
                count_2025 -= 1
            if s[l] == 'Y':
                count_y -= 1
            l += 1
print(maxs)

#Второй способ через .split()

s = s.split('2025')

#s[i : i + 50]

for i in range(len(s) - 49):
    if i != 0:
        k = '025' + '2025'.join(s[i : i + 50]) + '2025'
    else:
        k = '2025'.join(s[i : i + 50]) + '2025'
    maxs = max(maxs, len(k))

print(maxs)

with open('24_26077.txt') as f:
    s = f.readline().strip()

#s = 'G3126481276F3891274671280GG2716835GGG378216G78213' #3 нечет

'''
G31264812
G271683
G378216
G78213
'''
maxs = float('-inf')
for l in range(len(s)):
    if s[l] == 'G':
        r = l + 1
        count_odd = 0
        while r < len(s):
            if s[r].isdigit() and int(s[r]) % 2 != 0:
                count_odd += 1
            if count_odd == 46:
                break
            if s[r] == 'G':
                break
            r += 1
        if count_odd >= 45:
            maxs = max(maxs, r - l)
    else:
        l += 1

print(maxs)

with open('24_26077.txt') as f:
    s = f.readline().strip().split('G')

#s = ['3126481276F3891274671280', '', '2716835', '', '', '378216', '78213'] #3 нечет
maxs = float('-inf')

for i in s:
    count_odd = 0
    for ind, elem in enumerate(i):
        if elem.isdigit() and int(elem) % 2 != 0:
            count_odd += 1
        if count_odd == 46:
            break
    if count_odd >= 45:
        maxs = max(maxs, ind + 1)
    
print(maxs)

for i in s:
    count_odd = 0
    for j in range(len(i)):
        if i[j].isdigit() and int(i[j]) % 2 != 0:
            count_odd += 1
        if count_odd == 46:
            break
    if count_odd >= 45:
        maxs = max(maxs, j + 1)
    
print(maxs)
