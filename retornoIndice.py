import indice

def retorno(integers, reals, words, sentence):
    """
    Função para retornar ao índice.
    """
    back = str(input('\nVoltar para o indice? s/n >> '))

    if back == 's':
        indice.indice(integers, reals, words, sentence)
    else:
        exit('Okay, saindo do exemplo. Até mais~')