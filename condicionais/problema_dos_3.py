def main():

    # declaração de variáveis
    a = int()
    b= int()
    c = int()
    # entrada de dados
    a = int(input("Número 1: "))
    b= int(input("Número 2: "))
    c= int(input("Número 3: "))

    # processamento e saída dos dados
    
    if ( a == b and b == c):
        print("Os números são iguais")
    elif ( a > b and a > c):
        print("O primeiro número é o maior")
    elif (b > a and b > c):
        print("O segundo número é o maior")
    else:
        print("O terceiro número é o maior")


    return 0

if __name__ == "__main__":
    main()