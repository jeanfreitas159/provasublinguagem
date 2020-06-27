class Calculadora():

    def __init__(self,numero1,numero2):
        self.n1 = numero1
        self.n2 = numero2
                
    def somar(self):
        resultado = self.n1 + self.n2
        return resultado
            
    def subtrair(self):
        resultado = self.n1 - self.n2
        return resultado

    def multiplicar (self):
        resultado = self.n1 * self.n2
        return resultado

    def dividir (self):
        resultado = self.n1 / self.n2
        return resultado
