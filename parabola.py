from math import sqrt

class Parabola:
    def __init__(self, k1, k2, k3):
        self.a = k1
        self.b = k2
        self.c = k3
        self.D = self.dd()
        if self.D < 0:
            self.iskorni = False
        else:
            self.iskorni = True
        if self.iskorni:
            self.x1 = self.korni1()
            self.x2 = self.korni2()
        self.vertex()
    def dd(self):
        res = self.b ** 2 - 4 * self.a * self.c
        return res

    def korni1(self):
        if self.a != 0:    
            res1=(-1 * self.b + sqrt(self.D))/(2*self.a)
            return(res1)
        else:
            res1=((self.c * -1)/self.b)
            return(res1)

    def korni2(self):
        if self.a != 0:    
            res2=(-1 * self.b - sqrt(self.D))/(2*self.a)
            return(res2)
        else:
            res2=((self.c * -1)/self.b)
            return(res2)
    
    def vertex(self):
        if self.a >0:
            self.vertex_x = (-1 * self.b)/(2 * self.a)
            self.vertex_y = (self.b**2 - 4 * self.a*self.c)/(4 * self.a)
        else:
            self.vertex_x = 0
            self.vertex_y = 0
        

    def knowY(self, x):
        y = self.a * x**2 + self.b * x + self.c
        return(y)