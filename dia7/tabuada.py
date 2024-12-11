# tabuada

def tabuada(num):
    print(f"Tabuada do {num}")
    for i in range(1, 11):
        resultado = num * i
        print(f"{num} * {i} = {resultado}")
        
#solicitar o numero
num = int(input("Digite um numero: "))
    
#vamos chamar a funcao
tabuada(num)

        