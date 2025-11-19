""" from turtle import *
tracer(0)
lt(90)
m = 10
for _ in range(2):
    fd(14 * m)
    lt(270)
    bk(12 * m)
    rt(90)
up()
fd(9 * m)
rt(90)
bk(7 * m)
lt(90)
down()
for _ in range(2):
    fd(13 * m)
    rt(90)
    fd(6 * m)
    rt(90)
up()
for x in range(-50, 50):
    for y in range(-50, 50):
        goto(x * m, y * m)
        dot(3, 'red')

update()
done()
 """
from turtle import *
tracer(0)
m = 10
lt(90)
for _ in range(3):
    fd(39 * m)
    rt(90)
    fd(48 * m)
    rt(90)
up()
fd(27 * m)
rt(90)
fd(24 * m)
lt(90)
down()
for _ in range(3):
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

