import modulo_indice

def retorno(
    integers=[3, 5, 8, 13, 21], 
    reals=[1.5, 2.4, 5.3, 7.2, 10.5], 
    words=["bike", "kitten", "banana", "plant", "laptop"], 
    sentence="I threw my tablet at a banana tree and a kitten fell on my bike"):
    """
    Função para retornar ao índice.
    """
    back = str(input('\nVoltar para o indice? s/n >> '))

    if back == 's':
        modulo_indice.indice(integers, reals, words, sentence)
    else:
        exit('Okay, saindo do exemplo. Até mais~')


if __name__ == '__main__':
    retorno()
