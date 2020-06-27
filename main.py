from calc import Calculadora
from geo import Geometria

menup = ('''SUB - Linguagem de Programação - Menu Inicial
[1] - Menu Calculadora
[2] - Menu Geometria
[0] - Sair do programa ''')
menuc = ('''SUB - Linguagem de Programação - Menu Calculadora
[1] - Somar
[2] - Subtrair
[3] - Multiplicar
[4] - Dividir
[0] - Retorna ao menu anterior ''')
menug = ('''SUB - Linguagem de Programação - Menu Geometria
[1] - Identificar triângulo
[2] - Área do Triângulo
[3] - Área do Retângulo
[4] - Perímetro do Retângulo
[0] - Retorna ao menu anterior ''')
opção = 1
while opção != 0:   # Menu inicial
    print(menup)
    opção = int(input())
    if opção==0:
        print('Sair do programa')
        break
    elif opção==1:  # Menu calculadora
        cal=1
        while cal !=0:
            print(menuc)
            cal = int(input())
            if cal == 1:    # Somar
                A = int(input('Informe o primeiro numero '))
                B = int(input('Informe o segundo numero '))
                mycalc = Calculadora(A,B)
                r = mycalc.somar()
                print('A soma dos numeros digitados é {} \n'.format(r))
            elif cal == 2:  # Subtrair
                A = int(input('Informe o primeiro numero '))
                B = int(input('Informe o segundo numero '))
                mycalc = Calculadora(A,B)
                r = mycalc.subtrair()
                print('A diferença entre os numeros digitados é {} \n'.format(r))
            elif cal == 3:  # Multiplicar
                A = int(input('Informe o primeiro numero '))
                B = int(input('Informe o segundo numero '))
                mycalc = Calculadora(A,B)
                r = mycalc.multiplicar()
                print('A multiplicação entre os numeros digitados é {} \n'.format(r))
            elif cal == 4:  # Dividir
                A = int(input('Informe o primeiro numero '))
                B = int(input('Informe o segundo numero '))
                mycalc = Calculadora(A,B)
                r = mycalc.dividir()
                print('A divisão do primeiro numero digitado pelo segundo numero é {} \n'.format(r))
            else:
                print('Opção inválida! Escolha uma opção válida no menu \n')
    elif opção==2: # Menu geometria
        geo=1
        while geo !=0:
            print(menug)
            geo = int(input())
            if geo == 1:    # Identificar triangulo
                X=int(input('Informe a medida do primeiro lado do triangulo '))
                Y=int(input('Informe a medida do segundo lado do triangulo '))
                Z=int(input('Informe a medida do terceiro lado do triangulo '))
                triangulo = Geometria(X,Y,Z)
                triangulo.identificarTriangulo()
            elif geo == 2:  # Calcular area triangulo
                X=int(input('Informe a medida da base do triangulo '))
                Y=int(input('Informe a medida da altura do triangulo '))
                Z=2
                triangulo = Geometria(X,Y,Z)
                r = triangulo.calcularAreaTriangulo()
                print('A área deste triangulo é {} \n'.format(r))
            elif geo == 3:  # Calcular area retangulo
                X=int(input('Informe a medida da base do retangulo '))
                Y=int(input('Informe a medida da altura do retangulo '))
                Z=1
                triangulo = Geometria(X,Y,Z)
                r = triangulo.calcularAreaRetangulo()
                print('A área deste retangulo é {} \n'.format(r))
            elif geo == 4:  # Calcular perimetro retangulo
                X=int(input('Informe a medida da base do retangulo '))
                Y=int(input('Informe a medida da altura do retangulo '))
                Z=2
                triangulo = Geometria(X,Y,Z)
                r = triangulo.calcularPerietroRetangulo()
                print('O perímetro deste retangulo é {} \n'.format(r))
            else:
                print('Opção inválida! Escolha uma opção válida no menu \n')
    else:
        print('Opção inválida! Escolha uma opção válida no menu \n')