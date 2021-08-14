import retornoIndice

def ifelse(integers, reals, words, sentence):
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

    retornoIndice.retorno(integers, reals, words, sentence)