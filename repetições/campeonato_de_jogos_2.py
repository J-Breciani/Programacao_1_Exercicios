def main():

    # declaração de variáveis
    quantidade_jogadores = int()
    soma_de_pontos = int() 
    nick = str()
    fase = str()
    pontos = int()
    media = float()
    maior_pontos = int()
    maior_nick = str()

    # entrada dos dados:
    nick = input("")
    maior_pontos = 0
            
    # processamento dos dados:       
    while (nick != ""):
       quantidade_jogadores += 1
       pontos = 0
       for i in range(10):
            if (pontos < 0):
                pontos = 0
            fase = input("").upper()
            if(fase == "A1"):
               pontos += 5
            elif(fase == "A2"):
                pontos += 7
            elif(fase == "A3"):
                pontos += 10
            elif(fase == "E1"):
                pontos -= 2
            elif(fase == "E2"):
                pontos -= 5
            else:
                pontos = 0
            if (pontos > maior_pontos):
                nick_maior = nick
                maior_pontos = pontos
            soma_de_pontos += pontos
            print(f"{nick} {pontos} pontos")
            nick = input("")
    media = soma_de_pontos / quantidade_jogadores
    # saída:
    print(f"Media de pontos = {media:.2f} pontos")
    print(f"Vencedor {nick_maior} com {maior_pontos} pontos")


    return 0
if __name__== "__main__":
    main()