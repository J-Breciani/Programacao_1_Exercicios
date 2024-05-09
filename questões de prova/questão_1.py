"""
Faça um programa, em Python 3.x, que leia um valor inteiro entre 1000 (MIL) e 9999 (NOVE MIL NOVECENTOS E NOVENTA E NOVE) 
(inclusive os dois valores)  e, utilizando apensa recursos  matemáticos (DIV:  % e MOD: //) que já aprendemos em sala de aula, 
inverta esse número, entregando um valor inteiro como resposta (NÃO É PERMITIDO UTILIZAR QUALQUER RECURSO DE STRING OU MÉTODO/FUNÇÃO 
NÃO APRENDIDOS E USADOS NA DISCIPLINA, EM CASO DE USO, A QUESTÃO TERÁ NOTA ZERO). Ao final, o programa deverá verificar se o valor digitado 
é uma CAPICUA, imprimindo a informação conforme os casos de teste.

CAPICUA: sequência de algarismos que permanece a mesma se lida na ordem direta ou inversa (p.ex., 13231).
"""

def main():

    # declaração de variáveis

    numero = int()
    milhar = int()
    centena = int()
    dezena = int()
    unidade = int()
    resto = int()
    inverso = int
    

    # entrada dos dados

    numero = int(input("Digite um número: "))

    # processamento 

    milhar = numero // 1000
    resto = numero % 1000
    centena = resto // 100
    resto = resto % 100
    dezena = resto // 10
    unidade = resto % 10

    inverso = unidade * 1000 + dezena * 100 + centena * 10 + milhar

    # saída

    if (numero == inverso):
        print(f"O número {numero} é uma capicua.")
    else:
        print(f"O número {numero} não é uma capicua.")

    

    return 0 

if __name__ == "__main__":
    main()