"""
Considere um programa que contenha um menu de seis opções (de 1 a 6). Faça uma validação de entrada, em Python 3.x, 
que valide o input do usuário da seguinte forma: caso o usuário digite uma opção fora desses valores, 
exiba a mensagem "OPÇÃO INVÁLIDA. DIGITE UM VALOR DE 1 A 6", e caso ele informe uma opção dentro do esperado, apresenta  
a mensagem "OPÇÃO VÁLIDA".
"""

def main():

    # declaração de variáveis

    numero = int()

    # entrada de dados

    numero = int(input("Digite um número de 1 a 6: "))

    # processamento e saída dos dados

    while (numero < 1 or numero > 6):
        print("OPÇÃO INVÁLIDA. DIGITE UM VALOR DE 1 A 6")
        numero = int(input("Digite um número de 1 a 6: "))
    print ("OPÇÃO VÁLIDA")
    

    return 0

if __name__ == "__main__":
    main()