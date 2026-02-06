from ipaddress import *

ip1 = ip_address('192.192.30.21') #создание ip-адреса
ip2 = ip_address('192.192.30.22') 

print(ip2 > ip1) #сравнение ip-адресов

#Любой ip-адрес представляет из себя не только 32-битную цепочку, но и целочисленное значение

print(int(ip1)) #3233816085 - 32-битная запись в 10СС

#Чтобы найти номер компьютера в сети, следует из числового значения ip-адреса узла вычесть ip-адрес сети.

ip2_net = ip_address('192.192.30.0')

print(int(ip2) - int(ip2_net))

#Как перевести ip-адрес в 2 СС

print(f'{ip2:b}')

#Создание сети

ip_net1 = ip_network('192.192.30.0/255.255.255.0') #первая вариация, где создание сети происходит с ip-адресом сети

ip_net2 = ip_network('192.192.30.22/255.255.255.0', 0) #обнуление хостового компонента

'''
Второй параметр - strict (по умолчанию равен True). strict = True обозначает, что можно передать в качестве адреса только адрес сети.

Если передать адрес узла, то будет ошибка.

strict = False обнуляет хостовый компонент, то есть приводит адрес узла к адресу сети -> ошибка не возникает
'''

print(ip_net2) #24 - количество ведущих единиц. префикс маски

'''
ip_network('192.192.30.21/24', 0)
'''

for ip in ip_net2:
    print(ip)

#Адрес сети

print(ip_net1[0], ip_net1.network_address)

#Широковещательный адрес

print(ip_net1[-1], ip_net1.broadcast_address)

#Получить ip-адреса только хостов

print(list(ip_net1.hosts()))

print(list(ip_net1)[1:-1])

#Получение маски сети

print(ip_net1.netmask) #wildcard - маска, инвертируемая маска сети. 
print(ip_net1.hostmask)

#Количество адресов в сети

print(len(list(ip_net1)))

print(len(list(ip_net1.hosts())) + 2)

print(ip_net1.num_addresses)

#Выделить байты ip-адреса

#ip2 = ip_address('192.192.30.22') 

print(ip2.packed[0], ip2.packed[1], ip2.packed[2], ip2.packed[3])

#Проверить, есть ли адрес в сети

print(ip2 in ip_net1)


ip_net1 = ip_network('190.202.83.62/255.255.252.0', 0)
max_ip = ip_net1[-2]
print(sum(max_ip.packed[i] for i in range(4)))

ip_net2 = ip_network('46.29.170.214/255.255.128.0', 0)
for ip in list(ip_net2)[-2:0:-1]:
    max_oct = max(ip.packed[i] for i in range(4))
    summa = sum(ip.packed[i] for i in range(4))
    if summa - max_oct == max_oct:
        print(str(ip).replace('.', ''))
        break

for x in range(1, 33):
    ip_net3 = ip_network(f'84.32.84.32/{x}', 0)
    if f'{ip_net3[-2]:b}'.count('1') == 19:
        print(x)
        break

sp = []
ip_net4 = ip_network('95.24.16.0/255.255.240.0', 0)
for ip in list(ip_net4)[1:-1]:
    sp.append((f'{ip:b}'.count('1'), ip))

sp.sort(reverse = True)
max_ip = sp[0][1]
print(max_ip.packed[2] + max_ip.packed[3])