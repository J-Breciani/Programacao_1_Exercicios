"""
Faça um programa em Python3 que leia o resultado uma rodada de um campeonato de futebol. O programa deve ler o nome do primeiro time
e o nome do segundo time, em seguida a quantidade de gols primeiro time e a do segundo time (validação: aceite apenas valores maiores
ou iguais a zero, caso ocorram entradas incorretas retorne à entrada dos dados). A condição de parada será informar o nome do primeiro
time como string vazia (“”). Após a entrada de dados da partida o programa deverá imprimir o nome do time vencedor, ou imprimir que
houve empate, ou imprimir que a quantidade de gols é inválida. Ao final da entrada de dados de todas as partidas da rodada o programa
deve informar:

a) A média de gols da rodada
b) O time que fez mais gols em uma mesma partida da rodada
c) A quantidade de gols da partida em que houve o menor número de gols na rodada
"""
def f_jogo(a,b,c,d):
    if (b > d): # primeiro time ganha
        return(f"{a} x {c}\nVencedor: {a}")
    elif(b < d): # segundo time ganha
        return(f"{a} x {c}\nVencedor: {c}")
    else:
        return("Empate")

def main():
    # declaração das variáveis
    primeiro_time = str()
    segundo_time = str()
    gols_pri = int()
    gols_seg = int()
    resultado = str()
    media = float()
    soma = int()
    times = int()
    maior = int()
    maior_time = int()
    menor = int()
    # entrada dos dados:
    primeiro_time = "a"
    maior = 0
    menor = 5000

    # processamento e saída dos dados:
    while(primeiro_time != ""):
        try:
            primeiro_time = input("")
            segundo_time = input("")
            gols_pri = int(input(""))
            gols_seg = int(input(""))
            resultado = f_jogo(primeiro_time,gols_pri,segundo_time,gols_seg)
            times += 1
            soma += gols_pri
            soma += gols_seg
            if(gols_pri > maior):
                maior = gols_pri
                maior_time = primeiro_time
            if(gols_seg > maior):
                maior = gols_seg
                maior_time = segundo_time
            if(gols_pri < menor):
                menor = gols_pri
            if(gols_seg < menor):
                menor = gols_seg             
            print(resultado)
        
        except EOFError:
            break
    media = soma / times
    print(f"Média de Gols: {media} por jogo")
    print(f"Time aue fez mais gols em um jogo: {maior_time}")
    print(f"Menor número de gols em uma partida: {menor}")

    return 0

if __name__ == "__main__":
    main()