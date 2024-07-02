"""
Fazer um programa que:

- Para cada uma das N turmas (N diversas turmas), calcule a porcentagem de ausência dos alunos. Imprima a identificação da turma e a porcentagem, calculada,
 de ausência de alunos com duas casas decimais.

- Determine e imprima qual turma teve a (primeira) maior porcentagem de ausência. Imprima a turma e sua respectiva porcentagem com duas casas decimais.

- Determine e imprima qual turma teve a (primeira) menor porcentagem de ausência. Imprima a turma e sua respectiva porcentagem com duas casas decimais.

- Determine e imprima quantas turmas tiveram porcentagem de ausência superior a 20%.
"""
def main():
    # declaração de variáveis:
    n = int()
    id = str()
    alunos = int()
    matricula = str()
    frequencia =str()
    ausencia = int()
    media = float()
    id_maior = str()
    maior = float()
    id_menor = str()
    menor = float()
    superior = int()

    # entrada dos dados:
    n = int(input(""))
    maior = 0
    menor = 100

    # processamento:

    for a in range (n):
        ausencia = 0
        id = input("")
        alunos = int(input(""))
        for i in range(alunos):
            matricula = input("")
            frequencia = input("").upper()
            if frequencia == "A":
                ausencia += 1
        media = ausencia * 100 / alunos
        if media > 20:
            superior += 1
        if media > maior:
            id_maior = id
            maior = media
        if media < menor:
            id_menor = id
            menor = media
        print(f"TURMA = {id} AUSENCIA = {media:.2f}%")

    # saída dos dados:

    print(f"TURMA COM MAIOR % DE AUSENCIA = {id_maior} AUSENCIA = {maior:.2f}%")
    print(f"TURMA COM MENOR % DE AUSENCIA = {id_menor} AUSENCIA = {menor:.2f}% ")
    print(f"{superior} TURMAS COM % DE AUSENCIA SUPERIOR A 20%")
    return 0
if __name__ == "__main__":
    main()