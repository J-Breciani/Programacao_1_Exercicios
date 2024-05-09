"""
Faça um programa que leia dois números
inteiros e apresente o resultado de sua soma e multiplicação:

"""
def main():

    # declaração de variáveis

    numero_1 = int()
    numero_2 = int()
    soma = int()
    multiplicacao = int()

    # entrada de dados

    numero_1 = int(input("Primeiro número: "))
    numero_2 = int(input("Segundo número: "))

    # processamento dos dados

    soma = numero_1 + numero_2
    multiplicacao = numero_1 * numero_2

    # saída de dados

    print(soma, multiplicacao)

    return 0 

if __name__ == "__main__":
    main()