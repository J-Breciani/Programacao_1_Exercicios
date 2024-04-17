"""
Escreva um algoritmo que leia as idades de 2 homens e de 2 mulheres 
(considere que as idades dos homens serão sempre diferentes entre si, bem como as das mulheres).
 Calcule e escreva a soma das idades do homem mais velho com a mulher mais nova, e o produto das idades do homem mais novo com
 a mulher mais velha."""

def main():
    #declaração de variáveis

    homem_1 =int()
    homem_2 = int()
    mulher_1 = int()
    mulher_2 = int()
    homem_mais_novo = int()
    homem_mais_velho = int()
    mulher_mais_nova = int()
    mulher_mais_velha = int()
    soma = int()
    produto = int()

    #entrada de dados:
    homem_1 =int(input("Homem 1: "))
    homem_2 = int(input("Homem 2: "))
    mulher_1 = int(input("Mulher 1: "))
    mulher_2 = int(input("Mulher 2: "))

    #processamento:
    if (homem_1 < homem_2 ):
        homem_mais_novo = homem_1
        homem_mais_velho = homem_2
    else:
        homem_mais_novo = homem_2
        homem_mais_velho = homem_1
    if(mulher_1 < mulher_2):
        mulher_mais_nova = mulher_1
        mulher_mais_velha = mulher_2
    else:
        mulher_mais_nova = mulher_2
        mulher_mais_velha = mulher_1

    soma = homem_mais_velho + mulher_mais_nova
    produto = homem_mais_novo * mulher_mais_velha

    #saída:
    print(soma , produto)

    return 0 

if __name__ == "__main__":
    main()