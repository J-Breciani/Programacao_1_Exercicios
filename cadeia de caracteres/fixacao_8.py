"""
Faça um programa que leia dez pares palavras. A partir dessa leitura, o programa deve imprimir uma nova palavra, 
gerada pelas 3 primeiras letras da primeira palavra com as 3 últimas letras da segunda palavra.
"""
def main():

    # declaração de variáveis: 
    palavra = str()
    segunda = str()
    formada = str

    # entrada, processamento e saída:
    for i in range(10):
        palavra = input(" ").upper()
        segunda = input(" ").upper()
        formada = palavra[:3] + segunda[len(segunda) -3: len(segunda)]
        print(formada)

    return 0 

if __name__ == "__main__":
    main()

