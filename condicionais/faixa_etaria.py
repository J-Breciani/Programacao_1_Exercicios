"""
criar um programa que receba a idade de uma pessoa e determine em qual categoria ela se enquadra:

Se a idade for menor que 18 anos, imprimir "Menor de idade".
Se a idade estiver entre 18 e 65 anos (inclusive), imprimir "Adulto".
Se a idade for maior que 65 anos, imprimir "Idoso".

"""



def main():

    # declaração de variáveis
    idade = int()
    # entrada de dados
    idade = int(input("Qual sua idade: "))
    
    # processamento e saída
    if (idade < 18):
        print("Menor de idade")
    elif (idade < 65):
        print("Adulto")
    else:
        idade("Idoso")

    return 0

if __name__ == "__main__":
    main()