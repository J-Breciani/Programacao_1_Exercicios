"""
Um jogo de videogame gera um relatório após processar os dados de um campeonato. Neste campeonato vários jogadores participam de 10 fases, 
onde os pontos são contabilizados por tipos de erros e tipos de acertos para cada fase. Os acertos são caracterizados pelas strings: 
A1, A2 e A3. Já os erros são  caracterizados pelas strings: E1, E2, E3.

A1 : soma 5 pontos
A2 : soma 7 pontos
A3 : soma 10 pontos
E1 : subtrai 2 pontos, se tiver pontos > 0
E2 : subtrai 5 pontos, se tiver pontos > 0
E3 : zera a pontuação
Os dados são fornecidos nesta ordem:
Nick name do jogador
Tipo de erro/acerto para cada uma das 10 fases.
Considere que os dados encerram quando um nick name igual a string vazia for fornecido para o
jogador.
Seu programa deverá calcular, para cada jogador, a pontuação ao final das 10 fases, sendo que toda
vez que a pontuação se tornar negativa deverá ser zerada. Imprima o nome do jogador e sua
pontuação final.
Ao final do campeonato imprima:
- A média de pontos do campeonato;
- O nome e a pontuação do jogador com maior pontuação;

"""

def main():

    # declaração de variáveis: 

    nick = str()
    vencedor = str()
    pontos = int()
    media = float()
    jogada = str()
    i = int()
    maior = int()
    jogadores= int()
    media = float()
    pontos_totais = int()


    # entrada de dados:
    maior = 0
    nick = input("Informe o nick: ")

    # processamento:

    while (nick != ""):
        pontos = 0
        for i in range(0,10,1):
            jogada = input("").upper()
            if (jogada == "A1"):
                pontos += 5
            elif (jogada == "A2"):
                pontos += 7
            elif (jogada == "A3"):
                pontos += 10
            elif (jogada == "E1"):
                    pontos -= 2
            elif (jogada == "E2"):
                    pontos -= 5
            elif (jogada == "E3"):
                pontos = 0
            if (pontos < 0):
                pontos = 0
        print(f"{nick} {pontos} pontos")
        if (pontos > maior):
            vencedor = nick
            maior = pontos
        jogadores += 1
        pontos_totais += pontos
        nick = input("")

    media = pontos_totais / jogadores

    # saída de dados: 
    print(f"Média de pontos = {media:.2f} por jogo")
    print(f"Vencedor {vencedor} com {maior} pontos")

    return 0 

if __name__ == "__main__":
    main()