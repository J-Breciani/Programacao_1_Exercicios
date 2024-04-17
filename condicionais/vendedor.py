"""Ler o salário fixo e o valor das vendas efetuadas pelo vendedor de uma empresa.
 Sabendo-se que ele recebe uma comissão de 3% sobre o total das vendas até R$ 1.500,00 mais 5% sobre o que ultrapassar este valor,
   calcular e escrever o seu salário total."""
def main():
    #declaração de variáveis:
    salario_fixo = float()
    vendas = float
    total = float()
    resto = float()
    #entrada de dados:
    salario_fixo = float(input("Salário fixo: "))
    vendas = float(input("Valor das vendas: "))
    #processamento de dados:
    if( vendas <= 1500):
        total = salario_fixo + (vendas * 0.03)
    else:
        resto = vendas - 1500
        total = salario_fixo + (1500 * 0.03) + (resto * 0.05)
    #saída de dados:
    print(f"{total:.1f}")

    return 0 
if __name__ == "__main__":
    main()