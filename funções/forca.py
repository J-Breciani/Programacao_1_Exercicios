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
def f_forca(palavra):
    # declaração de variáveis:
    chute = str()
    palavra_formada = str()
    tentativas = int()
    erros = str()
    letras_acertadas = str()
    dica = str()
    flag = str()
    # entrada de dados: 
    tentativas = 0
    for i in range(len(palavra)):
        dica += "_ "
    print(dica)
    # processamento: 
    while(tentativas <= 6 or flag != palavra):
        chute = input("").upper()
        if (chute in palavra):
            letras_acertadas += chute
        else:
            tentativas += 1
            erros += chute
        palavra_formada = ""
        for i in range(len(palavra)):
            if palavra[i] in letras_acertadas:  
                palavra_formada += palavra[i] + " "
            else:
                palavra_formada += "_ "
        print(palavra_formada)
        print(erros)
        for a in len(palavra_formada):
            if (palavra_formada[i] != " "):
                flag += palavra_formada[a]
    # saída de dados:
    if (palavra_formada == palavra):
        resultado = (f"Parabéns, você ganhou com {tentativas} jogadas")
    else:
        resultado = (f"Que pena, você não acertou a palavra {palavra}")
    return resultado

def main():

    # declaração das variáveis:
    palavraSecreta = str()
    forca = str()
    # entrada de dados:
    palavraSecreta = input("").upper()
    # processamento:
    forca = f_forca(palavraSecreta)
    # saída dos dados:
    print(forca)

    return 0 

if __name__ == "__main__":
    main()