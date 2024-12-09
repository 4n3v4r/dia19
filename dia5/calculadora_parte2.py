#Calculadora

def adicao(x,y):
    return x + y

def subtracao(x,y):
    return x - y

def multiplicacao(x,y):
    return x * y

def divisao(x,y):
    return x / y

def calculadora ():
    print("Selecione operação")
    print("1 - Adição")
    print("2 - Subtração")
    print("3 - Multiplicação")
    print("4 - Divisão")

while True:
    calculadora()
    escolha = input("Escolha(1/2/3/4): ")
    
    if escolha in ("1", "2", "3", "4"):
        x = float(input("Digite o 1º Numero: "))
        y = float(input("Digite o 2º Numero: "))
        if escolha == "1":
            print("Resultado = ", adicao(x,y))
        if escolha == "2":
            print("Resultado = ", subtracao(x,y))
        if escolha == "3":
            print("Resultado = ", multiplicacao(x,y))
        if escolha == "4":
            if y != 0:
                print("Resultado = ", divisao(x,y))
            else:
                print("Não é possivel divisao por zero")
    else:
        print("Escolha invalida")

    continuar = input("Deseja continuar? (s / n): ")
    if continuar == "n":
        print("Fechar calculadora")
        break;
    
calculadora()
