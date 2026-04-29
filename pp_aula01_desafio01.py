#Author: Raphael Campos Squilaro
#Project: Functions for simple and compound interest

def juros_simples(p, i, t):
    return p * (i / 100) * t

def juros_compostos(p, i, t):
    montante = p * (1 + i / 100) ** t
    return montante - p

valor = float(input("Digite um valor: "))
juros = int(input("Digite um número para os juros: "))
tempo = int(input("Digite o tempo (em meses/anos): "))
decisao = input("Digite qual tipo de juros você quer usar: ")

if "simples" in decisao.lower():
    resultado = juros_simples(valor, juros, tempo)
    print(f"O valor dos juros simples é: R$ {resultado:.2f}")
    print(f"Montante Total (Capital + Juros): R$ {valor + resultado:.2f}")
elif "composto" in decisao.lower():
    resultado = juros_compostos(valor, juros, tempo)
    print(f"O valor dos juros compostos é: R$ {resultado:.2f}")
    print(f"Montante Total (Capital + Juros): R$ {valor + resultado:.2f}")
else:
    print("Tipo de juros inválido.")
