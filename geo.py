class Geometria():
    def __init__(self,M1,M2,M3):
        self.l1 = M1
        self.l2 = M2
        self.l3 = M3

    def identificarTriangulo(self): # Verificação de lados de um triângulo
        X=self.l1
        Y=self.l2
        Z=self.l3
        if X <0:
            print('Erro, você digitou um valor negativo \n')
        elif Y<0:
            print('Erro, você digitou um valor negativo \n')
        elif Z<0:
            print('Erro, você digitou um valor negativo \n')    
        elif X>(Y+Z):
            print('Estas medidas não correspondem a um triângulo \n')
        elif Y>(X+Z):
            print('Estas medidas não correspondem a um triângulo \n')
        elif Z>(X+Y):
            print('Estas medidas não correspondem a um triângulo \n')
        elif X==Y==Z:
            print('Estas medidas são de um triângulo Equilátero \n')
        elif X!=Y!=Z:
            print('Estas medidas são de um triângulo Escaleno \n')
        else:
            print('Estas medidas são de um triângulo Isósceles \n')     
            
    def calcularAreaTriangulo(self):
        resultado = (self.l1 * self.l2)/self.l3
        return resultado

    def calcularAreaRetangulo(self):
        resultado = (self.l1 * self.l2)/self.l3
        return resultado

    def calcularPerietroRetangulo(self):
        resultado = (self.l1 + self.l2)*self.l3
        return resultado