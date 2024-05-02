def main():
    #declaração:
    
    dia = int()
    mes = int()
    outono = bool()
    verao = bool()
    inverno = bool()
    primavera = bool()
    
    #emtrada:
    
    dia = int(input("Dia: "))
    mes = int(input("Mês: "))
    
    #processamento dos dados:
    
    outono = (dia >= 21 and mes == 3) or mes == 4 or mes == 5 or (dia <= 20 and mes == 6)
    inverno = (dia >= 21 and mes == 6) or mes == 7 or mes == 8 or (dia <= 22 and mes == 9)
    primavera = (dia >= 23 and mes == 9) or mes == 10 or mes == 11 or (dia <= 20 and mes == 12)
    verao = (dia >= 21 and mes == 12) or mes == 1 or mes == 2 or (dia <= 20 and mes == 3)
    
    #saída:
    if (outono):
        print (f"O dia {dia}/{mes} cai no Outono")
    elif(inverno):
        print (f"O dia {dia}/{mes} cai no Inverno")
    elif(primavera):
        print (f"O dia {dia}/{mes} cai na Primavera")
    elif(verao):
        print (f"O dia {dia}/{mes} cai no Verão")
    else:
        print("Data Inválida")
    
    return 0
    
if __name__ == "__main__":
    main()