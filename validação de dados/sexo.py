"""
Faça um programa que solicite que o usuário digite um sexo (M ou F). Na entrada altere esse valor para maiúsculo. 
Faça uma validação de entrada, em Python 3.x, que valide o input do usuário da seguinte forma: caso o usuário digite um sexo válido, 
exiba a mensagem "SEXO VÁLIDO", caso o usuário digite um sexo inválido a mensagem "SEXO INVÁLIDO, DIGITE F OU M" deverá ser exibida
"""
def main():

    # declaração de variáveis
    sexo = str()

    # entrada dos dados

    sexo = input("Informe o sexo com M ou F: ").upper()

    # processamento e saída dos dados

    while sexo != "M" and sexo != "F":
        print("SEXO INVÁLIDO, DIGITE F OU M")
        sexo = input("Informe o sexo com M ou F: ").upper()

    if sexo == "M" or sexo == "F":
        print("SEXO VÁLIDO")


    return 0

if __name__ == "__main__":
    main()