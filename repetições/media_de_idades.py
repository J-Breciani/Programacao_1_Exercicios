def main():
    #declaração de variáveis

    idade = int()
    soma = int()
    media = float()
    cont = int()
    i = int()

    #entrada de dados:
    i = 1

    while (i != 0):
        idade = int(input("Digite a idade: "))
        i = idade
        if (i == 0):
            break
        cont = 1 + cont
        soma = soma + idade

    #processamento 
    media = soma / cont
    
    #saída de dados:

    print(f"{media:.1f}")

    return 0 

if __name__ == "__main__":
    main()