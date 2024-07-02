"""
Jogo de Craps.

Faça um programa de implemente um jogo de Craps.

O jogador lança um par de dados, obtendo um valor entre 2 e 12.

Se, na primeira jogada, você tirar 7 ou 11, é um "natural" e você ganhou.

Se você tirar 2, 3 ou 12 na primeira jogada, isto é chamado de "craps" e você perdeu.

Se, na primeira jogada, você fez um 4, 5, 6, 8, 9 ou 10, este é seu "Ponto".

Seu objetivo agora é continuar jogando os dados até tirar este número outra vez, quando você tirar esse número, você "ganhou". 
Apresente o número de jogadas que foram necessárias para você ganhar.

No entanto, você perde, se tirar um 7 antes de tirar este "Ponto" novamente. Apresente o número de jogadas que você fez até perder.
"""

def f_craps(x):
    jogadas = int()
    flag = bool()
    flag = True
    if(x == 7 or x == 11):
        print(x)
        return ("NATURAL! VOCÊ GANHOU\nJOGADAS = 1")
    elif(x == 2 or x == 3 or x == 12):
        print(x)
        return ("CRAPS! VOCÊ PERDEU\nJOGADAS = 1")
    else:
        print(x)
        ponto = x
        jogadas = 1
        while(flag):
            jogadas +=1 
            x = int(input(""))
            print(x)
            if (x == ponto or x == 7):
                flag = False
        if(ponto == x):
            return (f"VOCÊ GANHOU\nJOGADAS = {jogadas}")
        else:
            return (f"VOCÊ PERDEU\nJOGADAS = {jogadas}")


def main():
    # declaração de variáveis
    pontos = int()
    resposta = str()
    # entrada de dados
    pontos = int(input(""))
    # processamento
    resposta = f_craps(pontos)
    # saída dos dados
    print(resposta)
    

    return 0 
if __name__ == "__main__":
    main()