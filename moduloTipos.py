import retornoIndice

def types(integers, reals, words, sentence):
    """
    Aqui veremos como manipular tipos.
    """
    print('\nBem vindo(a) à seção de Manipulação de Tipos\n')

    '''Nesta sessão veremos como manipular os tipos de variáveis, e como elas funcionam.
    Antes de começarmos, vou pedir que me dê algumas variáveis de tipos específicos.'''

    str1 = str(input('Insira uma palavra qualquer ou frase, mas não exagere no tamanho: '))
    a = int(input('Me informe agora um número inteiro, independente se é positivo ou negativo: '))
    x = float(input('Por fim, me informe um número com casas decimais: '))

    '''Em Python trabalhamos com diversos tipos de dados diferentes.
    Abaixo, uma lista deles para fins de curiosidade:'''

    print(f'Textos:\t\t\tStrings (str)')
    print(f'Números:\t\tIntegers (int), Float (float), Complex (complex)')
    print(f'Sequências:\t\tListas (list), Tuplas (tuple), Comprimentos (range)')
    print(f'Mapeamentos:\tDicionários (dict)')
    print(f'Sets:\t\t\tSets (set), Set Imutável (frozenset)')
    print(f'Booleano:\t\tBool (bool)')
    print(f'Binários:\t\tBytes (bytes), Array de Bytes (bytearray), Vista de Memória (memoryview)')

    '''
    Para descobrir o tipo de algum elemento, use a seguinte função:
    print(type(x))

    Vamos fazer isso com os elementos que foram informados acima, mas vou usar um comando levemente
    diferente, para que possamos ver as mudanças uma a uma:
    print(str1, "=", type(str1)) =
    '''

    print(str1, '=', type(str1))
    print('print(a, "=", type(a)) = ')
    print(a, '=', type(a))
    print('print(x, "=", type(x)) = ')
    print(x, '=', type(x))

    '''Neste exemplo vamos conferir o que é "Casting".
    Casting é basicamente converter um tipo para o outro.
    É possível fazer isso com elementos dos tipos String e Números, para isso usamos:
    variável = tipo(variável)

    Vamos converter os tipos dos elementos informados antes?
    Esta operação será feita fora deste print atual, mas usaremos:
    a = float(a)
    x = int(x)'''

    a = float(a)
    x = int(x)

    '''Voltando à programação normal abaixo:
    print(a, "=", type(a)) = '''
    print(a, '=', type(a))
    'print(x, "=", type(x)) = '
    print(x, '=', type(x))

    '''Note que ele arredondou o número 'x', e acrescentou um '.0' após o número 'a'.
    Agora vamos converter ambos para strings:'''

    a = str(a)
    x = str(x)

    '''Último resultado dos testes de laboratório abaixo:
    print(a, "=", type(a)) = '''
    print(a, '=', type(a))
    'print(x, "=", type(x)) = '
    print(x, '=', type(x))

    '''E agora todos são strings.
    Isto encerra o conteúdo sobre manipulações de tipos.'''

    retornoIndice.retorno(integers, reals, words, sentence)