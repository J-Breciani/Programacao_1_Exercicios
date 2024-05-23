"""
Utilizando, apenas e obrigatoriamente, ESTRUTURAS CONDICIONAIS, faça um programa, em Python 3.x, que receba como entrada de dados, 
via teclado, 4 valores  INTEIROS (considere que não serão informados valores iguais) e apresente,
como saída de dados, a soma do MAIOR com o MENOR.
"""
def main():
    # declaração de variaveis
    a = int()
    b = int()
    c = int()
    d = int()
    maior = int()
    menor = int()
    # entrada de dados
    a = int(input("A: "))
    b = int(input("B: "))
    c = int(input("C: "))
    d = int(input("D: "))

    # processamento
    if (a > b and a > c and a > d):
        maior = a
    elif( b > a and b > c and b > d):
        maior = b
    elif(c > a and c > b and c > d):
        maior = c
    else:
        maior = d
    if (a < b and a < c and a < d):
        menor = a
    elif (b < a and b < c and b < d):
        menor = b
    elif(c < a and c < b and c < d):
        menor = c
    else:
        menor = d
    # saída de dados
    
    print(maior + menor)

    return 0

if __name__ == "__main__":
    main()