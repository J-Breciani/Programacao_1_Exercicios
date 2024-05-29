"""
Faça um programa, com uma função que necessite de um argumento. A função retorna o valor de caractere ‘P’, 
se seu argumento for positivo, e ‘N’, se seu argumento  negativo ou 'Z' se for zero.
"""
def f_resposta(a):
    if (a > 0):
        return "P"
    elif (a == 0):
        return "Z"
    else:
        return "N"

def main():

    # declaração de variáveis

    numero_1 = int()
    resposta = str()

    # entrada de dados
    numero_1 = int(input(""))

    # processamento
    resposta = f_resposta(numero_1)
    # saída de dados
    print(resposta)
    return 0

if __name__ == "__main__":
    main ()