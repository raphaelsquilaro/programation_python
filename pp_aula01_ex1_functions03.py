#Author: Raphael Campos Squilaro
#Project: 


def calcular (a, b, op):
    #() -> tuplas - imutável
    #[] -> listas - mutável
    operacoes = {
        '+': a + b,
        '-': a - b,
        '*': a * b,
        '/': a / b,
        '//': a // b,
        '**': a ** b,
        '%': a % b
    }
    return operacoes[op]


n1 = float(input("Digite o primeiro valor: "))
n2 = float(input("Digite o segundo valor: "))
op = input("Escolha a operação[+, -, *, /, //, **, %]: ")

print(calcular(n1, n2, op))