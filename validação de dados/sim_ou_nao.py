"""
Faça um programa que solicite que o usuário digite a resposta para uma pergunta (S ou N). 
Na entrada altere esse valor para maiúsculo.
"""
def main():

    # declaração de variáveis
    resposta = str()

    # entrada dos dados

    resposta = input("Informe S ou N: ").upper()

    # processamento e saída dos dados

    while resposta != "S" and resposta != "N":
        print("RESPOSTA INCORRETA, DIGITE S OU N")
        resposta = input("Informe S ou N: ").upper()

    if resposta == "S" or resposta == "N":
        print("RESPOSTA CORRETA")


    return 0

if __name__ == "__main__":
    main()