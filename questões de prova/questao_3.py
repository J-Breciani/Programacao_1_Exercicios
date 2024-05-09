"""
Acredita-se que todos os adultos precisam beber cerca de 2 litros de água por dia, no entanto essa quantidade é uma estimativa. 
Isso porque a quantidade exata de água que cada pessoa necessita ingerir diariamente varia de acordo com o peso, idade, estação do ano 
e outros fatores, como prática de atividade física, por exemplo, já que durante o exercício se perde mais líquidos através do suor, sendo 
necessário consumir mais água.

A água corresponde a cerca de 60 a 70% da composição corporal total e é fundamental para o bom funcionamento do organismo, 
por isso a forma mais adequada para saber qual a necessidade diária de água é através de um cálculo que leva em consideração o peso e 
a idade da pessoa.

Para descobrir a quantidade de água que se deve ingerir por dia, a calculadora utiliza os seguintes valores, que variam de acordo com a idade:

Adultos	Quantidade de água por kg
Jovens até os 17 anos	40 ml por cada kg
18 a 55 anos	35 ml por cada kg
56 a 65 anos	30 ml por cada kg
66 anos em diante	25 ml por cada kg


Com base nos dados, acima, faça um programa, em Python 3.x, que solicite a idade e o peso ao usuário, então, calcule
e informe a quantidade de água (EM LITROS, COM UMA CASA DECIMAL) que essa pessoa deve consumir ao longo do dia.
"""

def main():

    # declaração de variáveis:

    idade = int()
    peso = int()
    agua = float()

    # entrada de dados:

    idade = int(input("Informe sua idade: "))
    peso = int(input("Informe seu peso: "))

    # processamento de dados:
    if(idade <= 17):
        agua = peso * 0.040
    elif ( idade <= 55):
        agua = peso * 0.035
    elif(idade <= 65):
        agua = peso * 0.03
    else:
        agua = peso * 0.025

    # saída de dados:
    print(f"{agua:.1f} LITROS")

    return 0 

if __name__ == "__main__":
    main()