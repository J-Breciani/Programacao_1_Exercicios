"""
Faça um algoritmo que leia a idade de uma pessoa expressa em anos, meses e dias e escreva a idade dessa pessoa expressa apenas em dias. 
Considerar ano com 365 dias e mês com 30 dias.
"""


def main():

    # declaração de variáveis

    anos = int()
    meses = int()
    dias = int()
    total = int()

    # entrada dos dados

    anos = int(input("Idade em anos: "))
    meses = int(input("Idade em meses: "))
    dias = int(input("Idade em dias: "))

    # processamento 

    total = (anos * 365) + (meses * 30) + dias

    # saída

    print(total)

    return 0 

if __name__ == "__main__":
    main()