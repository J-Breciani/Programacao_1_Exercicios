"""
Código Padrão Americano para o Intercâmbio de Informação (do inglês American Standard Code for Information Interchange - ASCII, 
pronunciado [áski]) é um sistema de representação de letras, algarismos e sinais de pontuação e de controle, através de um sinal 
codificado em forma de código binário (cadeias de bits formada por vários 0 e 1), desenvolvido a partir de 1960, que representa um 
conjunto de 128 sinais: 95 sinais gráficos (letras do alfabeto latino, algarismos arábicos, sinais de pontuação e sinais matemáticos) 
e 33 sinais de controle, utilizando 7 bits para representar todos os seus símbolos.

Assim, nesse sistema a letra "A" é representada pelo código binário que, em decimal, representa 65 e a letra "a", por sua vez, pelo 
código que representa 97 em decimal.

Dessa forma, ao se comparar uma letra com outra, letras com ordem maior serão consideradas maiores que a outra, como no exemplo do 
parágrado anterior "a" > "A".

Baseado nessa informação, faça um programa, em Python 3.x, que receba strings e informe, a partir de uma função, qual a MAIOR e a 
MENOR letra do texto. A condição de parada é quando for informada uma string vazia ("").
"""

def f_maior(palavra):
    letra = str()
    numeracao = int()
    maior = int()
    maior = 0
    for i in range(len(palavra)):
        letra = palavra[i]
        numeracao = f_ord(letra)
        if (numeracao > maior):
            maior = numeracao
    return maior
  
def f_menor(palavra):
    letra = str()
    numeracao = int()
    menor = int()
    menor = 5000
    for i in range(len(palavra)):
        letra = palavra[i]
        numeracao = f_ord(letra)
        if (numeracao < menor):
            menor = numeracao
    return menor

def f_ord(letra):
    numero = int()
    numero = ord(letra)
    return numero

def f_chr(numero):
    letra = str()
    letra = chr(numero)
    return letra

def main():
    # declaração:
    palavra = str()
    maior = int()
    menor = int()

    # entrada:
    palavra = input("").upper()
    # processamento:
    while(palavra != ""):
        maior = f_maior(palavra)
        menor = f_menor(palavra)
        maior = f_chr(maior)
        menor = f_chr(menor)
        # saída:
        print(f"MAIOR LETRA DE {palavra} = {maior}")
        print(f"MENOR LETRA DE {palavra} = {menor}")
        palavra = input("").upper()
    return 0
if __name__ == "__main__":
    main()