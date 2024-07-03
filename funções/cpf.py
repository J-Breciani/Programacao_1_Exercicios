"""
Faça um programa que, dados os nove primeiros números e os dois dígitos verificadores, informe se o CPF é válido ou inválido.
"""

def f_limpaCPF(cpf):
    # declaração de variáveis:
    numeros = str()
    # entrada:
    numeros = ""
    # processamento: 
    for i in range(len(cpf)):
        if (cpf[i] != "." and cpf[i] != "-"):
            numeros += cpf[i]
    return numeros

def f_dv1(cpf):
    multiplicador = 10
    total = 0
    for i in range(len(cpf)):
        total += int(cpf[i])*multiplicador
        multiplicador -= 1
    resto = total % 11
    if (resto < 2):
        return 0
    else:
        return 11 - resto
    
def f_dv2(cpf):
    multiplicador = 11
    total = 0
    for i in range(len(cpf)):
        total += int(cpf[i])*multiplicador
        multiplicador -= 1
    resto = total % 11
    if (resto < 2):
        return 0
    else:
        return 11 - resto    

def f_verifica(cpf):
    cpf = f_limpaCPF(cpf)
    verificador = cpf[9:]
    teste_cpf = cpf[:9]    
    dv1 = str(f_dv1(teste_cpf))
    teste_cpf += dv1
    dv2 = str(f_dv2(teste_cpf))
    if (verificador == dv1+dv2):
        return True
    else:
        return False
    
def main():
    #declaração :
    cpf = str()
    # entrada de dados:
    cpf = input("")
    # processamento e saída de dados:
    if (f_verifica(cpf)):
        print("CPF VÁLIDO")
    else:
        print("CPF INVÁLIDO")
    return 0
    
if __name__ == "__main__":
    main()        