import modulo_retorno

def string( package = {
    'inteiros': [3, 5, 8, 13, 21], 
    'reais': [1.5, 2.4, 5.3, 7.2, 10.5], 
    'palavras': ["bike", "kitten", "banana", "plant", "laptop"], 
    'frase': "I threw my tablet at a banana tree and a kitten fell on my bike" } ):
    """
    Aqui veremos como manipular strings.
    """

    print('\nBem vindo(a) à seção de Manipulação de Strings\n')
    
    str1, str2, str3, str4, str5 = [str(x) for x in package['palavras']]
    frase = package['frase']
    # Acima só estamos importando alguns dos valores informados no começo
    # e atribuindo variáveis mais aplicáveis aos exemplos

    'Abaixo, vamos conferir na prática o uso de uma das funções mais básicas, print()'

    print('Para exibirmos um texto no terminal, utilizamos a função print() e inserimos')
    print('o conteúdo dentro dos parênteses. Cada print() gera uma nova linha.')
    multi1 = ('''Para criar um texto de múltiplas linhas sem utilizar vários prints, temos 
    algumas opções. Uma delas é utilizar áspas triplas.''')
    multi1 = multi1.replace('    ', '')
    print(multi1)
    print('Este método no entanto trás algumas desvantagens. Por exemplo: depender de uma função\n'
    +'para remover identação que aparecerá no console, (utilizamos a função replace() para isso).\n'
    +'Uma forma mais prática de realizar isso é criando múltiplas linhas entre os parênteses,\n'
    +'mantendo cada linha entre áspas próprias, e as unindo com um "+" na frente de cada nova linha.\n'
    +'Mas neste caso devemos criar uma quebra de linha utilizando "\ n" como neste caso.\n\n'
    +'O Python em geral não faz diferença entre áspas simples e duplas. Ambos servem para armazenar\n'
    +'tanto strings quanto caracteres.')
    print('Utilizando "f" na frente das áspas, podemos inserir variáveis e instruções dentro de chaves "{ }"')
    print(f'Como neste exemplo, onde posso exibir o resultado de 2 + 3 aqui -> {2 + 3} ou até mesmo\n'
    +f'exibir as palavras que inserimos antes aqui -> {str1} {str2} {str3} {str4} {str5} assim vai.\n'
    +'Note que para o texto poder manter essa capacidade, é necessário usar o "f" na frente de cada linha\n'
    +'que precisar exibir algo entre { }, a não ser que você utilize áspas triplas para isso.')

    '''
    Strings são considerados arrays de "strings de 1 caractere"", portanto algumas das operações disponíveis
    para estruturas de dados como listas e afins, também são possíveis utilizando strings.
    Vamos à alguns exemplos abaixo:
    '''
    
    print(f'Acessar a primeira letra de {str1} usando índice "0": str1[0] = {str1[0]}\n'
    # lembrando que índices começam por "0" e seguem a partir daí
    +f'Última letra de {str2} usando str2[-1] = {str2[-1]}\n'
    # Podemos acessar os elementos de trás para frente usando índices negativos, começando por -1
    +f'Penúltima letra de {str3} usando str3[-2] = {str3[-2]}\n'
    +f'cinco primeiros caracteres de "{frase}" usando frase[0:3] = {frase[0:6]}\n'
    # O índice [6] serve como ponto final, e não é exibido.
    +f'Concatenação de {str4} e {str5} usando str4+str5 = {str4+str5}\n'
    # Ao concatenar, podemos inserir caracteres como espaços e afins, colocando entre aspas
    +f'Concatenação de {str1} + espaço + {str3} + vírgula e espaço + {str5} usando\n'
    +f'str1 + " " + {str3} + ", " + {str5} = {str1 + " " + str3 + ", " + str5}\n\n')
    
    '''
    Nos exemplos que vimos até agora, note que usamos o \n para quebra de linhas.
    Existem outros códigos para inserção de conteúdos diversos no código, entre eles:
    \n = Nova linha                     \t = Tabulação
    \' = Áspas simples                  \\ = Barra invertida (a mesma usada aqui)
    \" = Áspas duplas
    E outros mais incomuns abaixo:
    \f = Quebra de página               \a = Bel (apito do computador)
    \b = Backspace                      \v = Tabulação vertical
    '''

    '''
    Outras operações possíveis de se fazer com strings:
    '''
    print(f'{str1} impresso na vertical:')
    for x in str1:
        print(x)
    # ^ Utilizar um loop de "for" para percorrer a string

    print('print("a" in str3)')
    print('a' in str3)
    ''' ^ Conferir se uma palavra ou caractere existe na str1 usando o 
    argumento "in" como em print("a" in str1) Que retornará "True" ou "False"'''

    "Alguns dos Métodos Disponíveis Para Usar com Strings"

    fraSE = 'Todas as vogais desta frase eventualmente serão substituídas por outra vogal. Qual? Não sei...'
    print(fraSE)
    frise = fraSE.replace('a', 'i')
    print(f'frise = fraSE.replace("a", "i") = {frise}')
    frisi = frise.replace('ã', 'i').replace('e', 'i').replace('o', 'i').replace('u', 'i')
    print(f'frisi = frise.replace("ã", "i").replace("e", "i").replace("o", "i").replace("u", "i") = {frisi}')
    '''^ Usar a função .replace(a, b) para substituir todas as instâncias de um determinado
    elemento. Os argumentos de .replace() podem conter múltiplos caracteres, sendo possível
    substituir palavras inteiras. Também podemos combinar replaces em replaces, fazendo 
    replaces aninhados. Outra forma de fazer o mesmo, seria juntar as vogais a serem substituídas
    em uma lista, e varrermos ela com um loop de "for"'''

    print(f'Frase original = {frase}')
    # ^ Vamos exibir a frase que informamos mais cedo
    partes_da_frase = frase.split(' ')
    ''' ^ Usamos .split() para separar a string em cada ocorrência do caractere entre áspas. 
    Espaço nesse caso. É criada uma tupla com os itens, que aqui chamamos de "partes_da_frase"'''
    print(f'partes_da_frase = frase.split(" ") = {partes_da_frase}')
    # ^ Resultado do uso da função .split() acima.
    frase_junta = ('').join(partes_da_frase)
    print(f'frase_junta = ("").join(partes_da_frase) = {frase_junta}')
    ''' ^ Acima utilizamos a função .join() para unir os elementos separados que
    estão armazenados em "partes_da_frase. As áspas são necessárias, mesmo que não
    desejemos nenhum caractere entre cada palavra'''
    frase_normal = (' ').join(partes_da_frase)
    print(f'frase_normal = (" ").join(partes_da_frase) = {frase_normal}')
    ''' ^ Dessa vez designamos espaços na função .join() para que entre cada palavra
    seja inserindo um espaço. Desta forma, frase_normal é o mesmo que "frase"'''
    frase_maiuscula = frase.upper()
    print(f'frase_maiuscula = frase.upper() = {frase_maiuscula}')
    # ^ A função .upper() converte todos os caracteres para maiúsculas
    frase_minuscula = frase.lower()
    print(f'frase_minuscula = frase.lower() = {frase_minuscula}')
    # ^ A função .lower() converte todos os caracteres para minúsculas
    frase_titulo = frase.title()
    print(f'frase_titulo = frase.title() = {frase_titulo}')
    # ^ A função .title() deixa todas as palavras com apenas a primeira letra maiúscula
    frase_capitalizada = frase.capitalize()
    print(f'frase_capitalizada = frase.capitalize() = {frase_capitalizada}')
    # ^ A função .capitalize() faz a string iniciar com maiúscula, e todo o resto é minúsculo
    frase_swap = frase_capitalizada.swapcase()
    print(f'frase_swap = frase_capitalizada.swapcase() = {frase_swap}')
    # ^ A função .swapcase() inverte maiúsculas e minúsculas.
    print(f'frase.count("a") = {frase.count("a")}')
    # ^ A função .count(termo) conta a quantidade de vezes que o elemento entre áspas aparece na string
    print(f'len(frase) = {len(frase)} caracteres')
    # ^ A função len(termo) retorna a quantidade de caracteres na string
    
    '''
    Existem outros métodos disponíveis para usarmos com strings, mas 
    estes são alguns dos mais simples de usar e demonstrar. Podemos encontrar
    mais informações na documentação oficial.
    '''
    
    print('E isso é tudo sobre strings.')    

    modulo_retorno.retorno(package)


if __name__ == '__main__':
    string()
