"""
Um posto está vendendo combustíveis com a seguinte tabela de descontos:

Alcool:

Até 20 litros, desconto de 3%

Acima 20 litros, desconto de 5%

Gasolina:

Até 20 litros, desconto de 4%

Acima 20 litros, desconto de 6%

Escreva um algoritmo que leia o número de litros vendidos e o tipo de combustível (codificado da seguinte forma: A-álcool ou  G-gasolina),
 calcule e imprima o valor a ser pago pelo cliente sabendo-se que o preço do litro da gasolina é R$ 3,30 e o preço do litro do álcool
 é R$ 2,90
"""


def main():
    #declaração de variáveis
    litrosComprados = int()
    combustivel = str()
    preçoGasolina = float()
    preçoAlcool = float()
    menorDescontoA = float()
    maiorDescontoA = float()
    menorDescontoG = float()
    maiorDescontoG = float()

    #entrada de dados
    litrosComprados = int(input("Quantos litros deseja comprar: "))
    combustivel = input("Álcool[A] ou Gasolina[G]? ")

    #processamento de dados
    preçoGasolina = 3.30 * litrosComprados
    preçoAlcool = 2.90 * litrosComprados
    menorDescontoA = preçoAlcool - (0.03 * preçoAlcool)
    maiorDescontoA = preçoAlcool - (0.05 * preçoAlcool)
    menorDescontoG = preçoGasolina - (0.04 * preçoGasolina)
    maiorDescontoG = preçoGasolina - (0.06 * preçoGasolina)

    #saída de dados
    if(litrosComprados <= 20 and combustivel == "A"):
        print(f"{menorDescontoA:.2f}")
    elif(litrosComprados > 20 and combustivel == "A"):
        print(f"{maiorDescontoA:.2f}")
    elif(litrosComprados <= 20 and combustivel == "G"):
        print(f"{menorDescontoG:.2f}")
    else:
        print(f"{maiorDescontoG:.2f}")

    return 0
if __name__ == "__main__":
    main()