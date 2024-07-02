"""
UTILIZE UMA FUNÇÃO PARA CÁLCULO DA MÉDIA

Ler informações sobre um grupo de 25 pessoas e calcular alguns dados estatísticos.

Para cada pessoa do grupo obter o o sexo (“F” para feminino e “M” para o masculino), a altura e o peso. Calcular e escrever:

As letras de A, C e D devem ser efetuadas com utilização de funções externas.

O preenchimento das listas de sexo, altura e peso podem ser preenchidas diretamente na função.

Dica: para testar se funciona, teste com 5 pessoas, para não ter que digitar 75 informações toda vez que testar.

a) A média de peso dos homens
b) A maior peso entre os homens
c) A média de peso do grupo
d) A média de altura entre as mulheres
e) A menor altura entre as mulheres
"""

def f_media(numero, quantidade):
    media = float()
    media = numero / quantidade 
    return media


def main():
    # declaracão:
    media_homens = float()
    media_grupo = float()
    media_mulheres = float()
    sexo = str()
    altura = float()
    peso = int()
    n_homens = int()
    n_mulheres = int()
    soma_pesos_homens = int()
    maior_peso_homens = int()
    soma_pesos_grupo = int()
    soma_altura_mulheres = float()
    menor_altura_mulheres = float()
    # entrada:
    maior_peso_homens = 0
    menor_altura_mulheres = 50
    for i in range(25):
        sexo = input("").upper()
        altura = float(input(""))
        peso = int(input(""))
        soma_pesos_grupo += peso
        if (sexo == "M"):
            n_homens += 1
            soma_pesos_homens += peso
            if(peso > maior_peso_homens):
                maior_peso_homens = peso
        else:
            n_mulheres += 1
            soma_altura_mulheres += altura
            if(altura < menor_altura_mulheres):
                menor_altura_mulheres = altura

    # processamento:
    media_homens = f_media(soma_pesos_homens,n_homens)
    media_grupo = f_media(soma_pesos_grupo, 25)
    media_mulheres = f_media(soma_altura_mulheres, n_mulheres)

    # saída:
    print(f"{media_homens:.2f}")
    print(f"{maior_peso_homens:.2f}")
    print(f"{media_grupo:.2f}")
    print(f"{media_mulheres:.2f}")
    print(f"{menor_altura_mulheres:.2f}")

    return 0

if __name__ == "__main__":
    main()