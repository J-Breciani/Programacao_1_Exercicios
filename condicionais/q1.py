def main():

    # declaração de variáveis

    numero = int()
    

    # entrada de dados

    numero = int(input(""))

    # processamento
    milhar = numero // 1000
    centena = (numero - milhar * 1000) // 100
    dezena = (numero - milhar * 1000 - centena * 100) // 10
    unidade = numero - milhar * 1000 - centena * 100 - dezena * 10
    inverso = (unidade * 1000) + (dezena * 100) + (centena * 10) + milhar

    # saída
    print(inverso)
    if (numero == inverso):
        print(f"{numero} É UMA CAPICUA")
    else:
        print(f"{numero} NÃO É UMA CAPICUA")


    return 0 

if __name__ == "__main__":
    main()