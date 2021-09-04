import modulo_retorno

def lists(
    integers=[3, 5, 8, 13, 21], 
    reals=[1.5, 2.4, 5.3, 7.2, 10.5], 
    words=["bike", "kitten", "banana", "plant", "laptop"], 
    sentence="I threw my tablet at a banana tree and a kitten fell on my bike"):
    """
    Aqui veremos como utilizar Listas.
    """
    print('\nBem vindo(a) à seção de Listas\n')

    a, b, c, d, e = [float(x) for x in input('Informe 5 números quaisquer de -100 a 100 separados por espaço: ').split()]
    str1, str2, str3, str4, str5 = input('Informe cinco palavras separadas por espaço: ').split()

    'DEFINIÇÃO'
    '''
    Listas são um dos tipos de "containeres de dados" disponíveis em Python. Permite que mais de um item
    seja armazenado em uma única variável indexada. Elas permitem que itens novos sejam inclusos (por
    padrão, sempre no final da lista), outros sejam removidos, e também aceita substituição de itens.

    Lembrando que o índice das listas começa a partir do "0", então uma lista com 10 itens possui um
    índice que vai de "0" (primeiro ítem) à "9" (último ítem). A ordem dos itens em uma lista permanece
    fixa a não ser que se especifique através de métodos como "reverse()" e "sort()".

    Vamos criar abaixo algumas listas com os valores que você informou acima:
    '''

    palavras = [str1, str2, str3, str4, str5]
    # lista de strings
    numeros = [a, b, c, d, e]
    # lista de números
    numlavras = [a, str1, b, str2, c, str3, d, str4, e, str5]
    # lista incluindo números e palavras
    palavras2 = [str1, str2, str3, str4, str5, str1, str2, str3+str4, str5[0], str1+str1[-1]+str1[-1]+str1[-1]]
    # lista incluindo strings repetidas, concatenações de strings e strings em partes
    numeros2 = [a, b, c, d, e, a*a, c*c, e*e, d*d, b*b, a+b*c, (a+b)*c, d/e]
    # lista de números contendo também operações aritméticas como elementos

    print(palavras, '\n', numeros, '\n', numlavras, '\n', palavras2, '\n', numeros2, "\n")

    '''
    Acima podemos notar algumas propriedades que listas permitem:
    
    1. Elas permitem itens repetidos.
    2. Elas permitem itens de tipos diferentes.
    3. O índice está atrelado apenas à posição na lista, não ao conteúdo do item.
    4. É possível concatenar (unir) strings no próprio item da lista. A união é um item só.
    5. É possível incluir operações matemáticas em listas, sendo a conta um item só.

    Podemos usar qualquer tipo de elemento em uma lista, seja números dos tipos integer e float,
    strings, ou valores booleanos (este último não estamos demonstrando no exemplo).
    
    Strings podem ser concatenadas, e podem ser inclusos apenas partes da string (já que estas
    são listas de caracteres, exemplo: str1[0] vai exibir apenas o primeiro caractere da str1).

    Números podem ser adicionados como são, ou como partes de operações aritméticas.
    '''

    print(type(numlavras), "\n")

    '''
    Usando a função type() acima, verificamos que listas são um elemento do tipo "list".

    Outro modo de fazer listas é usando a função "list()". Confira abaixo:
    '''

    alternada = list((str1[0:2], b, e, str2+str5, (a/d)*c, str4[-2], str3))
    # Note os parênteses duplos na construção dessa lista

    print(alternada, "\n")

    'ACESSANDO ITENS NA LISTA'
    '''
    Para acessar os itens de uma lista, podemos nos referir diretamente à seu índice. Exemplo:

    list[0]     # Acessará o primeiro item de list.
    list[0:5]   # Acessará todos os itens do primeiro ao quinto (o índice final é excluído).
    list[-1]    # Acessará o último item da lista (fará uma contagem de trás para frente).
    list[-2]    # Acessará o penúltimo item da lista, -3 o antepenúltimo, e assim sucessivamente.
    list[-4:-1] # Acessará do quarto ao segundo item de trás para frente (excluirá o do -1).

    Com isso podemos utilizar outras funções e operações, como:

    print(list[0])  # Exibirá o primeiro item de list.
    4 * list[2]     # Fará a multiplicação de 4 vezes o elemento contido na list[2] caso
                    # este seja um número.
    list[4] = var   # Atribui um novo valor para o quinto item de list.

    Vamos realizar estas operações acima com alguns itens que você informou anteriormente,
    mais alguns itens que listaremos aqui.
    '''

    lista_ex01 = ['cuscuz','cafézinho', 'frutas', 'empada', 'suco', a, b, c, d, e]
    # Os 5 primeiros itens são strings, os 5 finais são os números informados
    print(lista_ex01[0])      # Exibirá (cuscuz)
    print('---------------------------------------\n')
    print(lista_ex01[-4])     # Exibirá o segundo número que você informou
    print('---------------------------------------\n')
    print(lista_ex01[3:6])    # Exibirá 'empada', 'suco', e os dois primeiros números informados
    print('---------------------------------------\n')
    print(lista_ex01[-1])     # Exibirá o último número informado
    print('---------------------------------------\n')
    print(lista_ex01[-7:-2])  # Exibirá 'empada', 'suco', e os três primeiros números indormados
    print('---------------------------------------\n')
    print(4 * lista_ex01[8])  # Exibirá o resultado de 4 * o quarto número informado
    print('---------------------------------------\n')
    print(lista_ex01[2])      # Exibirá 'frutas'
    lista_ex01[2] = 'abacaxi' # Mudará 'frutas' para 'abacaxi'
    print(lista_ex01[2])      # Exibirá 'abacaxi' como novo item do índice [2]
    print('---------------------------------------\n')

    '''
    Abaixo veremos como conferir se determinado item existe na lista:
    '''
    print('Temos abacaxi aqui?')
    if 'abacaxi' in lista_ex01:
        print('Tem sim! Hora de fazer um suquinho de abacaxi~')
    else:
        print('Eita, tem não... Vou ter de me contentar com ki-suco... :´(')
    print('---------------------------------------\n')

    'MODIFICANDO ITENS DA LISTA'
    '''
    Para modificar um item da lista, referencie-o pelo seu índice.
    Vimos um exemplo acima, confira mais um logo abaixo:
    '''

    lista_ex02 = ['pera', 'uva', 'maçã', 'salada mista', str1, str2, str3, str4, str5]
    print(f'Lista exemplo: {lista_ex02}')
    print('---------------------------------------\n')

    lista_ex02[3] = 'melancia'
    print(f'Quarto item modificado: {lista_ex02}')
    print('---------------------------------------\n')
    ''' O quarto item (salada mista) agora é 'melancia'

    Podemos também modificar mais de um item da lista ao mesmo tempo: '''
    
    lista_ex02[0:4] = ['dois hamburgueres', 'alface', 'queijo', 'molho especial']
    print(f'Receita MC: {lista_ex02}')
    print('---------------------------------------\n')
    ''' Modificamos os itens de 1 à 4 para os itens acima.
    Mas estão faltando alguns, poderíamos tê-los inserido como abaixo: '''

    lista_ex02[0:4] = ['dois hamburgueres', 'alface', 'queijo', 'molho especial', 'cebola', 'picles', 'pão com gergelim']
    print(f'Receita MC completa: {lista_ex02}')
    print('--------------------------------------\n')
    ''' Os itens extras são inseridos após o último item indexado, e antes dos restantes.
    O resultado final terá a receita completa + as 5 strings informadas.

    Mas e se eu odiar MC e quiser outra coisa no lugar? '''

    lista_ex02[0:7] = ['cuscuz', 'charque', 'vinagrete']
    print(f'Refeição de respeito: {lista_ex02}')
    print('---------------------------------------\n')
    # Os elementos não reescritos são eliminados, e os que estavam após estes são trazidos para frente.

    'ADICIONANDO E REMOVENDO ITENS DA LISTA'
    '''
    Vamos criar uma nova lista para vermos a inserção e remoção de itens.

    Para inserir um elemento novo na posição desejada, siga o exemplo abaixo:
    '''

    animais01 = ['gato', 'cachorro', 'papagail', 'pelicano']
    print(f'animais: {animais01}')
    print('---------------------------------------\n')
    # O tema agora é animais.

    animais01.insert(2, 'poiquinho')
    print(f'animais + poiquinho[2]: {animais01}')
    print('---------------------------------------\n')
    
    '''
    No exemplo acima adicionamos um 'poiquinho' entre o cachorro e o papagaio (papagail é proposital).
    Observe a sintaxe do insert(). Ele requer o número do índice, seguido do item:
    >> lista.insert(índice, item)

    Para adicionar um item ao final da lista usamos a função 'append()', que apenas exige o item.
    
    '''
    animais01.append('peixo')
    print(f'animais + peixo: {animais01}')
    print('---------------------------------------\n')
    # Um porém é que a função append() aceita apenas um item.

    '''
    Podemos também fundir duas listas em uma só. Para isso utilizamos a função extend().
    Vamos criar mais outra lista de animais abaixo e uní-la à anterior:
    '''

    animais02 =  ['hamster', 'sagui', 'coruja']

    animais01.extend(animais02)
    # Acima juntamos ambas as listas, os itens da lista adicionada são posicionados ao final.
    print(f'animais demais: {animais01}')
    print('---------------------------------------\n')

    '''
    Algo que notaremos futuramente, a função append() permite mesclar diferentes
    estruturas de dados. Poderíamos ter adicionado uma tupla, set ou mesmo dicionário
    ao final da lista, por exemplo.

    Vamos agora ver como remover itens da lista, seguindo os exemplos acima. Há quatro
    métodos para isso, vamos conferir cada um:
    '''

    animais01.remove('pelicano')
    print(f'O pelicano vôou: {animais01}')
    print('---------------------------------------\n')
    # Para remover especificando o item, usamos remove(). A função aceita apenas um item.

    animais01.pop(3)
    print(f'Agora se foi o papagaio: {animais01}')
    print('---------------------------------------\n')
    ''' Podemos remover especificando o índice usando pop(). Também aceita apenas um item.
    Se usarmos sem argumentos, removerá o último item da lista. '''

    del animais01[2]
    print(f'Até mais, porquinho: {animais01}')
    print('---------------------------------------\n')
    ''' Podemos também utilizar del para remoção de itens pelo índice. A vantagem é que del
    aceita mais de um item, confira abaixo: '''

    del animais01[4:6]
    print(f'Sagui e coruja estão livres: {animais01}')
    print('---------------------------------------\n')
    ''' Lembrando que o último índice utilizado não é considerado. A remoção foi dos índices 4 e 5.
    
    Podemos também utilizar o del para deletar a lista por completo, como em:'''

    del animais02

    # E para limpar a lista por completo, utilizamos clear():

    animais01.clear()
    # Note que não aceita argumentos
    print(f'Os bichos estão soltos! {animais01}')
    print('---------------------------------------\n')


    modulo_retorno.retorno(integers, reals, words, sentence)


if __name__ == '__main__':
    lists()
