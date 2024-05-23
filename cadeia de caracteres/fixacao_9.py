"""
Faça um programa que leia o nome de cinco pessoas e informe a quantidade de caracteres que o nome tem.
"""
def main():

    # declaração de variáveis: 
    nome = str()
    cont = int()

    # entrada, processamento e saída:
    for i in range(5):
        nome = input(" ").upper()
        cont = len(nome)
        print(f"{nome} tem {cont} letras")

    return 0 

if __name__ == "__main__":
    main()