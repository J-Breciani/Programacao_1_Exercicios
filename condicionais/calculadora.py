"""
Desenvolva um programa que receba dois valores para efetuar operações matemáticas de acordo com a opção do usuário, 
1 para soma, 2 para subtração (do primeiro pelo segundo), 3 para multiplicação, 4 para divisão (do primeiro pelo segundo),
 5 para exponenciação (o segundo número será a potência), 6 para  raiz (o primeiro número será o radicando e o segundo o índice).
   Qualquer valor diferente desse deve retornar uma mensagem de erro. Apresente o resultado da operação.
"""
def main():

    # declaração de variáveis:
    operaçao = int()
    primeiro = int()
    segundo = int()

    # entrada de dados:
    print(("1: soma - 2: subtração - 3: multiplicação - 4: divisão - 5:exponeciação - 6: raiz quadrada"))
    operaçao = int(input("Operação escolhida: "))
    while (operaçao < 7 and operaçao >= 1):
        primeiro = int(input("x: "))
        segundo = int(input("y: "))

        # processamento e saída de dados:
        if(operaçao == 1):
            print(primeiro + segundo)
        elif(operaçao == 2):
            print(primeiro - segundo)
        elif(operaçao == 3):
            print(primeiro * segundo)
        elif(operaçao == 4):
            print(primeiro / segundo)
        elif(operaçao == 5):
            print( primeiro ** segundo)
        else:
            print(primeiro ** (1/segundo))

    print("OPERACAO INVALIDA")
    return 0

if __name__ == "__main__":
    main()
    