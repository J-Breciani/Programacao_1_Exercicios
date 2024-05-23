"""
Faça um programa que leia a matrícula de um estudante e imprima a sigla de seu curso
"""

def main():

    # declaração de variáveis: 
    matricula = str()
    letras =str()

    # entrada de dados:
    matricula = input("Digite a matrícula: ").upper()

    # processamento:
    for i in range(len(matricula)):
        if (i >= 5 and i <=8):
            letras += matricula[i] 
  
    # saída de dados: 
    print(letras)



    return 0 

if __name__ == "__main__":
    main()