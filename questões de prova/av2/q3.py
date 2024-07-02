"""
Faça um programa que verifique números informados por input (de -infinito a +infinito), identificando os que são capicuas 
(capicuas é o número que lido de trás para frente é a mesma coisa: 121, 1001, 4334 etc)

Utilize as seguintes funções externas criadas por você:

a) uma função que retorne o tamanho de um número 

b) um função que inverta um número

A condição de parada será quando for informado um número IGUAL A ZERO

os outputs devem seguir o seguinte modelo
"""

def f_tamanho(n):
    #declaração de variáveis
    cont = int()   
    cont = 0
    #processamento
    while (n > 0):
        n = n // 10
        cont += 1
    
    #valor de retorno
    return cont

def f_inverte(n):
    #declaração de variáveis
    invertido = int(0)
    pot = int(0)
    resto = int(0)

    #inicialização de variáveis
    invertido = 0
    pot = f_tamanho(n)-1
    
    #processamento
    while (n > 0):
        resto = n % 10
        invertido += resto * 10 ** pot
        n = n // 10
        pot = pot - 1
        
    #valor de retorno
    return invertido

def main():
  #declaração de variáveis
  n = int(0)
  inverso = int()
  
  #entrada de dados
  n = int(input(""))
  #processamento
  while(n != 0): 
    inverso = f_inverte(n)
    print(f"O inverso de {n} é {inverso}")
    n = int(input(""))
    
  # saída de dados
  

  return 0

if __name__ == "__main__":
  main()