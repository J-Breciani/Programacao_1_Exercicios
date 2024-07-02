"""
Faça um programa, em Python 3.x, que receba strings e informe, a partir de uma função, 
qual a menor letra do texto (considerando A a menor letra e Z a maior). 
A condição de parada é quando for informada uma string vazia ("").
"""
def f_ord(a):
    a = ord(a)
    return a 
def f_chr(b):
    b = chr(b)
    return b


def main():
    # declaração de variáveis
    palavra = str()
    numero = int()
    menor = int()
    letra = str
    # entrada dos dados
    menor = 1000
    palavra = input("").upper()
    # processamento  e saída de dados
    while(palavra != ""):
        for i in range(len(palavra)):
            numero = f_ord(palavra[i])
            if numero < menor:
                menor = numero
        letra = f_chr(menor)
        print(letra)
        palavra = input("").upper()





    return 0

if __name__ == "__main__":
    main()
    