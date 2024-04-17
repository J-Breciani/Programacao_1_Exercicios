"""Tendo como dados de entrada a altura e o sexo (M ou F) de uma pessoa, calcule e mostre seu peso ideal,
 utilizando as seguintes fórmulas: - para sexo masculino: peso ideal = (72.7 * altura) - 58 – 
 para sexo feminino: peso ideal = (62.1 * altura) - 44.7
"""
def main():
    #declaração de variáveis:
    sexo = str()
    altura = float()
    peso_ideal = float
    #entrada de dados:
    sexo = input("Sexo feminino ou masculino: [F/M] ").upper()
    altura = float(input("Altura em metros: "))
    #processamento de dados:
    if (sexo == "M"):
        peso_ideal = (72.7 * altura) - 58
    else: 
        peso_ideal = (62.1 * altura) - 44.7
    #saída de dados:
    print(f"{peso_ideal:.3f}")
    return 0 

if __name__ == "__main__":
    main()