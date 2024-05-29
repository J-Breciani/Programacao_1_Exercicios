"""
Fazer um programa que calcule e escreva o valor de S:
S = 1/1 + 3/2 + 5/3 + 7/4 + ... + 99/50

"""
def main():

    # declaração de variáveis: 
    divisor = int()
    dividendo = int()
    soma = float()

    # processamento:
    divisor = 1
    dividendo = 1

    while (divisor <=50):
        soma += (dividendo / divisor)
        dividendo += 2
        divisor += 1
    

    # saída de dados: 
    print(soma)
    return 0 

if __name__ == "__main__":
    main()