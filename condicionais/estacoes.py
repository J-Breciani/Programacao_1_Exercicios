def main ():
    # declaração de variáveis:
    outono = int()
    inverno = int()
    verao = int()
    primavera = int()
    dia = int()
    mes = int()

    # entrada de dados:
    dia = int(input("Dia: "))
    mes = int(input("Mês: "))

    # processamento de dados:
    outono = (dia >= 21 and mes >= 3) or ( dia <= 20 and mes <= 6)
    inverno = (dia >= 21 and mes >= 6) or (dia <= 22 and mes <= 9)
    primavera = (dia >= 23 and mes >= 9) or (dia <= 20 and mes <= 12)
    verao = (dia >= 21 and mes == 12) or (dia <= 20 and mes <= 3)
    # saída de dados:
    if (outono):
        print("É outono")
    elif (inverno):
        print("É inverno")
    elif (primavera):
        print("É primavera")
    elif (verao):
        print("É verão")
    else:
        print("Data inválida")

    return 0 

if __name__ == "__main__":
    main()