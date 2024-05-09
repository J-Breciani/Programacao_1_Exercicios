"""
Tem-se um conjunto de dados contendo o sexo (masculino, feminino) e a altura de 5 pessoas. Fazer um algoritmo que calcule e escreva:
- a maior e a menor altura do grupo;
- a média de altura das mulheres;
- a quantidade de homens;
"""

def main():

    # declaração de variáveis
    sexo = str()
    altura = float()
    maior_altura = float()
    menor_altura = float()
    media = float()
    cont_m = int
    cont_f = int
    i = int()
    # entrada de dados
    i = 0
    maior_altura = 0
    menor_altura = 5
    cont_m = 0
    cont_f = 0
    while (i < 5):
        sexo = input("sexo [m]asculino ou [f]eminino? ").lower()
        altura = float(input("Altura em metros: "))
        if sexo == "f":
            media = media + altura
            cont_f = cont_f + 1
        if altura > maior_altura:
            maior_altura = altura
        if altura < menor_altura:
            menor_altura = altura
        if sexo == "m":
            cont_m = cont_m + 1
        i = i + 1
    # processamento de dados

    media = media / cont_f

    # saída de dados
    print(f"{maior_altura:.2f}")
    print(f"{menor_altura:.2f}")
    print(f"{media:.2f}")
    print(cont_m)


    return 0 

if __name__ == "__main__":
    main()