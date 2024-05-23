"""
Faça um programa que leia a data de nascimento, de uma pessoa, no formato DD/MM/AAAA e imprima o ano em que nasceu.
"""
def main():

    # declaração de variáveis: 
    data = str()
    ano = str()

    # entrada de dados:
    data = input("Informe uma data: ")

    # processamento:
    for i in range(len(data)):
        if (i >= 6 and i <= 10):
            ano += data[i]

  
    # saída de dados: 
    print(ano)

    return 0 

if __name__ == "__main__":
    main()
