import modulo_retorno, modulo_bool, modulo_classe, modulo_date_time, \
    modulo_dicionario, modulo_extras, modulo_for, modulo_funcao, modulo_if_else, \
    modulo_input, modulo_lista, modulo_math, modulo_objeto, modulo_set, \
    modulo_string, modulo_tipos, modulo_tupla, modulo_while

def indice(
    integers=[3, 5, 8, 13, 21], 
    reals=[1.5, 2.4, 5.3, 7.2, 10.5], 
    words=["bike", "kitten", "banana", "plant", "laptop"], 
    sentence="I threw my tablet at a banana tree and a kitten fell on my bike"):
    """
    Aqui temos o índice por completo, para melhor organização.
    """

    print('Confira abaixo o índice:\n\n'
    +'~~  Tipos de Dados  ~~~~~~~~~~~~~~~~~~~~~~~~~\n'
    +'[1]\t\tOperações matemáticas\n'
    +'[2]\t\tManipulação de strings\n'
    +'[3]\t\tOperadores booleanos (True/False)\n'
    +'[4]\t\tManipulação de tipos\n'
    +'~~  Sistemas de Decisão e repetição ~~~~~~~~~\n'
    +'[5]\t\tSistemas de decisão if/else/elif\n'
    +'[6]\t\tSistemas de repetição: while\n'
    +'[7]\t\tSistemas de repetição: for\n'
    +'~~  Estruturas de dados  ~~~~~~~~~~~~~~~~~~~~\n'
    +'[8]\t\tEstruturas de dados: Listas\n'
    +'[9]\t\tEstruturas de dados: Sets\n'
    +'[10]\t\tEstruturas de dados: Tuplas\n'
    +'[11]\t\tEstruturas de dados: Dicionários\n'
    +'~~  Funções, Classes e Objetos  ~~~~~~~~~~~~~~~~~~~~~~~~\n'
    +'[12]\t\tInputs do Usuário\n'
    +'[13]\t\tFunções\n'
    +'[14]\t\tObjetos\n'
    +'[15]\t\tClasses\n'
    +'~~  Outros  ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~\n'
    +'[16]\t\tData e hora\n'
    +'[18]\t\tInformações Extra')

    index = str(input('\nPara qual exemplo deseja ir? Digite um número inteiro de 1 à 18:\n>> '))

    if index == '1':
        modulo_math.math(integers, reals, words, sentence)
    elif index == '2':
        modulo_string.string(integers, reals, words, sentence)
    elif index == '3':
        modulo_bool.boolean(integers, reals, words, sentence)
    elif index == '4':
        modulo_tipos.types(integers, reals, words, sentence)
    elif index == '5':
        modulo_if_else.ifelse(integers, reals, words, sentence)
    elif index == '6':
        modulo_while.loop_while(integers, reals, words, sentence)
    elif index == '7':
        modulo_for.loop_for(integers, reals, words, sentence)
    elif index == '8':
        modulo_lista.lists(integers, reals, words, sentence)
    elif index == '9':
        modulo_set.sets(integers, reals, words, sentence)
    elif index == '10':
        modulo_tupla.tuples(integers, reals, words, sentence)
    elif index == '11':
        modulo_dicionario.dicionary(integers, reals, words, sentence)
    elif index == '12':
        modulo_input.inputs(integers, reals, words, sentence)
    elif index == '13':
        modulo_funcao.functions(integers, reals, words, sentence)
    elif index == '14':
        modulo_objeto.objects(integers, reals, words, sentence)
    elif index == '15':
        modulo_classe.classes(integers, reals, words, sentence)
    elif index == '16':
        modulo_date_time.datetime(integers, reals, words, sentence)
    elif index == '18':
        modulo_extras.extras(integers, reals, words, sentence)
    else:
        exit('Okay, saindo do exemplo. Até mais~')


if __name__ == '__main__':
    indice()
