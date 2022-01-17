class retta:
    

    def __init__(self, p1=None, p2=None, p3=None):

        self.__a=float(p1)
        self.__b=float(p2)
        self.__c=float(p3)        

    def implicita(self):
        if self.__a == 0:
            return f"\nl'equazione in forma implicita è: \n {self.__b}y + {self.__c} = 0"

        elif  self.__b == 0:
            return f"\nl'equazione in forma implicita è: \n {self.__a}x + {self.__c} = 0"

        elif self.__c == 0:
            return f"\nl'equazione in forma implicita è: \n {self.__a}x + {self.__b} = 0"

        else:
            return f"\nl'equazione in forma implicita è: \n {self.__a}x + {self.__b}y +{self.__c} = 0"

    def esplicita(self):
        k = -self.__c / self.__b
        if self.__b == 0:
            return f"\nl'equazione non può essere scritta in forma esplicita"

        elif self.__a == 0:
            return f"\nl'equazione in forma esplicita è: \n y = {-self.__c  / self.__b}x"
 
        elif self.__c == 0:
            return f"\nl'equazione in forma esplicita è: \n y = {-self.__a  / self.__b}x" 
        
        else:
            if k > 0:
                return f"\nl'equazione in forma esplicita è: \n y = {-self.__a  / self.__b}x + {-self.__c / self.__b}"
            else:
                return f"\nl'equazione in forma esplicita è: \n y = {-self.__a  / self.__b}x {-self.__c / self.__b}"
    
 
    def getA(self):
        return self.__a

    def getB(self):
        return self.__b

    def getC(self):
        return self.__c

    def coefficiente_angolare(self):
        if self.__b==0:
           return f"\nla retta è parallela all'asse y, il coefficiente angolare è indefinito."
        else:
            m = -self.__a / self.__b
            return m

    
    def y(self,x):
        self.__x=float(x)
        if self.__b==0:
            return f"\nla retta è parallela all'asse y"
        elif self.__a==0:
            y=-self.__c/self.__b
            cord_punti=[self.__x,y]
        elif self.__c==0:
            y=-self.__a*self.__x/self.__b
            cord_punti=[self.__x,y]
        else:
            y=-self.__a*self.__b+(-self.__c/self.__b)
            cord_punti=[self.__x,y]
        print("\nle cordinate del punto sono:")
        return cord_punti
            



valori_a_b_c = retta(input("\ninsersisci il valore di a: "), input("insersisci il valore di b: "), input("insersisci il valore di c: "))


print(valori_a_b_c.implicita())
print(valori_a_b_c.esplicita())
print("\nil coefficiente angolare è: ", valori_a_b_c.coefficiente_angolare(), sep ="")
print(valori_a_b_c.y(input("\ninserisci il valore della x = ")))
