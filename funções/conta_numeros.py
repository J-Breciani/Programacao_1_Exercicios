"""
Faça um programa que conte a incidência de um determinado número [0-9] dentro de um intervalo de valores, 
começando em 0 e o fim do intervalo determinado pelo usuário.
"""

def contar_incidencia(numero, alcance):
    contador = 0
    for i in range(alcance + 1):
        num_str = str(i)
        for elemento in num_str:
            if elemento == str(numero):
                contador += 1
    return contador

def main():
    # declaração:
    numero = int()
    alcance = int()
    incidencias = int()
    # entrada:
    numero = int(input(""))
    alcance = int(input(""))
    # processamento:
    incidencias = contar_incidencia(numero, alcance)
    # saída de dados:
    print(incidencias)

if __name__ == "__main__":
    main()
