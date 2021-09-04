import modulo_retorno

def loop_while(
    integers=[3, 5, 8, 13, 21], 
    reals=[1.5, 2.4, 5.3, 7.2, 10.5], 
    words=["bike", "kitten", "banana", "plant", "laptop"], 
    sentence="I threw my tablet at a banana tree and a kitten fell on my bike"):
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

    modulo_retorno.retorno(integers, reals, words, sentence)


if __name__ == '__main__':
    loop_while()
