"""
Faça um programa que leia uma frase e conte quantas vezes aparecem vogais no texto.
"""
def main():

    # declaração de variáveis: 
    frase = str()
    quantidade = int()
    # entrada de dados:
    frase = input("Informe uma frase: ").upper()

    # processamento:
    for i in range(len(frase)):
        if (frase[i] == "A" or frase[i] == "E" or frase[i] == "I" or frase[i] == "O" or frase[i] == "U") :
            quantidade += 1
  
    # saída de dados: 
    print(f"A frase tem {quantidade} vogais")



    return 0 

if __name__ == "__main__":
    main()