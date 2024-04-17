"""
Faça um Programa que leia números até que o usuário não queira mais digitar os números.
 No final escrever a soma dos valores lidos. (o usuário digitará a letra s para continuar informando dados e n quando quiser parar)
"""
def main():
    #declaração de variáveis:
    flag = str()
    numero = int()
    soma = int()
    i = int()
    media = float()
    #entrada de dados:
    flag = input("Deseja inserir um número: [s/n] ").lower() #inicialização da V.C.
    #processamento de dados:
    while(flag == "s"): #condição de parada
        numero = int(input("Número: "))
        soma = soma + numero #ação
        i = i + 1 
        flag = input("Deseja inserir outro número: [s/n] ").lower() #atualização da V.C.
    media = int(soma / i)
    #saída de dados: 
    print(f"{media:.0f}")
    return 0

if __name__ == "__main__":
    main()