"""
Faça um algoritmo para ler: quantidade atual em estoque, quantidade máxima em estoque e quantidade mínima em estoque de um produto.
 Calcular e escrever a quantidade média ((quantidade média = quantidade máxima + quantidade mínima)/2). 
 Se a quantidade em estoque for maior ou igual a quantidade média escrever a mensagem 'NÃO EFETUAR COMPRA', 
 senão escrever a mensagem 'EFETUAR COMPRA'."""

def main():
    #declaração de variáveis
    quantidade_atual = int()
    quant_max = int()
    quant_min = int()
    quantidade_media = int()
    #entrada de dados
    quantidade_atual = int(input("Quant. atual: "))
    quant_max = int(input("Quant. máxima: "))
    quant_min = int(input("Quant. mínima: "))

    #processamento de dados
    quantidade_media = (quant_max + quant_min) / 2
    if quantidade_atual >= quantidade_media:
        print("NÃO EFETUAR COMPRA")
    else:
        print('EFETUAR COMPRA')
    #saída de dados

    return 0
if __name__ == "__main__":
    main()