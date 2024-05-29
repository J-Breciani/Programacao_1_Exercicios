"""
Faça um programa que leia três número e, a partir de uma função, informe o resultado da soma, dos mesmos.
"""
def f_soma(a,b,c):
    s = a + b + c # processamento da função
    return s

def main():

    # declaração de variáveis

    numero_1 = int()
    numero_2 = int()
    numero_3 = int()
    soma = int()

    # entrada de dados
    numero_1 = int(input(""))
    numero_2 = int(input(""))
    numero_3 = int(input(""))

    # processamento
    soma = f_soma(numero_1, numero_2, numero_3)
    # saída de dados
    print(soma)
    return 0

if __name__ == "__main__":
    main ()