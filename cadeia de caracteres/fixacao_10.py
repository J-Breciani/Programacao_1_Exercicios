"""
Faça um programa que, dado 10 matrículas de estudantes, informe o ano e o semestre de entrada, do mesmo.

"""

def main():
    # declaração das variáveis
    matricula = str()
    ano = str()
    semestre = str()

    # entrada, processamento e saída dos dados
    for i in range (10):
        matricula = input("Informe sua matrícula: ")
        ano = matricula[0:4]
        semestre = matricula[4:5]
        print(f"Ano: {ano} Semestre: {semestre}")


    return 0

if __name__ == "__main__":
    main()