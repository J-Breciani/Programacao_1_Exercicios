"""A jornada de trabalho semanal de um funcionário é de 40 horas. O funcionário que trabalhar mais de 40 horas receberá hora extra,
 cujo cálculo é o valor da hora regular com um acréscimo de 50%. Escreva um algoritmo que leia o número de horas trabalhadas em um mês,
 o salário por hora e escreva o salário total do funcionário, que deverá ser acrescido das horas extras, caso tenham sido trabalhadas 
 (considere que o mês possua 4 semanas exatas, totalizando o esperado de 160h/mês).
"""
def main():
    #declaração de variáveis:
    horas_trabalhadas = int()
    salario_hora = int()
    salario_total = int()
    horas_extras = int()
    valor_extra = int()
    #entrada de dados:
    horas_trabalhadas = int(input("Horas trabalhadas no mês: "))
    salario_hora = int(input("Informe o salário por hora: "))

    #processamento de dados:
    valor_extra = 0
    if horas_trabalhadas > 160:
        horas_extras = horas_trabalhadas - 160
        valor_extra = horas_extras * (salario_hora * 1.5)
        horas_trabalhadas = horas_trabalhadas - horas_extras
    salario_total = horas_trabalhadas * salario_hora + valor_extra
    #saída de dados:
    print(f"{salario_total:.1f}")

    return 0
if __name__ == "__main__":
    main()