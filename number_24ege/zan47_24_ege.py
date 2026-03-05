import string

p = string.digits

s = '234XXXX12XX012XXX2000XXXXX3001XXX3'
l, r = 0, 0
sp = []

while l < len(s):
    if s[l] in p and s[l] != '0': #число не может начинаться с нуля
        r = l
        while r < len(s) and s[r] in p:
            r += 1
        sp.append(s[l : r])
        l = r
    else:
        l += 1

print(sp) 

import string

p = string.printable[:14]

with open('24_26551.txt') as f:
    s = f.readline().strip().lower() #привожу к нижнему регистру, так как в printable сначала идут строчные буквы

#s = 'XXXXXXX01aXXXX2b3cXXXX389XXXX2222222111XXX99' #1a, 2b3c, 38, 2222222

k = '123'

l, r = 0, 0
maxs = float('-inf')

while l < len(s):
    if s[l] in p and s[l] != '0':
        r = l
        ind_even = l if int(s[l], 14) % 2 == 0 else -1
        while r < len(s) and s[r] in p:
            if int(s[r], 14) % 2 == 0:
                ind_even = r #это нужно, чтобы запомнить индекс последней четной цифры
            r += 1
        if ind_even != -1: #если ind_even не поменялся
            maxs = max(maxs, ind_even - l + 1)
        l = r
    else:
        l += 1

print(maxs)


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




