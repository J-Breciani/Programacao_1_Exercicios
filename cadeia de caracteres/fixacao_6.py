"""
Faça um programa que leia uma palavra e verifique se ela é um palíndromo.

Palíndromo é uma palavra ou frase que permanece igual quando lida de trás para frente.
"""
def main():

    # declaração de variáveis: 
    palavra = str()

    # entrada e processamento de dados:
    palavra = input(" ").upper()

    # processamento e saída de dados:
    if palavra == palavra[::-1]:
        print(f"{palavra} É UM PALÍNDROMO")
    else:
        print(f"{palavra} NÃO É UM PALÍNDROMO")




    return 0 

if __name__ == "__main__":
    main()