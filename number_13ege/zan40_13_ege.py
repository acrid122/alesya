from ipaddress import *


ip1 = ip_address('192.192.0.0') #создание ip-адресов
ip2 = ip_address('192.192.0.1')

print(ip2 > ip1) #Сравнение ip-адресов

#Любой ip-адрес построен как 32-битная цепочка
'''
8 октетов записываются друг за другом без разделений

ip2 > ip1, так как в 10 СС двоичная запись этих ip адресов будет сравниваться также
'''

print(f'{ip1:b}') #двоичная запись

print(ip1, ip2)

print(int(ip1))

#Чтобы найти номер компьютера в сети, следует из числового значения ip-адреса узла вычесть ip-адрес сети

print(int(ip2) - int(ip1)) #номер

#Создание сети

ip_net1 = ip_network('192.192.0.1/255.255.255.0', 0) #либо '192.192.0.1/24' - 24 - количество ведущих единиц.

'''
Второй параметр - strict (по умолчанию True). strict = True обозначает, что я могу создать сеть только на основе адреса сети. Если я передам адрес хоста в этой сети, то будет ошибка.

strict = False обнуляет хостовый компонент, то есть приводит адрес узла к адресу сети -> ошибки не возникает
'''
print(ip_net1)

for i in ip_net1:
    print(i)

#Адрес сети

print(ip_net1[0], ip_net1.network_address)

#Широковещательный адрес

print(ip_net1[-1], ip_net1.broadcast_address)

#Получить только хосты

print(list(ip_net1.hosts()))

#Получение маски сети

print(ip_net1.netmask)

#Получение маски сети

print(ip_net1.hostmask) #wildcard - маска. инвертируемая обычная маска. биты инвертировались

print(len(list(ip_net1))) #количество адресов

print(ip_net1.num_addresses) #количество адресов

print(ip1.packed[0], ip1.packed[1], ip1.packed[2], ip1.packed[3]) #выделить байты

print(ip1 in ip_net1) #проверить, есть ли адрес в сети


ip_net = ip_network('190.202.83.62/255.255.252.0', 0)
print(sum(ip_net[-2].packed[i] for i in range(4)))

ip_net = ip_network('46.29.170.214/255.255.128.0', 0)

for ip in list(ip_net)[-2:0:-1]: #от большего ip к меньшему
    max_oct = max(ip.packed[i] for i in range(4))
    summa = sum(ip.packed[i] for i in range(4) if ip.packed[i] != max_oct)
    if summa == max_oct:
        print(str(ip).replace('.', ''))
        break

for i in range(1, 33):
    ip_net = ip_network(f'84.32.84.32/{i}', 0)
    max_ip = ip_net[-2]
    if f'{max_ip:b}'.count('1') == 19:
        print(i)
        break

ip_net = ip_network('95.24.16.0/255.255.240.0', 0)
sp = []

for ip in list(ip_net)[-2:0:-1]:
    sp.append((f'{ip:b}'.count('1'), ip))

sp.sort(reverse = True)
max_ip = sp[0][1]
print(max_ip)