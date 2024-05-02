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