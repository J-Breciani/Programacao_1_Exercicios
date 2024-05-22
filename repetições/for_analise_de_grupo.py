"""
Tem-se um conjunto de dados contendo o sexo (masculino, feminino) e a altura de 5 pessoas. Fazer um algoritmo que calcule e escreva:
- a maior e a menor altura do grupo;
- a média de altura das mulheres;
- a quantidade de homens;

"""

def main():

    # declaração de variáveis: 
    i = int()
    maior = float()
    menor = float()
    soma = float()
    quantidade_m = int()
    quantidade_f = int()
    media = float()
    sexo = str()
    altura = float()

    # entrada de dados: 

    maior = 0
    menor = 5.0

    for i in range(5):
        sexo = input("Informe o sexo: ").lower()
        altura = float(input("Informe a altura: "))
        if (altura > maior):
            maior = altura
        if (altura < menor):
            menor = altura 
        if (sexo == "m"):
            quantidade_m += 1
        elif (sexo == "f"):
            soma += altura
            quantidade_f += 1


    # processamento:

    media = soma / quantidade_f

    # saída dos dados: 

    print(maior)
    print(menor)
    print(media)
    print(quantidade_m)

    return 0
if __name__ == "__main__":
    main()