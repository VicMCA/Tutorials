import modulo_retorno, modulo_bool, modulo_classe, modulo_date_time, \
    modulo_dicionario, modulo_extras, modulo_for, modulo_funcao, modulo_if_else, \
    modulo_input, modulo_lista, modulo_math, modulo_objeto, modulo_set, \
    modulo_string, modulo_tipos, modulo_tupla, modulo_while

def indice( package = {
    'inteiros': [3, 5, 8, 13, 21], 
    'reais': [1.5, 2.4, 5.3, 7.2, 10.5], 
    'palavras': ["bike", "kitten", "banana", "plant", "laptop"], 
    'frase': "I threw my tablet at a banana tree and a kitten fell on my bike" } ):
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
        modulo_math.math(package)
    elif index == '2':
        modulo_string.string(package)
    elif index == '3':
        modulo_bool.boolean(package)
    elif index == '4':
        modulo_tipos.types(package)
    elif index == '5':
        modulo_if_else.ifelse(package)
    elif index == '6':
        modulo_while.loop_while(package)
    elif index == '7':
        modulo_for.loop_for(package)
    elif index == '8':
        modulo_lista.lists(package)
    elif index == '9':
        modulo_set.sets(package)
    elif index == '10':
        modulo_tupla.tuples(package)
    elif index == '11':
        modulo_dicionario.dicionary(package)
    elif index == '12':
        modulo_input.inputs(package)
    elif index == '13':
        modulo_funcao.functions(package)
    elif index == '14':
        modulo_objeto.objects(package)
    elif index == '15':
        modulo_classe.classes(package)
    elif index == '16':
        modulo_date_time.datetime(package)
    elif index == '18':
        modulo_extras.extras(package)
    else:
        exit('Okay, saindo do exemplo. Até mais~')


if __name__ == '__main__':
    indice()
