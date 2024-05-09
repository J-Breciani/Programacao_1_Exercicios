"""
Escreva um programa para ler um valor INTEIRO e escreva seu antecessor.

"""


def main():

    # declaração de variáveis

    numero = int()
    antecessor = int()

    # entrada dos dados

    numero = int(input("X: "))

    # processamento 

    antecessor = numero - 1

    # saída

    print(antecessor)

    return 0 

if __name__ == "__main__":
    main()