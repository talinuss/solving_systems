from math import sqrt
from parabola import Parabola as Pb
from tkinter import *

def create_labels():
    names = ['a', 'b', 'c', 'D', 'x1', 'x2', 'Вершины ', 'x', 'y' ]
    for j in range(2):
        for i in range(0, len(names)):
            couple = []
            couple.append(Label(window, text = names[i]))
            couple.append(Entry(window))
            interface[j].append(couple)
    return(interface)
           
def placing(x, g):
    answer_lb.grid(column = 0, row = 21, rowspan = 4, columnspan = 2)
    r = 0
    for i in range(0, len(interface[x])):
        interface[x][i][0].grid(column = 0, row = r + g)
        interface[x][i][1].grid(column = 1, row = r + g)
        if i >= 3:
            interface[x][i][1]['state'] = DISABLED
        r += 1

def get_data(a, b, c):    
    if a.get() == '' or b.get() == '' or c.get() == '':
        can = False
        text1, text2, text3 = 0, 0, 0
    else:
        can = True
        text1 = float(a.get())
        text2 = float(b.get())
        text3 = float(c.get())
    return(can, text1, text2, text3)

def clearing(name):
    name['state'] = NORMAL
    name.delete(0, END)
    name['state'] = DISABLED

def enabliding(name, value):
    name['state'] = NORMAL
    name.delete(0, END)
    name.insert(0, str(value))
    name['state'] = DISABLED

def objects():
    global usl
    usl =[]
    for k in range(2):   
        can, a, b, c = get_data(interface[k][0][1], interface[k][1][1], interface[k][2][1])
        usl.append(can)
        if usl[k]: 
            par = Pb(a, b, c)
            interface[k].insert(9, par)
    return(usl)

def clicked():
    pole.delete('parabola')
    objects()
    system_solving(interface)
    global usl
    for k in range(2):
        for j in interface[k][3:]:
            if type(j) == list :
                clearing(j[1])             
    for k in range(2):
        if usl[k]:
            par = interface[k][9]
            enabliding(interface[k][3][1], par.D)
            enabliding(interface[k][4][1], par.x_1)
            enabliding(interface[k][5][1], par.x_2)
            enabliding(interface[k][6][1], 'Параболы:')
            enabliding(interface[k][7][1], par.vertex_x)
            enabliding(interface[k][8][1], float(par.vertex_y * -1))
            build_graf(par)

def build_graf(par):
    global mash
    i = 0
    half_osi_x = int(pole['width']) / 2
    half_osi_y = int(pole['height']) / 2
    while i<int(pole['width'])/mash:
        x1 = i - half_osi_x / mash
        y1 = par.knowY(x1)
        x2 = (i + 0.1) - half_osi_x / mash
        y2 = par.knowY(x2)
        pole.create_line(x1 * mash + half_osi_x, y1 * mash * -1 + half_osi_x, x2 * mash + half_osi_x, y2 * -1 * mash + half_osi_x, fill = 'black', width = 2, tags = 'parabola')
        i+=0.1

def osi():
    global mash
    half_osi_x = int(pole['width']) / 2
    half_osi_y = int(pole['height']) / 2
    
    #ОСИ Y
    pole.create_line(half_osi_x, 0, half_osi_x, half_osi_y*2, fill = 'red', width = 2, tag = 'osi')     #y
    a = mash
    for i in range(int(half_osi_y*2 / mash)):  #линии на оси Y
        i += 1
        pole.create_line(0, a, half_osi_x*2, a, fill = 'yellow', width = 1)
        a += mash
    a = mash
    for i in range( int( half_osi_y / mash) - 1):  #цифры на оси Y сверху
        i += 1
        pole.create_text(half_osi_x - 8, a, justify = CENTER, text =str(int(half_osi_y / mash - i)), font = 'Times 7')
        a += mash
    a = half_osi_y + mash
    for i in range( int( half_osi_x / mash) - 1):  #цифры на оси Y снизу
        i += 1
        pole.create_text(half_osi_x - 8, a, justify = CENTER, text = '-' + str(i), font = 'Times 7')
        a += mash

    #ОСИ X
    pole.create_line(0, half_osi_y, half_osi_x * 2, half_osi_y, fill = 'red', width = 2, tag = 'osi')   #x
    a = mash
    for i in range(int(half_osi_x*2 / mash)):  #линии на оси X
        i += 1
        pole.create_line(a, 0, a, half_osi_y*2 + 3, fill = 'yellow', width = 1)
        a += mash
    a = mash
    for i in range( int( half_osi_x / mash) - 1):  #цифры на оси X слева
        i += 1
        pole.create_text(a, half_osi_y + 8, justify = CENTER, text ='-' +  str(int(half_osi_y / mash - i)), font = 'Times 7')
        a += mash
    a = half_osi_x + mash
    for i in range( int( half_osi_x / mash) - 1):  #цифры на оси X справа
        i += 1
        pole.create_text(a, half_osi_y + 8, justify = CENTER, text = str(i), font = 'Times 7')
        a += mash

def system_solving(interface):
    if interface[0][9].can and interface[1][9].can:
        a1, a2, b1, b2, c1, c2 = interface[0][9].a, interface[1][9].a, interface[0][9].b, interface[1][9].b, \
        interface[0][9].c, interface[1][9].c
        a, b, c = a1 - a2, b1 - b2, c1 - c2
        par = Pb(a, b, c)
        if a == 0 and b == 0 and c == 0:
            answer = 'Одинаковые графики'
        elif Pb(a, b, c).D < 0:
            answer = 'Нет решений'
        else:
            x1 = par.x_1
            x2 = par.x_2
            y1 = interface[0][9].knowY(x1)
            y2 = interface[0][9].knowY(x2)
            answer = 'x_1: ' + str(round(x1, 2)) + '\n' + 'y_1: ' +  str(round(y1, 2)) + '\n' + 'x_2: ' \
            + str(round(x2, 2)) + '\n' +  'y_2: ' +  str(round(y2, 2))
        if 'answer' in locals():
            answer_lb['text'] = answer
            print(answer)
    else:
        answer_lb['text'] = ''                    
def knowY(x, a, b, c):
        y = a * x**2 + b * x + c
        return(y)

window = Tk()
window.geometry('1170x1020')
window.title('Parabola')

interface = [[], []]
create_labels()
answer_lb = Label(window)
placing(0, 0)
Label(text = '------------------------------------').grid(column = 0, row = 9, columnspan = 2)
placing(1, 10)
btn = Button(window, text = 'рассчитать', command = clicked, width = 20)
btn.grid(column = 0, row = 20, columnspan = 2)

global pole
global mash
mash = 25

pole = Canvas(window, width = 1000, height = 1000, bg = 'white')
pole.place(x=200, y = 5)

osi()

window.mainloop()