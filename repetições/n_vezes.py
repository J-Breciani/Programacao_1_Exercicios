"""Faça um Programa que leia números até que o usuário não queira mais digitar os números. 
No final escrever a média dos valores lidos. (o usuário digitará a letra s para continuar informando dados e n quando quiser parar)
"""
def main():
    #declaração de variáveis:
    n = int()
    i = int()
    #entrada de dados:
    n = int(input("N: "))
    i = 1 # inicialização da V.C.
    #processamento e processamento de dados:
    while (i <= n): # condição de parada
        print(i) # ação
        i = i + 1 # atualização da V.C.

    return 0
if __name__ == "__main__":
    main()