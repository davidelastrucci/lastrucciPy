class retta:

    def __init__(self, p1=None, p2=None, p3=None):

        self.__a=float(p1)
        self.__b=float(p2)
        self.__c=float(p3)
        self.__punti=[]


    def implicita(self):
        if self.__a==0:
            return f"\n1'equazione in forma implicita è: \n {self.__b} y+{self.__c}=0"
        elif  self.__b==0:
            return f"\n1'equazione in forma implicita è: \n {self.__a} x+{self.__c}=0"
        elif self.__c==0:
            return f"\n1'equazione in forma implicita è: \n {self.__a} x+{self.__b}=0"
        else:
            return f"\n1'equazione in forma inplicita è: \n {self.__a} x+{self.__b} y+{self.__c}=0"


    def esplicita(self):
        if self.__b==0:
            return f"\n1'equazione puo essere scritta in forma esplicita"
        elif self.__a==0:
            return f"\n1'equazione in forma esplicita è: \n y={-self.__c / self.__b }x"
        elif self.__c==0:
            return f"\n1'equazione in forma esplicita è: \n y={-self.__a / self.__b} x"
        else:
            return f"\n1'equazione in forma esplicita è: \n y={-self.__a / self.__b} x+{-self.__c / self.__b}"

 
    def getA(self):
        return f"\n a={self.__a}"

    def getB(self):
        return f"\n b={self.__b}"

    def getC(self):
        return f"\n c={self.__c}"

    def coefficiente_angolare(self):
        if self.__b==0:
            return f"\nla retta è parallela all'asse y \nil coefficiente non è determinato"
        else:
            return f"\nil coefficiente angolare dell'equazione è {-self.__a / self.__b}"
    
    def y(self,x):
        self.__x=float(x)
        if self.__b==0:
            return f"\nla retta è parallela all'asse y"
        elif self.__a==0:
            return f" y={-self.__c / self.__b}"
        elif self.__c==0:
            return f" y={-self.__a * self.__x / self.__b}"
        else:
            return f" y={-self.__a * self.__b + (-self.__c / self.__b)}"
            
valori_a_b_c = retta(input("\ninresisci il valore di a: "), input("inresisci il valore di b: "), input("inresisci il valore di c: "))

print(valori_a_b_c.implicita())
print(valori_a_b_c.esplicita())
print(valori_a_b_c.coefficiente_angolare())
