def f_ord(x):
    a = ord(x)
    return a
def f_chr(x):
    b = chr(f_ord(x))
    return b

def main():
    # declaração de variáveis
    letra = str()
    # entrada dos dados
    letra = input("")
    # processamento dos dados
    letra = f_chr(letra)
    # saída dos dados
    print(letra)

    return 0
if __name__ == "__main__":
    main()