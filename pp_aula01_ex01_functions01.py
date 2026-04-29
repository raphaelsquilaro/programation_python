#Author: Raphael Campos Squilaro
#Project: functions

#variáveis globais do sistema - pode ser utilizada em todo o sistema
valor1 = float(input("Digite o 1° valor: "))
valor2 = float(input("Digite o 2° valor: "))

#creating a function for calculation
def calcular(v1, v2):
    #variaveis locais - utilizadas dentro desta função
    soma = v1 + v2
    subtracao = v1 - v2
    multiplicacao = v1*v2
    divisao = v1 / v2
    return soma, subtracao, multiplicacao, divisao

def imprimir(s, sub, m, d):
    print("A soma é de: " , s)
    print("A subtração é de: " , sub)
    print("A multiplicação é de: " , m)
    print("A divisão é de: " , d)

# Execução do sistema
res_soma, res_sub, res_mult, res_div = calcular(valor1, valor2)
imprimir(res_soma, res_sub, res_mult, res_div)