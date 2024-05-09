def main():
    #declaração de variáveis
    palavra = str()

    #entrada de dados:
    
    palavra = input("Digite uma plavra: ").upper()

    #processamento e saída de dados:
    
    for letra in palavra:
        print(letra)
    
    return 0 

if __name__ == "__main__":
    main()