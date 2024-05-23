"""
Faça um programa que leia dez palavras e, ao final, apresente a soma de todas as letras "O" digitadas.
"""
def main():

    # declaração de variáveis: 
    palavra = str()
    cont = int()

    # entrada e processamento de dados:
    for i in range(10):
        palavra = input("Digite uma frase: ").upper()
        for a in range(len(palavra)):
            if palavra[a] == "O":
                cont += 1

    # saída de dados: 
    print(f"Soma das letras O: {cont}")


    return 0 

if __name__ == "__main__":
    main()