"""
Faça uma função que informe a quantidade de dígitos de um determinado número inteiro informado, 
UTILIZANDO DIV E MOD. SEM USAR RECURSO DE STRING.
"""
def f_resposta(a):
    if (a // 10 == 1):
        return 2
    elif ( a % 10 == a):
        return 1
    elif (a // 100 <= 9):
        return 3
    elif (a // 1000 <= 9):
        return 4
    else:
        return 5


def main():

    # declaração de variáveis

    numero_1 = int()
    resposta = int()

    # entrada de dados
    numero_1 = int(input(""))

    # processamento
    resposta = f_resposta(numero_1)
    # saída de dados
    print(resposta)
    return 0

if __name__ == "__main__":
    main ()