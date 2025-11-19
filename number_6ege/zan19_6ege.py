from turtle import *

#fd(number) - вперед
#bk(number) - назад
#lt(number) - поворот налево
#rt(number) - поворот направо
#dot(size, color) - поставить точку
#goto(xcor, ycor) - перемещение на соответствующую координату
#up() - поднять хвост
#down() - опустить хвост
#tracer(seconds) - ускоряет движение. tracer(0) - моментальная отрисовка
#screensize(width, heigth) - изменение размера холста
#done() - завершение/фиксация рисунка на холсте
#update() - обновление экрана черепахи
#pos() - позиция черепашки относительно начала координат
#xcor() - получение абсциссы координаты
#ycor() - получение ординаты координаты
#heading() - получение угла поворота относително начала координат
'''
tracer(0)
lt(90)
m = 10
for _ in range(8):
    fd(22 * m)
    rt(90)
    fd(33 * m)
    rt(90)
up()
bk(8 * m)
rt(90)
fd(11 * m)
lt(90)
down()
for _ in range(8):
    fd(73 * m)
    rt(90)
    fd(62 * m)
    rt(90)
update()
done()

tracer(0)
lt(90)
m = 10
for _ in range(8):
    fd(16 * m)
    rt(90)
    fd(22 * m)
    rt(90)
up()
fd(5 * m)
rt(90)
fd(5 * m)
lt(90)
down()
for _ in range(8):
    fd(52 * m)
    rt(90)
    fd(77 * m)
    rt(90)
up()
for x in range(-50, 50):
    for y in range(-50, 50):
        goto(x * m, y * m)
        dot(3, 'red')
update()
done()
'''
tracer(0)
lt(90)
m = 10
for _ in range(4):
    fd(30 * m)
    rt(90)
    fd(48 * m)
    rt(90)
up()
fd(27 * m)
rt(90)
fd(24 * m)
lt(90)
down()
for _ in range(4):
    fd(29 * m)
    rt(90)
    bk(18 * m)
    rt(90)
up()
for x in range(-50, 50):
    for y in range(-50, 50):
        goto(x * m, y * m)
        dot(3, 'red')
update()
done()