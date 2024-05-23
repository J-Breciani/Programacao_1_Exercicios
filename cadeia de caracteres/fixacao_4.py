"""
Faça um programa que leia uma frase e conte quantas vezes aparece a letra "A".
"""
def main():

    # declaração de variáveis: 
    data = str()
    ano = str()
    idade = int()
    # entrada de dados:
    data = input("Informe uma data: ")

    # processamento:
    for i in range(len(data)):
        if (i >= 6 and i <= 10):
            ano += data[i]
    ano = int(ano)
    idade = 2024 - ano
  
    # saída de dados: 
    print(f"{idade} anos")



    return 0 

if __name__ == "__main__":
    main()