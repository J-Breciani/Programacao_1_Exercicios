"""
Faça um programa, em Python 3.x, que solucione o seguinte somatório:

S =  - (1 + 1)/2 + (2 + 4)/4 - (3 + 9)/6 + (4 + 16)/8 ..... - (9 + 81)/18 + (10 + 100)/20

OBS: PARA SER AVALIADO O PROGRAMA DEVE GERAR OUTPUT VÁLIDO, SEM ERRO. EM CASO DE ERRO, 
PROCURE ELIMINAR A SAÍDA DE ERRO, DEIXANDO, APENAS SAÍDAS VÁLIDAS, MESMO QUE INCOMPLETAS.

"""

def f_equacao(a,b,c):
    solucao = float()
   # processamento:
    for i in range (5):
        solucao += - (a + b) / c
        a = a + 1
        b = a ** 2
        c = a * 2
        solucao += + (a + b) / c
        a = a + 1 
        b = a ** 2
        c = a * 2
    return solucao
    
def main():
    #declaração de variáveis
    a = int()
    b = int()
    c = int()
    resultado = float()
  
    #entrada de dados
    a = 1
    b = 1 
    c = 2
    #processamento
    resultado = f_equacao(a,b,c)
    
    #saída de dados
    print(resultado)
    return 0

if __name__ == "__main__":
  main()
