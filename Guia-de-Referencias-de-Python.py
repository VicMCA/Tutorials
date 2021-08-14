#!/usr/bin/env python3

import indice, retornoIndice

def main():
    """
    Acima é o começo da função principal.
    E esta é a mini-documentação para ela, acessível chamando print(main.__doc__)
    O mesmo vale pra outras funções também. Aspas duplas são a forma recomendada.
    """

    print('\nBem-vindo(a) ao guia rápido de "Como Fazer X" em Python.\n\n'
    +'Este é um guia com exemplos para servir de referência sobre como fazer diversas\n'
    +'coisas, e as explicações se encontram nos comentários deste código.\n\n'
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

    # a, b, c, d, e = [int(x) for x in input('Digite cinco números inteiros separados por espaço:\n>> ').split()]
    # inteiros = (a, b, c, d, e)
    # v, w, x, y, z = [float(x) for x in input('Digite cinco números reais separados por espaço:\n>> ').split()]
    # reais = (v, w, x, y, z)
    # w1, w2,  w3, w4, w5 = input('Digite cinco palavras com mais de 4 letras, separados por espaço:\n>> ').split()
    # palavras = (w1, w2, w3, w4, w5)
    # frase = input('Digite uma frase que contenha pelo menos uma das palavras informadas acima:\n>> ')

    'Placeholder values'
    inteiros = (10, 20, 30, 40, 50)
    reais = (1.5, 2.4, 3.6, 4.2, 5.1)
    palavras = ('pêra', 'duas uvas', 'maçã', 'salada mista', 'roma')
    frase = 'o rato roeu a roupa do rei de roma'

    start = str(input('Muito bem! Vamos agora conferir o índice? s/n >> '))

    if start == 'n':
        exit('Okay, saindo do exemplo. Até mais~')

    indice.indice(inteiros, reais, palavras, frase)


if __name__ == '__main__':
    """
    Esta é a chamada para a função principal, caso este arquivo seja rodado como principal
    e não chamado como módulo de outro arquivo .py

    Para importar um outro arquivo .py você pode usar import arquivo
    Para importar uma função de outro arquivo .py você pode usar import arquivo.funcao
    """
    main()
