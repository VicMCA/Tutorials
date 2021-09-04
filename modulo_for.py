import modulo_retorno

def loopfor(
    integers=[3, 5, 8, 13, 21], 
    reals=[1.5, 2.4, 5.3, 7.2, 10.5], 
    words=["bike", "kitten", "banana", "plant", "laptop"], 
    sentence="I threw my tablet at a banana tree and a kitten fell on my bike"):
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

    modulo_retorno.retorno(integers, reals, words, sentence)


if __name__ == '__main__':
    loopfor()
