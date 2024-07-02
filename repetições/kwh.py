"""
Deseja-se fazer uma pesquisa a respeito do consumo mensal de energia elétrica em
uma determinada cidade. Para isso, são fornecidos os seguintes dados:
- preço do kWh consumido;
- número do consumidor;
- quantidade de kWh consumidos durante o mês;
- código do tipo de consumidor (R-residencial, C-comercial, I-industrial).
O número do consumidor igual a zero deve ser usado como flag de parada. Fazer um algoritmo que:
- leia os dados descritos acima:
- calcule:
a) para cada consumidor, o total a pagar;
b) o maior consumo verificado;
c) o menor consumo verificado;
d) o total do consumo para cada um dos três tipos de consumidores;
e) a média geral de consumo;
- escreva:
a) para cada consumidor, o seu número e o total a pagar;
b) o que foi calculado nos itens b, c, d, e acima especificados.
"""
def main():
    # declaração de variáveis
    preco = float()
    numero = int()
    consumo = int()
    codigo = str()
    pago = float
    total = int()
    total_r = int()
    total_c = int()
    total_i = int()
    maior = int()
    menor = int()
    cont = int()
    media = float()
    # entrada dos dados
    preco = float(input(""))
    numero = int(input(""))
    maior = 0
    menor = 10000000000000

    while (numero != 0):
        consumo = float(input(""))
        total += consumo
        codigo = input("").upper()
        pago = preco * consumo
        print(f"{numero} {pago:.2f}")
        if consumo > maior:
            maior = consumo
        if consumo < menor:
            menor = consumo
        if codigo == "R":
            total_r += consumo
        elif codigo == "C":
            total_c += consumo
        else:
            total_i += consumo
        cont += 1
        numero = int(input(""))
        

    # processamento
    media = total / cont
    

    # saída de dados
    print(f"{maior:.2f}")
    print(f"{menor:.2f}")
    print(f"{total_r:.2f}")
    print(f"{total_c:.2f}")
    print(f"{total_i:.2f}")
    print(f"{media:.2f}")
    return 0
if __name__ == "__main__":
    main()