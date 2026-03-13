s = open('24_16333.txt').readline().strip()

table = str.maketrans("RW24", "QQ11")
s = s.translate(table)

while 'QQ' in s or '11' in s:
    s = s.replace('QQ', 'Q*Q')
    s = s.replace('11', '1*1')

s = s.split('*')
print(len(max(s, key = len)))

import re

s = open('24_18186 (1).txt').readline().strip()

""" s = re.findall(r"\bbba\b", s) """
spl = re.split(r'[BCDFGH]{2}[AE]', s)
print(len(max(spl, key = len)) + 6)

s = open('24_18186 (1).txt').readline().strip()
""" fnd = re.findall(r'[BCDFGH]{2}[AE](?:(?![BCDFGH]{2}[AE]).)*[BCDFGH]{2}[AE]', s)
print(max(fnd, key = len)) """

table = str.maketrans('CDFGHE', 'BBBBBA')
spl2 = s.translate(table).split('BBA')
print(len(max(spl2, key = len)) + 6)

s = open('24_18186 (1).txt').readline().strip()
table = str.maketrans('CDFGHE', 'BBBBBA')
s = s.translate(table)

l, maxs = 0, float('-inf')
count_bba = 0

for r in range(len(s)):
    if s[r - 3:r] == 'BBA':
        count_bba += 1
        if count_bba == 1:
            l = r - 3
    if count_bba == 2:
        maxs = max(maxs, r - l)
        l = r - 3
        count_bba -= 1

print(maxs)

import re

s = open('24_20813.txt').readline().strip()

s = re.findall(r'(?:0|[789][0789]*)(?:[-*](?:0|[789][0789]*))*', s)

print(len(max(s, key = len)))
import string

s = list(map(str.strip, open('24_7012.txt').readlines())) #.readlines() создает список из строк

count = 0
table = str.maketrans('','',f'{string.digits}ABCDFGHIJKLMNOPSUVXZ')
for i in s:
    q = "QWERTY"
    pos = 0
    for c in i:
        if c == q[pos]:
            pos += 1
            if pos == 6:
                count += 1
                break

print(count)

s = '7+8-3+4'
print(eval(s))