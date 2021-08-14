import moduloBool, moduloClasse, moduloDateTime, moduloDicionario, moduloExtras, moduloFor
import moduloFuncao, moduloIfElse, moduloInput, moduloLista, moduloMath, moduloObjeto
import moduloSet, moduloString, moduloTipos, moduloTupla, moduloWhile

def indice(integers, reals, words, sentence):
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
        moduloMath.math(integers, reals, words, sentence)
    elif index == '2':
        moduloString.string(integers, reals, words, sentence)
    elif index == '3':
        moduloBool.boolean(integers, reals, words, sentence)
    elif index == '4':
        moduloTipos.types(integers, reals, words, sentence)
    elif index == '5':
        moduloIfElse.ifelse(integers, reals, words, sentence)
    elif index == '6':
        moduloWhile.loopwhile(integers, reals, words, sentence)
    elif index == '7':
        moduloFor.loopfor(integers, reals, words, sentence)
    elif index == '8':
        moduloLista.lists(integers, reals, words, sentence)
    elif index == '9':
        moduloSet.sets(integers, reals, words, sentence)
    elif index == '10':
        moduloTupla.tuples(integers, reals, words, sentence)
    elif index == '11':
        moduloDicionario.dicionary(integers, reals, words, sentence)
    elif index == '12':
        moduloInput.inputs(integers, reals, words, sentence)
    elif index == '13':
        moduloFuncao.functions(integers, reals, words, sentence)
    elif index == '14':
        moduloObjeto.objects(integers, reals, words, sentence)
    elif index == '15':
        moduloClasse.classes(integers, reals, words, sentence)
    elif index == '16':
        moduloDateTime.datetime(integers, reals, words, sentence)
    elif index == '18':
        moduloExtras.extras(integers, reals, words, sentence)
    else:
        exit('Okay, saindo do exemplo. Até mais~')