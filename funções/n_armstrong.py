"""
Um número de Armstrong é um número de N dígitos onde a soma de cada dígito, elevado a N, é igual ao próprio número.

Veja um exemplo com um número de 3 dígitos em base 10:

153 = 1**3 + 5**3 + 3**3 =  1 + 125 + 27 = 153

Escreva um programa que imprima todos os números de Armstrong em base 10 que tenham até 6 dígitos, começando por 1.

Resolva esse exercício utilizando, apenas DIV e MOD. 

"""


def f_tam(n):
  cont = 0
  while (n > 0):
    cont += 1
    n = n // 10
  return cont

def f_somaArmstrong(n):
  soma = 0
  tam = f_tam(n)
  while(n > 0):
    resto = n % 10
    soma += resto**tam
    n = n // 10
  return soma

def f_verificaArmstrong(n):
  return n == f_somaArmstrong(n)

def main():
  #declaração de variáveis
  i = int(0)
  #entrada de dados
  for i in range(1,1000000):
    if (f_verificaArmstrong(i)):
      print(i)
  return 0

if __name__ == "__main__":
  main()