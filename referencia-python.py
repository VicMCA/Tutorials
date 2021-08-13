#!/usr/bin/env python3

def main():
    """
    Acima é o começo da função principal.
    E esta é a mini-documentação para ela, acessível chamando print(main.__doc__)
    O mesmo vale pra outras funções também. Aspas duplas são a forma recomendada.
    """

    print('\nBem-vindo(a) ao guia rápido de "Como Fazer X" em Python.\n'
    +'Este é um guia com exemplos para servir de referência sobre como fazer diversas coisas.\n'
    +'As explicações se encontram nos comentários deste código.\n'
    +'Antes de começarmos, vou pedir que você insira algumas informações para usarmos nos exemplos.')

    inicio = str(input('Caso deseje encerrar o programa, digite "q". Para continuar aperte "enter": '))
    inicio = inicio.lower()
    if inicio == 'q':
        exit('Okay, saindo do exemplo. Até mais~')
    
    ''' Abaixo (e acima) vemos o uso de algumas ferramentas que veremos nos capítulos a seguir, entre elas:
    1. Atribuição de variáveis, explicada no módulo de "Manipulação de tipos"
    2. Estrutura de repetição "for", explicada em seu módulo "Sistemas de repetição: for"
    3. Recebendo dados do usuário com "input()", também explicada em seu módulo "Inputs do Usuário"
    4. A função ".split()", explicada no módulo sobre "Inputs do Usuário"
    5. Criação de tuplas, explicada em seu módulo "Estruturas de dados: Tuplas"
    6. Uso de estruturas condicionais no módulo "Sistemas de decisão if/else/elif"
    7. Chamada de funções, no módulo "Funções" '''

    a, b, c, d, e = [int(x) for x in input('Digite cinco números inteiros separados por espaço:\n>> ').split()]
    inteiros = (a, b, c, d, e)
    v, w, x, y, z = [float(x) for x in input('Digite cinco números reais separados por espaço:\n>> ').split()]
    reais = (v, w, x, y, z)
    w1, w2,  w3, w4, w5 = input('Digite cinco palavras com mais de 4 letras, separados por espaço:\n>> ').split()
    palavras = (w1, w2, w3, w4, w5)
    frase = input('Digite uma frase que contenha pelo menos uma das palavras informadas:\n>> ')

    start = str(input('Muito bem! Vamos agora conferir o índice? s/n >> '))

    if start == 'n':
        exit('Okay, saindo do exemplo. Até mais~')

    indice()


def math(integers = (0, 0, 0, 0, 0), reals = (0, 0, 0, 0, 0)):
    """
    Esta função serve para exemplo de diversas operações matemáticas possíveis e suas sintaxes.
    """
    print('\nBem vindo(a) à seção de Operações Matemáticas\n')

    a, b, c, d, e = [integers[x] for x in integers]
    v, w, x, y, z = [reals[x] for x in reals]

    # Acima estamos criando variáveis a partir de elementos em uma lista. Vemos isso em outro módulo.

    print(f'Os números informados foram:'
    +f'a = {a}\tb = {b}\tc = {c}\td = {d}\te = {e}'
    +f'v = {v}\tw = {w}\tx = {x}\ty = {y}\tz = {z}'
    +'E abaixo faremos algumas operações básicas com eles.\n')

    # Para adição, apenas somamos os números no formato de n1 + n2, como no exemplo abaixo:
    print(f'Adição: {a} + {b} = {a + b} | {c} + {d} + {e} = {c + d + e}')
    print(f'Adição: {v} + {w} = {v + w} | {x} + {y} + {z} = {x + y + z}')
    print('\n')
    # Para subtração é igualmente simples, n1 - n2, como abaixo:
    print(f'Subtração: {e} - {d} = {e - d} | {c} - {b} - {a} = {c - b - a}')
    print(f'Subtração: {z} - {y} = {z - y} | {x} - {w} - {v} = {x - w - v}')
    print('\n')
    # Para multiplicação, n1 * n2:
    print(f'Multiplicação: {e} * {a} = {e * a} | {x} * {b} * {y} = {x * b * y}')
    print(f'Multiplicação: {v} * {z} = {v * z} | {c} * {w} * {d} = {c * w * d}')
    print('\n')
    # Para divisão, n1 / n2:
    print(f'Divisão: {d} / {b} = {d / b} | {e} / {c} / {a} = {e / c / a}')
    print(f'Divisão: {y} / {w} = {y / w} | {z} / {x} / {v} = {z / x / v}')
    print('\n')
    # Alternativamente, n1 // n2 para termos resultado arredondado:
    print(f'Divisão com resultado arredondado: {d} // {b} = {d // b} | {e} // {c} // {a} = {e // c // a}')
    print(f'Divisão com resultado arredondado: {y} // {w} = {y // w} | {z} // {x} // {v} = {z // x // v}')
    print('\n')
    # Para módulo, n1 % n2:
    print(f'Módulo: {a} % 2 = {a % 2}')
    print(f'Módulo: {b} % {c} = {b % c}')
    print('\n')

    "Abaixo veremos exponenciação, radicação, percentagem e arredondamento."

    # Para exponenciação, podemos usar n1 ** n2:
    print(f'Exponenciação: {b} ** {c} = {b ** c}')
    print(f'Exponenciação: {w} ** {x} = {w ** x}')
    print('\n')
    # Alternativamente usamos a função pow(n1, n2), como abaixo:
    print(f'Exponenciação: pow({d}, {e}) = {pow(d, e)}')
    print(f'Exponenciação: pow({y}, {z}) = {pow(y, z)}')
    print('\n')
    # Usando pow(x, y) podemos calcular o módulo (restante de uma divisão) usando pow(x, y, z)
    # Neste caso, será o módulo de x^y quando dividido por z.

    # Para radicação, usamos n1 ** 1/n2:
    print(f'Radicação: {d} ** 1/{a} = {d ** 1/a}')
    print(f'Radicação: {b} ** 1/{e} = {b ** 1/e}')

    # Basicamente, elevamos um número à 1/outro número. Bastante versátil.

    # Existe uma função para raiz quadrada usando a biblioteca math, importando com 'import math'
    # Para chamar essa função se usa math.sqrt(x,y)

    # Para percentual, usamos regra de 3, na fórmula "(percentagem / 100) * total"
    print(f'Percentual "{a} por cento de {d}: ({a} / 100) * {d} = {(a / 100) * d}')
    print(f'Percentual "{z} por cento de {c}: ({z} / 100) * {c} = {(z / 100) * c}')

    # Para arredondamento, usamos a função round(n1, n2)
    print(f'Arredondamento: round({w} * {x} + {y} / {z}, 2) = {round(w * x + y / z, 2)}')
    print(f'Sem arredondamento: ({w} * {x} + {y} / {z}, 2) = {w * x + y / z}')

    """
    E isso é tudo sobre operações aritméticas.
    """

    retorno_indice()


def string():
    """
    Aqui veremos como manipular strings.
    """

    print('\nBem vindo(a) à seção de Manipulação de Strings\n')
    
    '''
    Abaixo, para imprimir um texto multilinha removendo a identação causada
    por conta da organização do código em Python, armazenamos o texto em uma variável,
    em seguida usamos a função replace() com os argumentos ('    ') para a identação,
    e o argumento ('') para indicar nada. Com isso a função trocará a identação para nada.
    '''
    intro = ('''Podemos usar áspas triplas para
    fazer um texto multilinha\n''')

    intro = intro.replace('    ', '')
    
    print(intro)

    str1, str2 = input('Informe duas palavras ou frases com mais de 4 letras, separados por vírgula: ').split(',')

    # Strings são considerados arrays de "strings de 1 caractere"", portanto podemos fazer coisas como:
    exemplo01 = (f'''Primeira letra de {str2} usando str2[0] = {str2[0]}
    Última letra de {str1} usando str1[-1] = {str1[-1]}
    Penúltima letra de {str2} usando str2[-2] = {str2[-2]}
    Três primeiros caracteres de {str2} usando str2[0:3] = {str2[0:3]}
    Concatenação de {str1} e {str2} usando str1+str2 = {str1+str2}
    Concatenação de {str1} + turubom usando str1+"turubom" = {str1+"turubom"}''')
    print(exemplo01.replace('    ', ''))
    # Acima trocamos a tabulação pelo nada diretamente no print.

    # Loops como o abaixo para imprimir a string na vertical fazendo "for x in str1":

    print(f'{str1} impresso na vertical:')
    for x in str1:
        print(x)

    # Descobrir o tamanho de str2 usando len(str2)
    print(f'len(str2) = {len(str2)}')

    # Conferir se uma palavra ou caractere existe na str1 usando print("a" in str1)
    print('print("a" in str1)')
    print('a' in str1)
    # É possível usar o retorno de True ou False do "x" in "y" para realizar condições.

    # Também é possível usar "not in", com print("a" not in str2) para retornar o valor booleano.
    print('print("a" not in str1)')
    print('a' not in str1)

    """
    E isso é tudo sobre strings.
    """

    retorno_indice()


def boolean():
    """
    Nesta seção, veremos como funcionam operadores booleanos.
    """
    print('\nBem vindo(a) à seção de Operações Booleanas\n')
    '''Há diversos modos de conferir se  um valor é verdadeiro ou falso. Vamos conferir alguns modos.
    Antes de vermos alguns, vamos criar algumas variáveis para experimentar?'''

    print('Informe dois números inteiros iguais e um diferente, e separe-os por espaço:')
    a, b, c = [int(x) for x in input('>> ').split()]
    print('Informe três palavras/frases e separe-os por vírgula;')
    str1, str2, str3 = input('Faça uma delas ser parte de outra, ex "estou" está contido em "estourando": ').split(',')

    '''
    Para conferir se uma expressão é igual, maior ou menor que outra, basta realizar uma
    comparação direta usando os operadores abaixo:
    == significa "igual à"\t\t\t!= significa "diferente de"
    > significa "maior que"\t\t\t< significa "menor que"
    >= significa "maior ou igual\t <= significa "menor ou igual"

    Vamos agora fazer algumas comparações, começando abaixo:
    '''

    print(f'{str1} é igual a {str1}? {str1 == str1}')
    print(f'{str2} é diferente de {str2}? {str2 != str2}')
    print(f'{str3} é igual a {str1}? {str3 == str1}')
    print(f'{str2} é igual a {str3}? {str2 == str3}')
    print(f'{str1} é diferente de {str3}? {str1 != str3}')
    print(f'{str3} é diferente de {str2}? {str3 != str2}')

    'Podemos também comparar os tamanhos de strings, confira:'

    print(f'{str1} é maior que {str2}? {str1 > str2}')
    print(f'{str2} é maior que {str3}? {str2 > str3}')
    print(f'{str3} é menor que {str1}? {str3 < str1}')

    'O mesmo vale para números, confira operações com os números que você informou:'
    print(f'{a} é maior que {a}? {a > a}')
    print(f'{b} é menor que {b}? {b < b}')
    print(f'{c} é igual a {c}? {c == c}')
    print(f'({a} + {b}) é maior que {c}? {(a + b) > c}')

    '''
    E por aí vai. Podemos também usar o comando "print()" para imprimir o valor booleano.
    A função "bool()" lhe permite verificar o valor booleano de qualquer variável. Sintaxe abaixo:
    print(bool(15))
    print(bool('olá''))
    print(bool(str1))

    Os valores de diversas coisas são considerados "True" por padrão, por exemplo:
    1. Strings são consideradas "True", mas se forem vazias são "False"
    2. Qualquer número é considerado "True", exceto o número zero, que é "False"
    3. Listas, tuples, sets e dicionários são "True" a menos que estejam vazios.

    E isso é tudo sobre operações booleanas.
    '''

    retorno_indice()


def types():
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

    retorno_indice()


def ifelse():
    """
    Aqui veremos como utilizar os argumentos If e Else.
    """
    print('\nBem vindo(a) à seção de Sistemas de Decisão\n')

    ''' Usamos "if", "else" e "elif" para trabalharmos com condições.
    Todas as condicionais podem ser usadas com operadores matemáticos e lógicos.
    >= para maior ou igual    |   > para maior    |    == para igual   |
    <= para menor ou igual    |   < para menor    |    and para 'e'    |    or para 'ou'
    O "if" é sempre utilizado no começo, e pode receber uma cláusula "elif" para else/if,
    no qual devemos especificar também qual a próxima condição. O "else" pode ser utilizado
    no final para todos os outros casos não abordados nos "if" e "elif" anteriores.

    Exemplo da sintaxe abaixo:

    if argumento comparativo argumento:
        código a ser executado
    elif argumento comparativo argumento:
        código a ser rodado
    else:
        código a ser rodado

    Vamos experimentar abaixo:
    '''

    a, b, c = [float(x) for x in input('Informe três números quaisquer separados por espaço: ').split()]
    str1, str2, str3 = input('Informe três palavras separadas por espaço: ').split()

    'Vamos criar abaixo algumas decisões a serem tomadas com os elementos informados.'

    if a == b and b == c:
        print(str1, str2,  str3, 'JACKPOT')
    elif a != b and b != c and c != a:
        print(str3, str2, str1, 'REVERSE JACKPOT')
    else:
        print('Hmmm, então algum deles é igual ao outro, interessante...')

    'Pode ser também escrito como abaixo, que já resume um pouco o código:'

    if a == b == c:
        print(str1, str2,  str3, 'JACKPOT')
    elif a != b != c != a:
        print(str3, str2, str1, 'REVERSE JACKPOT')
    else:
        print('Hmmm, então algum deles é igual ao outro, interessante...')

    ''' Nos exemplos acima, o if questiona se a = b = c. Se sim, mostra as três palavras informadas na
    mesma ordem que foram informadas. O elif questiona se 'a' é diferente de 'b' e 'b' é diferente de 'c',
    e 'c' é diferente de 'a'. Se for o caso, mostra as palavras informadas em ordem inversa.
    Por fim, o else vai ser executado quando algum dos números for igual ao outro, mas não todos.

    A identação dos elementos acima é necessária para que o Python interprete da forma correta.

    Podemos também inserir uma condição dentro de outra. Como no exemplo abaixo: '''

    if a == b:
        if b == c:
            print(str1, str2,  str3, 'JACKPOT')
        else:
            print('Hmmm, então algum deles é igual ao outro, interessante...')
    elif a == c:
        if b == c:
            print(str1, str2,  str3, 'JACKPOT')
        else:
            print('Hmmm, então algum deles é igual ao outro, interessante...')
    else:
        if b == c:
            print('Hmmm, então algum deles é igual ao outro, interessante...')
        else:
            print(str3, str2, str1, 'REVERSE JACKPOT')

    '''Há mais diversas outras maneiras de escrever o mesmo código, o uso de operadores
    como 'and' ou 'or' também é um jeito útil de criar este mesmo algorítmo

    O código acima executa a mesma função que o anterior, mas com mais argumentos. Dentro de
    cada if, else e elif é possível incluir qualquer código necessário, sejam prints, loops, castings,
    e por aí vai. É também útil para criar retornos de erro compreensíveis, tanto para nós mesmos quanto
    para o usuário final.

    É possível também resumir os comandos if e else em uma única linha,
    caso estes possuam apenas uma instrução'''

    if a > b: print('A é maior que B')
    # Esta é a sintaxe para usar apenas um único if, sem else.

    print('A é maior que B') if a > b else print('B é maior que A')
    # Esta é a sintaxe para utilizar if + else. Também são possíveis verificações mais complexas:
    
    print('A é maior que B') if a > b else print('A é menor que B') if a < b else print('São iguais')
    # Neste caso, entre o primeiro else e o segundo if, é como se fosse incluso um elif.

    # Podemos também utilizar estas formas para atribuir variáveis, exemplos:
    positivoA = True if a >= 0 else False
    print(f'{a} é positivo.') if positivoA == True else print(f'{a} é negativo.')
    # E para exibir o resultado do teste de verdadeiro ou falso.
    parA = True if (a % 2 == 0) else False
    print(f'{a} é par.') if parA == True else print(f'{a} é ímpar.')
    # Nestes exemplos, determinamos valores lógicos para se o número A é positivo ou não, e par ou não.

    '''Caso você tenha necessidade para um if que não dê retorno algum ou não faça nada,
    é necessário que você utilize 'pass' ao final, para que o código não resulte em erro.'''

    if a == b:
        pass

    '''E isso é tudo sobre sistemas de decisão com If, Else e Elif.'''

    retorno_indice()


def loopwhile():
    """
    Aqui veremos como utilizar o loop While.
    """
    print('\nBem vindo(a) à seção do Loop While\n')

    a, b, c = [float(x) for x in input('Informe três números quaisquer menores que 10 separados por espaço: ').split()]

    '''
    Usamos "while" quando queremos que determinado código seja executado E repetido até que uma condição
    se torne verdadeira. Exemplo: Queremos que o programa faça uma contagem regressiva até chegar a zero.
    
    É possível utilizar diversos tipos de condição, como valores booleanos, numéricos ou relações entre
    dois ou mais valores. Acompanhe os exemplos abaixo:
    '''

    while a < 10:
        print('Contagem para "a" chegar em 10: ', 10 - a)
        a = a + 1       # ou a +=

    '''O código acima realizará uma contagem até que o número "a" 
    seja igual a 10 e exibirá uma contagem'''

    while (a + b + c) > 0:
        print('Contagem para "a + b + c" se reduzirem até 0: ', a + b + c)
        if a > 0:
            a = a - 1       # ou a -=
        if a == 0 and b > 0:
            b = b - 1       # ou b -=
        if a == b == 0 and c > 0:
            c = c - 1       # ou c -=

    '''Já o código acima fará uma contagem regressiva entre a 
    soma de a + b + c até que chegue a zero'''

    '''
    É possível encerrar um loop while antes que ele chegue à sua condição final,
    para isso usamos a função "break". Exemplo abaixo:
    '''
    x = a
    y = b
    cont = int(0)

    while (a + b) > 0:
        if cont == (a + b):
            break
        print(f'Contagem até a + b chegarem em 0: {a + b}')
        if a > 0:
            a -= 1
        if b > 0 and a == 0:
            b -= 1
        cont += 1

    '''Neste exemplo, o while tentará fazer uma contagem regressiva até que (a + b)
    sejam iguais a 0. Mas se a variável cont alcançar o valor de (a + b), o código é
    interrompido e não mais executado.'''

    print('- - - - - - - - - - - - - - - - - - - -')

    '''
    Também é possível interromper o loop atual e começar do zero na próxima rotação, para isso
    usamos a função "continue". Exemplo abaixo:
    '''

    a = x
    b = y
    cont = int(0)

    while (a + b) > 0:
        if cont == (a + b):
            continue
        print(f'Contagem até a + b chegarem em 0: {a + b}')
        if a > 0:
            a -= 1
        if b > 0 and a == 0:
            b -= 1
        cont += 1

    '''Já neste caso, o while novamente tentará fazer uma contagem regressiva até que (a + b)
    sejam iguais a 0, mas ao contrário do exemplo anterior, se a variável cont alcançar o valor
    de (a + b), o código é interrompido e retomado do zero no próximo loop'''

    print('- - - - - - - - - - - - - - - - - - - -')

    '''
    Por fim, podemos também utilizar a função "else" após o "while", para ativar um código assim
    que a condição que fazia o "while" continuar não for mais verdadeira. Reaproveitando o exemplo acima:
    '''

    while (a + b) > 0:
        if cont == (a + b):
            continue
        print(f'Contagem até a + b chegarem em 0: {a + b}')
        if a > 0:
            a -= 1
        if b > 0 and a == 0:
            b -= 1
        cont += 1
    else:
        print('Agora chegamos em 0')

    'E com isso encerramos os exemplos da função while.'

    retorno_indice()


def loopfor():
    """
    Aqui veremos como utilizar o loop For.
    """
    print('\nBem vindo(a) à seção do Loop For\n')

    a, b, c, d, e = [float(x) for x in input('Informe 5 números quaisquer de 0 a 10 separados por espaço: ').split()]
    str1, str2, str3, str4, str5 = input('Informe cinco palavras de no mínimo 4 letras, separadas por espaço: ').split()

    '''
    Enquanto o while é utilizado para iterar um código de acordo com um número arbitrário de vezes,
    o for é utilizado para iterar um código em relação à quantidade de elementos de uma lista.
    
    Neste caso, lista pode se referir à um array, tuple, dictionary, set, ou mesmo uma string (as
    strings são arrays de caracteres, como lembramos). Contanto que seja um conjunto de elementos,
    pode ser utilizado como parâmetro para o 'for'.
    
    Exemplo abaixo:
    '''

    palavras = [str1, str2, str3, str4, str5]
    nums = [a, b, c, d, e]

    for x in palavras:
        print(x)

    print('- - - - - - - - - - - - - - - - - - - -')

    '''
    O exemplo acima adicionou as três palavras fornecidas à lista "palavras" (aproveitamos para
    adicionar os três números informados à lista "nums" também para usarmos depois).
    O "for" neste caso, para cada "x" (variável criada no momento que receberá o valor de cada item
    individual da lista "palavras"), ele deve exibir o valor que "x" carrega.
    
    Da mesma forma, podemos fazer o mesmo com os caracteres das palavras em si, exemplo abaixo:
    '''

    for x in str1:
        print(x)

    print('- - - - - - - - - - - - - - - - - - - -')

    'Neste caso, cada print(x) exibirá uma letra da palavra contida na str1.'

    '''
    Assim como no while, ao executarmos o for podemos também utilizar a função "break", caso
    precisemos que o código seja interrompido em determinado ponto. Veja o exemplo abaixo:
    '''

    for x in nums:
        if x == c:
            break
        print(x)

    print('- - - - - - - - - - - - - - - - - - - -')

    '''O exemplo acima exibirá os elementos da lista até que chegue no "c". Neste ponto, o código 
    será interrompido, antes de exibir o valor de "c".'''

    '''
    Da mesma forma, podemos também utilizar o "continue" para interromper o loop no ponto
    escolhido e recomeçar em seguida.
    '''

    for x in palavras:
        if x == str3:
            continue
        print(x)

    print('- - - - - - - - - - - - - - - - - - - -')

    '''Podemos ver que o break e continue funcionam da mesma forma que funcionam para o while.
    E é sempre bom prestar atenção a ordem onde inserimos ambos, pois isso afeta o que deixará
    de ser executado.'''

    '''
    A função range() pode sr utilizada no lugar de uma lista, e ela aceita até três parâmetros:
    range(6) = contará 6 repetições, começando de 0 e indo até 5
    range(2, 10) = contará repetições de 2 à 9 (o 10 não é contabilizado)
    range(2, 12, 3) = contará de 2 à 12, mas de de 3 em 3 ao invés de 1 em 1
    
    Vamos conferir nos exemplos abaixo:
    '''

    for x in range(6):
        print(x)

    print('- - - - - - - - - - - - - - - - - - - -')

    for x in range(2, 10):
        print(x)

    print('- - - - - - - - - - - - - - - - - - - -')

    for x in range(2, 12, 3):
        print(x)

    print('- - - - - - - - - - - - - - - - - - - -')

    '''
    Da mesma forma que ocorre com "while", também é possível usar a função "else"
    para loops de "for". O funcionamento é o mesmo, permitindo executar um codigo
    assim que as repetiçoes do "for" forem encerradas:
    '''

    for x in range(10):
        print(x)
    else:
        print('Você não viu, mas chegamos à 10.')

    print('- - - - - - - - - - - - - - - - - - - -')
    
    '''Lembrando de que o "else" não será executado caso o código seja
    antes interrompido com um "break".'''
    
    '''
    É possível também executar um loop de "for" dentro de outro loop de "for".
    Neste caso, a cada vez que o loop "externo" for executado, o loop interno
    será executado por completo a cada iteração. Confira a seguir:
    '''
    
    for x in nums:
        for y in palavras:
            print(x, y)
        else:
            print('fim do loop "interno"')
    else:
        print('fim do loop "externo"')

    print('- - - - - - - - - - - - - - - - - - - -')
    
    '''
    Por fim, da mesma forma que usamos no "if", caso precisemos utlizar um loop
    for que não dê nenhum retorno, devemos usar a função "pass". Exemplo:
    '''
    
    for x in range(11):
        pass

    'E com isso encerramos o conteúdo sobre Loops de For.'

    retorno_indice()


def lists():
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

    listaex01 = ['cuscuz','cafézinho', 'frutas', 'empada', 'suco', a, b, c, d, e]
    # Os 5 primeiros itens são strings, os 5 finais são os números informados
    print(listaex01[0])      # Exibirá (cuscuz)
    print('---------------------------------------\n')
    print(listaex01[-4])     # Exibirá o segundo número que você informou
    print('---------------------------------------\n')
    print(listaex01[3:6])    # Exibirá 'empada', 'suco', e os dois primeiros números informados
    print('---------------------------------------\n')
    print(listaex01[-1])     # Exibirá o último número informado
    print('---------------------------------------\n')
    print(listaex01[-7:-2])  # Exibirá 'empada', 'suco', e os três primeiros números indormados
    print('---------------------------------------\n')
    print(4 * listaex01[8])  # Exibirá o resultado de 4 * o quarto número informado
    print('---------------------------------------\n')
    print(listaex01[2])      # Exibirá 'frutas'
    listaex01[2] = 'abacaxi' # Mudará 'frutas' para 'abacaxi'
    print(listaex01[2])      # Exibirá 'abacaxi' como novo item do índice [2]
    print('---------------------------------------\n')

    '''
    Abaixo veremos como conferir se determinado item existe na lista:
    '''
    print('Temos abacaxi aqui?')
    if 'abacaxi' in listaex01:
        print('Tem sim! Hora de fazer um suquinho de abacaxi~')
    else:
        print('Eita, tem não... Vou ter de me contentar com ki-suco... :´(')
    print('---------------------------------------\n')

    'MODIFICANDO ITENS DA LISTA'
    '''
    Para modificar um item da lista, referencie-o pelo seu índice.
    Vimos um exemplo acima, confira mais um logo abaixo:
    '''

    listaex02 = ['pera', 'uva', 'maçã', 'salada mista', str1, str2, str3, str4, str5]
    print(f'Lista exemplo: {listaex02}')
    print('---------------------------------------\n')

    listaex02[3] = 'melancia'
    print(f'Quarto item modificado: {listaex02}')
    print('---------------------------------------\n')
    ''' O quarto item (salada mista) agora é 'melancia'

    Podemos também modificar mais de um item da lista ao mesmo tempo: '''
    
    listaex02[0:4] = ['dois hamburgueres', 'alface', 'queijo', 'molho especial']
    print(f'Receita MC: {listaex02}')
    print('---------------------------------------\n')
    ''' Modificamos os itens de 1 à 4 para os itens acima.
    Mas estão faltando alguns, poderíamos tê-los inserido como abaixo: '''

    listaex02[0:4] = ['dois hamburgueres', 'alface', 'queijo', 'molho especial', 'cebola', 'picles', 'pão com gergelim']
    print(f'Receita MC completa: {listaex02}')
    print('--------------------------------------\n')
    ''' Os itens extras são inseridos após o último item indexado, e antes dos restantes.
    O resultado final terá a receita completa + as 5 strings informadas.

    Mas e se eu odiar MC e quiser outra coisa no lugar? '''

    listaex02[0:7] = ['cuscuz', 'charque', 'vinagrete']
    print(f'Refeição de respeito: {listaex02}')
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


    retorno_indice()


def sets():
    """
    Aqui veremos como utilizar Sets.
    """
    print('\nBem vindo(a) à seção de Sets\n')

    retorno_indice()


def tuples():
    """
    Aqui veremos como utilizar Tuples.
    """
    print('\nBem vindo(a) à seção de Tuples\n')

    retorno_indice()


def dictionary():
    """
    Aqui veremos como utilizar Dicionários.
    """
    print('\nBem vindo(a) à seção de Dicionários\n')

    retorno_indice()


def inputs():
    """
    Aqui veremos como adquirir inputs do usuário.
    """
    print('\nBem vindo(a) à seção de Inputs do Usuário\n')

    retorno_indice()


def functions():
    """
    Aqui veremos como utilizar funções.
    """
    print('\nBem vindo(a) à seção de Funções\n')

    retorno_indice()


def objects():
    """
    Aqui veremos como funcionam Objetos.
    """
    print('\nBem vindo(a) à seção de Objetos\n')

    retorno_indice()


def classes():
    """
    Aqui veremos como funcionam as Classes.
    """
    print('\nBem vindo(a) à seção de Classes\n')

    retorno_indice()


def datetime():
    """
    Aqui veremos as possíveis operações com datas e horas.
    """
    print('\nBem vindo(a) à seção de Operações com Data e Hora\n')

    retorno_indice()


def extras():
    """
    Aqui veremos coisas extras sobre seções anteriores que são menos comuns no aprendizado inicial.
    """
    print('\nBem vindo(a) à seção de Informações Extras\n')

    retorno_indice()


def indice():
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
    +'~~  Funções Básicas  ~~~~~~~~~~~~~~~~~~~~~~~~\n'
    +'[12]\t\tInputs do Usuário\n'
    +'[13]\t\tFunções\n'
    +'[14]\t\tObjetos\n'
    +'[15]\t\tClasses\n'
    +'~~  Outros  ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~\n'
    +'[16]\t\tData e hora\n'
    +'[18]\t\tInformações Extra')

    index = str(input('\nPara qual exemplo deseja ir? Digite um número inteiro de 1 à 18:\n>> '))

    if index == '1':
        math()
    elif index == '2':
        string()
    elif index == '3':
        boolean()
    elif index == '4':
        types()
    elif index == '5':
        ifelse()
    elif index == '6':
        loopwhile()
    elif index == '7':
        loopfor()
    elif index == '8':
        lists()
    elif index == '9':
        sets()
    elif index == '10':
        tuples()
    elif index == '11':
        dictionary()
    elif index == '12':
        inputs()
    elif index == '13':
        functions()
    elif index == '14':
        objects()
    elif index == '15':
        classes()
    elif index == '16':
        datetime()
    elif index == '18':
        extras()
    else:
        exit('Okay, saindo do exemplo. Até mais~')


def retorno_indice():
    """
    Função para retornar ao índice.
    """
    back = str(input('\nVoltar para o indice? s/n >> '))

    if back == 's':
        indice()
    else:
        exit('Okay, saindo do exemplo. Até mais~')


if __name__ == '__main__':
    """
    Esta é a chamada para a função principal, caso este arquivo seja rodado como principal
    e não chamado como módulo de outro arquivo .py

    Para importar um outro arquivo .py você pode usar import arquivo
    Para importar uma função de outro arquivo .py você pode usar import arquivo.funcao
    """
    main()
