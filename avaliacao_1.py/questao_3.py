"""
Um número de Armstrong é um número de N dígitos onde a soma de cada dígito, elevado a N, é igual ao próprio número.

Veja um exemplo com um número de 3 dígitos em base decimal:

153 = 1**3 + 5**3 + 3**3 =  1 + 125 + 27 = 153

Veja um exemplo com um número de 3 dígitos em base decimal:

1634 = 1**4 + 6**4 + 3**4 + 4**4 = 1634

Escreva um programa que leia números inteiros de 100 a 9999 (não é necessário validação, considere que o usuário digitará apenas valores nesse intervalo) e verifique se é um número de Armstrong.

Resolva essa questão utilizando, apenas DIV e MOD. 
"""

def main():
    # declaração de variaveis
    numero = int()
    milhar = int()
    centena = int()
    dezena = int()
    unidade = int()
    resto = int()
    armstrong = int()
    # entrada de dados
    numero = int(input("Digite um número: "))

    # processamento
    if (numero < 1000):
        centena = numero // 100
        resto = numero % 100
        dezena = resto // 10
        unidade = resto % 10 
        armstrong = (centena ** 3) + (dezena ** 3) + (unidade ** 3)
    else:
        milhar = numero // 1000
        resto = numero % 1000
        centena = resto // 100
        resto = resto % 100
        dezena = resto // 10
        unidade = resto % 10
        armstrong = (milhar ** 4) + (centena ** 4) + (dezena ** 4) + (unidade ** 4)

    # saída de dados
    if (armstrong == numero):
        print(f"{numero} É UM NÚMERO DE ARMSTRONG")
    else:
        print(f"{numero} NÃO É UM NÚMERO DE ARMSTRONG")



    return 0

if __name__ == "__main__":
    main()