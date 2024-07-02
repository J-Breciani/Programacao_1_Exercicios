"""
Faça uma função que retorne o reverso de um número inteiro informado. Por exemplo: 127 -> 721. Usar, exclusivamente, DIV e MOD.

NÃO USAR STRING
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
  
  #entrada de dados
  n = int(input())

  #processamento e saída de dados
  print(f_inverte(n))

  return 0

if __name__ == "__main__":
  main()


