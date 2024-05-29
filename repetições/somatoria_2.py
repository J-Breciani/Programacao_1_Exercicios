"""
Fazer um programa que calcule e escreva o valor de S:
S = (37 x 38)/1 + (36 x 37)/2 + (35 x 36)/3 + ... + (1 x 2)/37
"""
def main():

    # declaração de variáveis: 
    primeiro = int()
    segundo = int()
    inteiro = int()
    soma = float()

    # processamento:
    primeiro = 37
    segundo = 38
    inteiro = 1

    while (inteiro <= 37):
        soma += (primeiro * segundo) / inteiro
        primeiro -= 1
        segundo -= 1
        inteiro += 1
    

    # saída de dados: 
    print(soma)
    return 0 

if __name__ == "__main__":
    main()