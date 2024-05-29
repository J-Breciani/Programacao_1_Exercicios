"""
Fazer um programa que calcule e escreva o valor de S:
S = 1/1 – 2/4 + 3/9 – 4/16 + 5/25 – 6/36 ... - 10/100

"""
def main():
    # declaração de variáveis: 
    dividendo = int()
    divisor = int()
    soma = float()
    # processamento:
    dividendo = 1
    divisor = 1
    for i in range(5):
        soma += dividendo / divisor
        dividendo += 1
        divisor = dividendo ** 2
        soma -= dividendo / divisor
        dividendo += 1
        divisor = dividendo ** 2

    # saída dos dados: 
    print(soma)

    return 0
if __name__ == "__main__":
    main()