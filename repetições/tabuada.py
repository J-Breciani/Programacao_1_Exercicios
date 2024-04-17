"""Faça um Algoritmo para ler um valor inteiro e escrever a tabuada de 1 a 10 do valor lido."""
def main():
    #declaração de variáveis
    tabuada = int()
    i= int()
    resultado = int()

    #entrada de dados:
    tabuada = int(input("Informar tabuada de: "))
    i = 2 #inicialização da V.C.

    #processamento e saída de dados:
    while(i <= 10): # condição de parada
        resultado = tabuada * i
        print(f"{i} X {tabuada} = {resultado}" ) #ação
        i = i + 1 #atualização da V.C.
    return 0 

if __name__ == "__main__":
    main()
