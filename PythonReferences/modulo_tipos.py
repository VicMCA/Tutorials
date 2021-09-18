import modulo_retorno

def types( package = {
    'inteiros': [3, 5, 8, 13, 21], 
    'reais': [1.5, 2.4, 5.3, 7.2, 10.5], 
    'palavras': ["bike", "kitten", "banana", "plant", "laptop"], 
    'frase': "I threw my tablet at a banana tree and a kitten fell on my bike" } ):
    """
    Aqui veremos como manipular tipos.
    """
    print('\nBem vindo(a) à seção de Manipulação de Tipos\n')

    '''Nesta sessão veremos como manipular os tipos de variáveis, e como eles funcionam.
    Antes de começarmos, vamos importar os valores de antes e converter para uma forma
    mais prática: '''

    a, b, c, d, e = [int(x) for x in package['inteiros']]
    v, w, x, y, z = [float(x) for x in package['reais']]
    str1, str2, str3, str4, str5 = [str(x) for x in package['palavras']]
    frase = package['frase']

    '''Em Python trabalhamos com diversos tipos de dados diferentes.
    Abaixo, uma lista deles para fins de curiosidade:

    Textos:             Strings (str)
    Números:            Integers (int), Float (float), Complex (complex)
    Sequências:         Listas (list), Tuplas (tuple), Comprimentos (range)
    Mapeamentos:        Dicionários (dict)
    Sets:               Sets (set), Set Imutável (frozenset)
    Booleano:           Bool (bool)
    Binários:           Bytes (bytes), Array de Bytes (bytearray), Vista de Memória (memoryview)
    '''


    '''
    Para descobrir o tipo de algum elemento, use a seguinte função:
    print(type(x))

    Vamos fazer isso com alguns dos elementos que foram informados acima, mas 
    vou usar um comando levemente diferente, para que possamos ver as mudanças uma a uma:
    print(variavel, " = ", type(variavel)) =
    '''

    print(str1, ' = ', type(str1))
    print(str2, ' = ', type(str2))
    print(str4, ' = ', type(str4))
    print(a, ' = ', type(a))
    print(d, ' = ', type(d))
    print(e, ' = ', type(e))
    print(x, ' = ', type(x))
    print(y, ' = ', type(y))
    print(v, ' = ', type(v))
    print(frase, ' = ', type(frase))
    print(package['inteiros'], ' = ', type(package['inteiros']))
    print(package['palavras'], ' = ', type(package['palavras']))

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
    z = str(z)

    print(a, '=', type(a))
    # A variável "a" agora é um número float, com .0 para o termo decimal
    print(x, '=', type(x))
    # A variável "x" agora foi arredondada para um número int
    print(z, '=', type(z))
    # A variável "z" foi convertida para uma string

    '''Isto encerra o conteúdo sobre tipos.'''

    modulo_retorno.retorno(package)


if __name__ == '__main__':
    types()
