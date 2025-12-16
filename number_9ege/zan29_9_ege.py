from statistics import mean

'''
хорош для IDLE
summa = 0
for i in range(42000): #количество строк из файла
    f = list(map(int, input().split())) #input() - функция ввода с клавиатуры (возвращает строку), .split() - делит по пробелам
    """
    "40 20 40 30" -> после .split() ['40', '20', '40', '30']
    map() - встроенная функция, которая применяет нужную нам функцию (в данном случае int()) к каждому элементу итерируемого объекта ->
    [40, 20, 40, 30]
    
    list() нужен для того, чтобы в случае необходимости удобно выводить на экран части или весь список чисел. map() возвращает так называемый
    map-object, который в консоли выводится плохо (не дает никакой информации)
    """
    povt = [i for i in f if f.count(i) == 3]
    nepovt = [i for i in f if f.count(i) == 1]
    if len(povt) == 3 and len(nepovt) == 4:
        sr_nepovt = mean(nepovt)
        if sr_nepovt <= povt[0]:
            summa = sum(f)
print(summa)
'''

with open('9_1.txt') as f:
    summa = 0
    for i in f:
        s = list(map(int, i.split()))
        povt = [i for i in s if s.count(i) == 3]
        nepovt = [i for i in s if s.count(i) == 1]
        if len(povt) == 3 and len(nepovt) == 4:
            sr_nepovt = mean(nepovt)
            if sr_nepovt <= povt[0]:
                summa = sum(s)
    print(summa)


with open('9_2.txt') as f:
    count = 0
    for i in f:
        s = list(map(int, i.split()))
        povt = [i for i in s if s.count(i) == 3]
        nepovt = [i for i in s if s.count(i) == 1]
        if len(povt) == 3 and len(nepovt) == 3:
            if max(s) ** 2 + min(s) ** 2 >= (sum(s) - max(s) - min(s)) ** 2:
                count += 1
    print(count)


with open('9_3.txt') as f:
    count = 0
    for i in f:
        s = list(map(int, i.split()))
        povt_3 = [i for i in s if s.count(i) == 3]
        povt_2 = [i for i in s if s.count(i) == 2]
        nepovt = [i for i in s if s.count(i) == 1]
        if len(povt_3) == 3 and len(povt_2) == 2 and len(nepovt) == 2:
            if max(povt_3 + povt_2) > max(nepovt):
                count += 1
    print(count)

with open('9_4.txt') as f:
    count = 0
    for i in f:
        s = list(map(int, i.split()))
        tr = [i for i in s if 99 < abs(i) < 1000] #беру модуль, чтобы проверять еще и отрицательные числа
        if len(tr) >= len(s) / 2:
            kr_5 = [i for i in s if i % 5 == 0]
            if len(kr_5) == 0:
                count += 1
    print(count)

    