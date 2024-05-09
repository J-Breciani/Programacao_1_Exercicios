"""
Escreva um algoritmo para ler o número total de eleitores de um município, 
o número de votos brancos, nulos e válidos. Calcular e escrever o percentual 
que cada um representa em relação ao total de eleitores.
"""
def main():

    # declaração de variáveis

    total = int()
    brancos = int()
    nulos = int()
    validos = int()
    p_brancos = float()
    p_nulos = float()
    p_validos = float()

    # entrada dos dados

    total = int(input("Total de eleitores: "))
    brancos = int(input("Total de brancos: "))
    nulos = int(input("Total de nulos: "))
    validos = int(input("Total de eleitores validos: "))


    # processamento 
    
    p_brancos = brancos * 100 / total
    p_nulos = nulos * 100 / total
    p_validos = validos * 100 / total


    # saída
    print(f"BRANCOS = {p_brancos}%")
    print(f"NULOS = {p_nulos}%")
    print(f"VALIDOS = {p_validos}%")



    return 0 

if __name__ == "__main__":
    main()