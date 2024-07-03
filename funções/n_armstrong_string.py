"""
Um número de Armstrong é um número de N dígitos onde a soma de cada dígito, elevado a N, é igual ao próprio número.

Veja um exemplo com um número de 3 dígitos em base 10:

153 = 13 + 53 + 33 =  1 + 125 + 27 = 153

Escreva um programa que imprima todos os números de Armstrong em base 10 que tenham até 6 dígitos, começando por 1.

Resolva esse exercício utilizando STRING. 
"""
def f_somaArmstrong(n):
    n = str(n)
    soma = 0
    tamanho = len(n)
    for i in range(len(n)):
        soma += int(n[i])**tamanho
    return soma

def f_verificaArmstrong(n):
    return n == f_somaArmstrong(n)
    
def main():
    #declaração de variáveis:
    i = int()
    #entrada processamento e saída dos dados:
    for i in range(1,1000000):
        if (f_verificaArmstrong(i)):
          print(i)
    return 0

if __name__ == "__main__":
    main()