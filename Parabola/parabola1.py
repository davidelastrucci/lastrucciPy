class parabola:
    def __init__(self, tipo = None, p1 = None, p2 = None, p3 = None, p4 = None):
        self.__dati = str(tipo)

        if tipo=="ABC":
                
            self.__a = round(float(p1), 2)
            self.__b = round(float(p2), 2)
            self.__c = round(float(p3), 2)
            self.delta = float(self.__b * self.__b - 4 * self.__a * self.__c)

        elif tipo == "FD":
            self.__xfuoco = round(float(p1), 2)
            self.__yfuoco = round(float(p2), 2)
            self.__ydirettrice = round(float(p3), 2)
            __a= round(float(), 2)
            __b= round(float(), 2)
            __c= round(float(), 2)

            self.delta = float(__b * __b - 4 * __a * __c)
            pass
    
    def equazione(self):
        if self.__dati == "ABC":
            if self.__a == 0:
                pass
                
            elif self.__a > 0:
                if self.__b < 0 and self.__c < 0:
                    return f"l'equazione della parabola è:\n y = {self.__a}x^2 {self.__b}x {self.__c} "

                elif self.__b < 0 and self.__c > 0:
                    return f"l'equazione della parabola è:\n  y = {self.__a}x^2 {self.__b}x + {self.__c} "

                elif self.__c < 0 and self.__b > 0:
                    return f"l'equazione della parabola è:\n  y = {self.__a}x^2 + {self.__b}x {self.__c} "

                else:
                    return f"l'equazione della parabola è:\n  y = {self.__a}x^2 + {self.__b}x + {self.__c} "
                
            elif self.__a < 0:
                if self.__b < 0 and self.__c < 0:
                    return f"l'equazione della parabola è:\n  y = {self.__a}x^2 {self.__b}x {self.__c} "

                elif self.__b < 0 and self.__c > 0:
                    return f"l'equazione della parabola è:\n  y = {self.__a}x^2 {self.__b}x + {self.__c} "

                elif self.__c < 0 and self.__b > 0:
                    return f"l'equazione della parabola è:\n  y = {self.__a}x^2 + {self.__b}x {self.__c} "

                else:
                    return f"l'equazione della parabola è:\n  y = {self.__a}x^2 + {self.__b}x + {self.__c} "

            
            elif self.__dati == "fuocoDiret":
                if self.__a == 0:
                    pass

                      
                             
    def getA(self):
        if self.__dati=="ABC":
            return self.__a

        elif self.__dati=="FD":
            self.__a= 2 * (1 / (self.__xfuoco - self.__ydirettrice))
            return self.__a

    def getB(self):
        if self.__dati=="ABC":
            return self.__b

        elif self.__dati=="FD":
            self.__b = -1 * (self.__yfuoco * (2 * self.__a))
            return self.__b
    
    def getC(self):
        if self.__dati=="ABC":
            return self.__c

        elif self.__dati=="FD":
            self.__c= (- 1 + self.__b * self.__b + 4 * self.__yfuoco)/4 * self.__a
            return self.__c
                
    def fuoco(self):
        if self.__dati == "ABC":
            return f"Fuoco: x= {- self.__b / 2 * self.__a}   y= {(1 - self.delta)/ 4 * self.__a}"
        elif self.__dati == "FD":
            return f"Fuoco: x= {self.__xfuoco}   y= {self.__yfuoco}"


    def direttrice(self):
        if self.__dati == "ABC":
            return f"Direttrice: y= {- (1 + self.delta)/ 4 * self.__a}"
        elif self.__dati == "FD":
            return f"Direttrice: y= {self.__ydirettrice}"


    def vertice(self):
        if self.__dati == "ABC":
            return f"Vertice: x = {- self.__b / 2 * self.__a}   y = {- self.delta / 4 * self.__a}"
        elif self.__dati == "FD":
            return f"Vertice: x = {- self.__b / 2 * self.__a}   y = {- self.delta / 4 * self.__a}"

parabola_abc = parabola("ABC", 2, 3, 4) #tipo dati, a, b,c
parabola_fd = parabola("FD", 2,3,4) #tipo dati, x fuoco, y fuoco, y direttrice

print(parabola_abc.equazione())
print(parabola_abc.direttrice())
print(parabola_abc.fuoco())
print(parabola_abc.vertice())

print(parabola_fd.equazione())
print(parabola_fd.direttrice())
print(parabola_fd.fuoco())
print(parabola_fd.vertice())