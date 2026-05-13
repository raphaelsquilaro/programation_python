#Author: Raphael Campos Squilaro
#Project: functions

def calcular(opala, mecanico, chevette):
    #CUIDADO!!!
    # eval - executa expressão em um texto (String)
    return eval (f"{opala}{mecanico}{chevette}")

n1 = float(input("Digite o primeiro valor: "))
n2 = float(input("Digite o segundo valor: "))
op = input("Escolha a operação[+, -, *, /]: ")

print("O resultado é: " , calcular(n1, op, n2))
