def main():

    # declaração de variáveis
    numero_1 = int()
    numero_2 = int()
    numero_3 = int()
    numero_4 = int()

    # entrada de dados
    numero_1 = int(input("Digite um número: "))
    numero_2 = int(input("Digite um número: "))
    numero_3 = int(input("Digite um número: "))
    numero_4 = int(input("Digite um número: "))


    #processamento e saída
    if (numero_1 >= numero_2 and numero_1 >= numero_3 and numero_1 >= numero_4): # 1 maior
        print(numero_2 + numero_3 + numero_4)
    elif (numero_2 >= numero_1 and numero_2 >= numero_3 and numero_2 >= numero_4): # 2 maior 
        print(numero_1 + numero_3 + numero_4)
    elif (numero_3 >= numero_1 and numero_3 >= numero_2 and numero_3 >= numero_4): # 3 maior
        print(numero_1 + numero_2 + numero_4)
    else:
        print(numero_1 + numero_2 + numero_3) # 4 maior

    return 0 

if __name__ == "__main__":
    main()