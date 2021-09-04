import modulo_retorno

def math(
    integers=[3, 5, 8, 13, 21], 
    reals=[1.5, 2.4, 5.3, 7.2, 10.5], 
    words=["bike", "kitten", "banana", "plant", "laptop"], 
    sentence="I threw my tablet at a banana tree and a kitten fell on my bike"):
    """
    Esta função serve para exemplo de diversas operações matemáticas possíveis e suas sintaxes.
    """

    print('\nBem vindo(a) à seção de Operações Matemáticas\n')

    a, b, c, d, e = [int(x) for x in integers]
    v, w, x, y, z = [float(x) for x in reals]

    # Acima estamos criando variáveis a partir de elementos em uma lista. Vemos isso em outro módulo.

    print(f'Os números informados foram:\n'
    +f'a = {a}\tb = {b}\tc = {c}\td = {d}\te = {e}\n'
    +f'v = {v}\tw = {w}\tx = {x}\ty = {y}\tz = {z}\n'
    +'E abaixo faremos algumas operações básicas com eles.\n')

    # Para adição, apenas somamos os números no formato de n1 + n2, como no exemplo abaixo:
    print(f'Adição: {a} + {b} = {a + b} | {c} + {d} + {e} = {c + d + e}\n'
    +f'Adição: {v} + {w} = {v + w} | {x} + {y} + {z} = {x + y + z}\n')
    
    # Para subtração é igualmente simples, n1 - n2, como abaixo:
    print(f'Subtração: {e} - {d} = {e - d} | {c} - {b} - {a} = {c - b - a}\n'
    +f'Subtração: {z} - {y} = {z - y} | {x} - {w} - {v} = {x - w - v}\n')

    # Para multiplicação, n1 * n2:
    print(f'Multiplicação: {e} * {a} = {e * a} | {x} * {b} * {y} = {x * b * y}\n'
    +f'Multiplicação: {v} * {z} = {v * z} | {c} * {w} * {d} = {c * w * d}\n')
    
    # Para divisão, n1 / n2:
    print(f'Divisão: {d} / {b} = {d / b} | {e} / {c} / {a} = {e / c / a}'
    +f'Divisão: {y} / {w} = {y / w} | {z} / {x} / {v} = {z / x / v}\n')
    
    # Alternativamente, n1 // n2 para termos resultado arredondado:
    print(f'Divisão com resultado arredondado: {d} // {b} = {d // b} | {e} // {c} // {a} = {e // c // a}\n'
    +f'Divisão com resultado arredondado: {y} // {w} = {y // w} | {z} // {x} // {v} = {z // x // v}\n')
    
    # Para módulo, n1 % n2:
    print(f'Módulo: {a} % 2 = {a % 2}\n'
    +f'Módulo: {b} % {c} = {b % c}\n')

    "Abaixo veremos exponenciação, radicação, percentagem e arredondamento."

    # Para exponenciação, podemos usar n1 ** n2:
    print(f'Exponenciação: {b} ** {c} = {b ** c}\n'
    +f'Exponenciação: {w} ** {x} = {w ** x}\n')
    
    # Alternativamente usamos a função pow(n1, n2), como abaixo:
    print(f'Exponenciação: pow({d}, {e}) = {pow(d, e)}\n'
    +f'Exponenciação: pow({y}, {z}) = {pow(y, z)}\n')
    
    # Usando pow(x, y) podemos calcular o módulo (restante de uma divisão) usando pow(x, y, z)
    # Neste caso, será o módulo de x^y quando dividido por z.

    # Para radicação, usamos n1 ** 1/n2:
    print(f'Radicação: {d} ** 1/{a} = {d ** 1/a}\n'
    +f'Radicação: {b} ** 1/{e} = {b ** 1/e}\n')

    # Basicamente, elevamos um número à 1/outro número. Bastante versátil.

    # Existe uma função para raiz quadrada usando a biblioteca math, importando com 'import math'
    # Para chamar essa função se usa math.sqrt(x,y)

    # Para percentual, usamos regra de 3, na fórmula "(percentagem / 100) * total"
    print(f'Percentual "{a} por cento de {d}: ({a} / 100) * {d} = {(a / 100) * d}\n'
    +f'Percentual "{z} por cento de {c}: ({z} / 100) * {c} = {(z / 100) * c}\n')

    # Para arredondamento, usamos a função round(n1, n2), onde n1 é o número, 
    # e n2 a quantidade de casas decimais.
    print(f'Arredondamento com round: round({w} * {x} + {y} / {z}, 2) = {round(w * x + y / z, 2)}\n'
    # Podemos também utilizar o formato var:.nf, onde n é o número de casas  decimais.
    +f'Arredondamento com ":.2f": ({w} * {x} + {y} / {z}):.2f = {(w * x + y / z):.2f}\n'
    +f'Sem arredondamento: ({w} * {x} + {y} / {z}, 2) = {w * x + y / z}\n')

    print('E isso é tudo sobre operações aritméticas.')

    modulo_retorno.retorno(integers, reals, words, sentence)


if __name__ == '__main__':
    math()
