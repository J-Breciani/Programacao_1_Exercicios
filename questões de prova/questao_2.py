"""
"""

def main():

    # declaração de variáveis

    a = int()
    b = int()
    c = int()
    d = int()
    soma = int()

    # entrada dos dados

    a = int(input("A: "))
    b = int(input("B: "))
    c = int(input("C: "))
    d = int(input("D: "))

    # processamento 

    if (a >= b and a >= c and a >= d):
        soma = b + c + d
    elif(b >= a and b >= c and b >= d):
        soma = a + c + d
    elif(c >= a and c >= b and c >=d):
        soma = a + b + d
    else: 
        soma = a + b + c
    # saída

    print(soma)

    return 0 

if __name__ == "__main__":
    main()