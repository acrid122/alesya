import string 

for x in string.printable[18::-1]:
    ch1 = int(f"2e{x}g8", 19)
    ch2 = int(f"6f{x}bg", 19)
    s = ch1 + ch2
    if s % 18 == 0:
        print(s // 9)
        break


def per(x, a):
    return sum(x[i] * a ** (len(x) - i - 1) for i in range(len(x)))

for x in range(40):
    ch1 = per([8, 7, 1, x, 2, 9, 1], 40)
    ch2 = per([3, 6, 6, x, 6, 3, 1], 40)
    ch3 = per([9, 7, 3, x, 6, 1, 8], 40)
    s = ch1 + ch2 + ch3
    if s % 39 == 0:
        print(s // 13)
        break

mas = []
for x in range(1, 32000 + 1):
    v = 75 ** 314 + 75 ** 118 - x
    count = 0
    while v > 0:
        if v % 75 == 0:
            count += 1
        v //= 75
    mas.append(count)

print(min(mas))


import string

s = string.printable[:21]

for x in s:
    for y in s:
        ch1 = int(f"12{y}{x}9", 21)
        ch2 = int(f"36{y}99", 21)
        summa = ch1 + ch2
        if summa % 18 == 0:
            ch1 = int(f"125{x}9", 21)
            ch2 = int(f"36599", 21)
            print((ch1 + ch2) / 18)
            #exit() #функция, которая завершает работу всей программы

v = (16 ** 350 * ((15 * 3 - 29) ** 16384) + 1007) // 63 #фиксим целочисленным делением
count = 0
while v > 0:
    if v % 4 == 1:
        count += 1
    v //= 4
'''
Traceback (most recent call last):
  File "<pyshell#0>", line 1, in <module>
    (16 ** 350 * ((15 * 3 - 29) ** 16384 + 1007)) / 63
OverflowError: integer division result too large for a float
'''
print(count)