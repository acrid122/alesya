def f(x, y, d):
    if x == y:
        return 1
    if x > y or x == 30:
        return 0
    return f(x + d, y, d) + f(x * 2, y, d)
count = 0
for d in range(1, 101):
    count += f(1, 10, d) * f(10, 100, d)
print(count)
'''
Исполнитель преобразует число на экране.

У исполнителя есть три команды, которые обозначены латинскими буквами:

A. Прибавить 2

B. Возвести в квадрат

C. Умножить на 3

Программа для исполнителя – это последовательность команд.

Сколько существует программ, для которых при исходном числе 2 результатом является число 64, если после выполнения команды B можно выполнить только команду A или C?
'''

def f1(x, y, last):
    if x == y:
        return 1
    if x > y:
        return 0
    if last == 1: #B
        return f1(x + 2, y, 0) + f1(x * 3, y, 2)
    else:
        return f1(x + 2, y, 0) + f1(x * 3, y, 2) + f1(x ** 2, y, 1)
print(f1(2,64,67)) 

    
def f2(x, y, cnt):
    if x > y or cnt > 1:
        return 0
    if x == y and cnt == 1:
        return 1
    return f2(x + 1, y, cnt) + f2(x + 2, y, cnt) + f2(x * 2, y, cnt + 1)
print(f2(2, 12, 0))