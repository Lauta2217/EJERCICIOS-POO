class Fraccion:
    def __init__(self, numerador:int, denominador:int):
        self.numerador = numerador
        self.denominador = denominador
    
    def __str__(self) -> str:
        return str(self.numerador) + "/" + str(self.denominador)
    
    def __add__(self, a:int):
        return Fraccion((self.numerador + a), self.denominador)
    
    def __radd__(self , a:int):
        return self.__add__(a)
    
    def __mul__(self, a:int):
        return Fraccion(self.numerador * a, self.denominador)
    
    def __rmul__(self, a:int):
        return self.__mul__(a)
    
    def __div__(self, a:int):
        return Fraccion(self.numerador, (a * self.denominador))
    
    def __rdiv__(self, a:int):
        return self.__div__(a)
    
    def __truediv__(self, a: int):
        return Fraccion(self.numerador, a * self.denominador)

    def __rtruediv__(self, a: int):
        return self.__truediv__(a)
    
    def calcular_fraccion(self):
        return self.numerador / self.denominador
    
    def __eq__(self, otra):
        return self.calcular_fraccion() == otra.calcular_fraccion()
    
    def __gt__(self, otra):
        return self.calcular_fraccion() > otra.calcular_fraccion()
    
    def __it__(self, otra):
        return self.calcular_fraccion() < otra.calcular_fraccion()
        
def main():
    f = Fraccion(5, 2)
    print(f + 2)
    print(3 + f)
    print(f * 2)
    print(3 * f)
    print(f / 2)
    print(f == Fraccion(10, 4))
    print(f > Fraccion(11, 4))
    print(f > Fraccion(9, 4))
    
    
main()