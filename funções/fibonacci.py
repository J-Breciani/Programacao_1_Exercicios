"""
Faça um programa em linguagem Python que lê um número n digitado pelo usuário(esse número vai ser a quantidade de termos) 
e imprime os n primeiros números da sequência de Fibonacci.
"""

def f_fibo(n): 
    # declaração:
    cont = int()
    a = int()
    p = int()
    # entrada dos dados:
    cont = 0
    a = 0
    p = 1
    # processamento e saída dos dados:
    print(p)
    while (cont < n-1):
        f = a + p
        print(f)
        a = p
        p = f
        cont += 1
def main():
    # declaração de variáveis:
    n = int()
    #entrada de dados:
    n = int(input(""))
    # processamento e saída dos dados:
    f_fibo(n) 

    return 0

if __name__ == "__main__":
    main()