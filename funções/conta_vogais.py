"""
Faça um programa, em Python 3.x, que receba strings e informe, a partir de uma função, escreva uma nova STRING SEM as VOGAIS. 
Apresente a nova string. A condição de parada é quando for informada uma string vazia ("").
"""

def f_vogal (letra):
    if (letra == "A" or letra == "E" or letra == "I" or letra == "O" or letra == "U"):
        return True
    else:
        return False

def f_semVogal(exemplo):
    # declaração:
    palavra = str()
    # entrada de dados:
    palavra = ""
    # processamento:
    for i in range(len(exemplo)):
        if (not f_vogal(exemplo[i])):
            palavra += exemplo[i]
    return palavra

def main():
    # declaração de variáveis:
    a = str()
    # entrada de dados:
    a = input("").upper()
    while (a != ""):
        print(f_semVogal(a))
        a = input().upper()
    return 0

if __name__ == "__main__":
    main()