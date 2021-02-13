from math import sqrt

class Parabola:
    def __init__(self, k1, k2, k3):
        self.a = k1
        self.b = k2
        self.c = k3
        self.can = self.iscan()
        self.vertex()
        self.make()

    def dd(self):
        res = self.b ** 2 - 4 * self.a * self.c
        return res

    def make(self):
        if self.a != 0:
            self.iskorni = True
            self.make_parabola()
        if self.a == 0:
            if self.b == 0:
                self.D = False
                self.vertex_x = False
                self.vertex_y = False
                self.iskorni = False
                self.x_1 = False
                self.x_2 = False
            else:
                self.iskorni = True
                self.D = False
                self.vertex_x = False
                self.vertex_y = False
                self.make_line()

    def make_parabola(self):
        self.D = self.dd()
        if self.D == 0:
            self.x_1 = -1*self.b / 2
            self.x_2 = False
        elif self.D > 0:
            self.x_1 = (-1 * self.b - sqrt(self.D))/(2*self.a)
            self.x_2 = (-1 * self.b + sqrt(self.D))/(2*self.a)
        else:
            self.x_1, self.x_2 = False, False
    def make_line(self):
        self.x_1 = -1*self.c / self.b
        self.x_2 = False
        

    def vertex(self):
        if self.a != 0:
            self.vertex_x = (-1 * self.b)/(2 * self.a)
            self.vertex_y = (self.b**2 - 4 * self.a*self.c)/(4 * self.a)
        else:
            self.vertex_x, self.vertex_y  = False, False
        
    def knowY(self, x):
        if type(x) == bool:
            return(False)
        else:
            y = self.a * x**2 + self.b * x + self.c
        return(y)

    def iscan(self):
        if self.a != '' and self.b != '' and self.c != '':
            can = True
        else:
            can = False
        return(can)