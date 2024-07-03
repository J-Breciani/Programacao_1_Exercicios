"""
Utilizando strings e reconstrução de strings, elabore um programa em python que simule um jogo de forca.

O programa deve solicitar uma palavra ao usuário desafiante (pesquise uma forma de apagar a "tela" console logo após a palavra chave ser infomada)

O usuário desafiado tem 6 chances de erro para tentar acertar a palavra. Apenas os erros serão contabilizados.

Detalhes do jogo:

O jogo termina quando o usuário usar as seis chances de erro ou quando ganhar o jogo.

Caso o usuário vença, deve ser informado o número de jogadas que ele tentou (inclusive os erros)

Apresente o sublinhado de tamanho da palavra procurada, use espaços em branco entre os sublinhados, pra facilitar a visualização

A cada jogada certa a letra correta deve aparecer na posição do sublinhado, onde ela está na palavra chave.

A cada jogada errada, as letras incorretas devem ser apresentadas abaixo dos sublinhados.

OBS:

Para testar tire as interações dos inputs

Não é permitido a utilização de LISTAS
"""
def f_geraForca(s):
    nova = ""
    for i in range(len(s)):
        nova += "_"
    return nova

def f_print(f):
    for i in range(len(f)):
        print(f[i],end=" ")
    print()

def f_verificaLetra(s,l,f):
    nova = ""
    for i in range(len(s)):
        if (s[i] == l):
            nova += s[i]
        else:
            nova += f[i]
    return nova

def f_forca(s,f,e):
    if (f == s):
        return 1
    elif (e == 6):
        return 2
    else:
        return 0

def f_errada(l,s):
    for i in range(len(s)):
        if (l == s[i]):
            return False
    return True

def main():
    erradas = ""
    jogadas = 1
    erros = 0
    #segredo = "CAIXA"
    segredo = input().upper()
    forca = f_geraForca(segredo)
    f_print(forca)
    letra = input().upper()
    if (f_errada(letra,segredo)):
        erros += 1
        erradas += letra
    forca = f_verificaLetra(segredo,letra,forca)
    continua = f_forca(segredo,forca,erros)
    while (continua == 0):
        f_print(forca)
        print(erradas)
        letra = input().upper()
        jogadas += 1
        if (f_errada(letra,segredo)):
            erros += 1
            erradas += letra
        forca = f_verificaLetra(segredo,letra,forca)
        continua = f_forca(segredo,forca,erros)        
    if (continua == 1):
        f_print(segredo)
        print(f'Parabéns, você ganhou com {jogadas} jogadas ')
    elif (continua == 2):
        f_print(forca)
        print(erradas)
        print(f'Que pena, você não acertou a palavra {segredo}')
    return 0

if __name__ == "__main__":
    main()