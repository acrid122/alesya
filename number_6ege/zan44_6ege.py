#Начальные координаты: 0,0
#После первого цикла: максимальные координаты: 22, 16

#Начальная координата: 5,5
#После второго цикла: 5 + 77, 5 + 52
def rect(x1, y1, x2, y2):
    return {(x, y) for x in range(min(x1, x2), max(x1, x2) + 1) for y in range(min(y1, y2), max(y1, y2) + 1)}

r1 = rect(0, 0, 22, 16)
r2 = rect(5, 5, 82, 57)

print(len(r1 & r2))

per = r1 & r2

max_coord = max(per)
min_coord = min(per)

razn_x = max_coord[0] - min_coord[0]
razn_y = max_coord[1] - min_coord[1]
print(razn_x * razn_y)

count = 0
for x in range(-1000, 1000):
    for y in range(-1000, 1000):
        if y < -x and y < x and y > x - 11 * 2 ** .5 and y > -x - 11 * 2 ** .5:
            count += 1

print(count)

from ipaddress import *
for A in range(255,-1,-1):
    ip_net = ip_network(f'248.112.{A}.35/255.255.255.240', 0)
    if all(f'{ip:b}'[:16].count('0') <= f'{ip:b}'[-16:].count('0') for ip in ip_net):
        print(A)
        break

def fact(n, p=2):
    for i in range(p, int(n**0.5) + 1):
        if n % i == 0: 
            return [i] + fact(n // i, i)
    return [n]
print(fact(18, 2))
