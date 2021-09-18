import modulo_retorno

def boolean( package = {
    'inteiros': [3, 5, 8, 13, 21], 
    'reais': [1.5, 2.4, 5.3, 7.2, 10.5], 
    'palavras': ["bike", "kitten", "banana", "plant", "laptop"], 
    'frase': "I threw my tablet at a banana tree and a kitten fell on my bike" } ):
    """
    Nesta seção, veremos como funcionam operadores booleanos.
    """
    print('\nBem vindo(a) à seção de Operações Booleanas\n')
    '''
    Operações booleanas nos permitem avaliar se uma condição é verdadeira ou falsa.
    Há diversos modos de conferir isso, e utilizamos muito dentro de condicionais if/else
    Abaixo, vamos conferir o principal para utilizarmos estes comparativos, mas antes,
    vamos importar as variáveis declaradas no começo para usarmos:
    '''
    a, b, c, d, e = [int(x) for x in package['inteiros']]
    v, w, x, y, z = [float(x) for x in package['reais']]
    str1, str2, str3, str4, str5 = [str(x) for x in package['palavras']]
    frase = package['frase']

    '''
    Para conferir se uma expressão é igual, maior ou menor que outra,
    basta realizar uma comparação direta usando os operadores abaixo:

    == significa "igual à"              != significa "diferente de"
    > significa "maior que"             < significa "menor que"
    >= significa "maior ou igual        <= significa "menor ou igual"

    Estas operações retornam sempre um valor "Verdadeiro(True)" ou "Falso(False)".
    True e False são sempre capitalizados, e resultados ambíguos não são permitidos.
    Vamos agora fazer algumas comparações, começando abaixo:
    '''

    print(f'{str1} é igual a {str1}? {str1} == {str1} = {str1 == str1}\n'
    +f'{str2} é igual a {str3}? {str2} == {str3} = {str2 == str3}\n'
    # Testando igualdades. O primeiro será True, o segundo False
    +f'{str4} é diferente de {str4}? {str4} != {str4} = {str4 != str4}\n'
    +f'{str4} é diferente de {str5}? {str4} != {str5} = {str4 != str5}\n')
    # Testando diferenças. O primeiro retornará False, o segundo True

    # O mesmo pode ser feito para números. Vamos conferir abaixo:

    print(f'{a} é igual a {a}? {a} == {a} = {a == a}\n'
    +f'{b} é igual a {c}? {b} == {c} = {b == c}\n'
    # O retorno da primeira será True, o da segunda será False
    +f'{d} + {e} é igual a {e} + {d}? {d} + {e} == {e} + {d} = {d + e == e + d}\n'
    # Note acima que podemos utilizar resultados de expressões como parâmetros de comparação
    +f'{a} é diferente de {a}? {a} != {a} = {a != a}\n'
    +f'{b} é diferente de {c}? {b} != {c} = {b != c}\n'
    # O retorno da primeira será False, o da segunda será True
    +f'{a} é maior que {d}? {a} > {d} = {a > d}\n'
    +f'{a} é menor que {d}? {a} < {d} = {a < d}\n'
    # O retorno depende dos números informados.
    +f'{a} * {c} * {e} é maior que {b} * {d}? ({a} * {c} * {e}) > ({b} * {d}) = {(a * c * e) > (b * d)}\n'
    +f'{a} * {c} * {e} é menor que {b} * {d}? ({a} * {c} * {e}) < ({b} * {d}) = {(a * c * e) < (b * d)}\n')
    # O resultado das expressões acima depende dos valores informados

    '''
    Além destes operadores, temos também outras ferramentas para nos ajudar
    na criação de condições:

    and = "e" | Uso: a > b and b > c             or = "ou" | Uso: a > b or b > c
    ^ Faz com que a exigência para              ^ Faz com que o valor retornado
    uma condição retornar "True" seja           seja "True" se qualquer uma das
    que todas as condições sejam                condições for verdadeira.
    verdadeiras.                                

    in = "em" | Uso: a in b                     not = "não" | Uso: not a == a        
    ^ A exigência para retornar "True"          ^ Inverte a exigência. No exemplo
    neste caso é de que "a" esteja              acima, "a" é igual a si próprio,
    contigo em "b". b pode ser uma              mas com o uso do "not" o valor
    string ou outra estrutura de dados.         retornado será "False"

    Vamos conferir alguns exemplos abaixo:
    '''
    print(f'{str1} existe dentro de {frase}?\n'
    +f'>> {str1} in {frase} = {str1 in frase}\n'
    # Confere se a primeira palavra existe dentro da frase informada

    +f'Dentre as palavras {str1}, {str2}, {str3}, {str4} e {str5}, alguma existe dentro de {frase}?\n'
    +f'>> ({str1} in frase or {str2} in frase or {str3} in frase or {str4} in frase or {str5} in {frase} =\n'
    +f'>> {str1 in frase or str2 in frase or str3 in frase or str4 in frase or str5 in frase}\n'
    # Confere se alguma das palavras existe dentro da frase informada usando "or"

    +f'Todas as palavras {str1}, {str2}, {str3}, {str4} e {str5} existem dentro de {frase}?\n'
    +f'>> ({str1} and {str2} and {str3} and {str4} and {str5}) in {frase} =\n'
    +f'>> {(str1 and str2 and str3 and str4 and str5) in frase}\n'
    # Confere se todas as palavras existem dentro da frase informada usando "and"

    +f'Todas as palavras {str1}, {str2}, {str3}, {str4} e {str5} não existem dentro de {frase}?\n'
    +f'>> ({str1} and {str2} and {str3} and {str4} and {str5}) not in {frase} =\n'
    +f'>> {(str1 and str2 and str3 and str4 and str5) not in frase}')
    # Confere se todas as palavras NÃO existem dentro da frase informada usando "and" e "not"

    '''
    Por fim, alguns métodos disponíveis que podem ser usados com valores booleanos:
    Usar print() para exibir no terminal o valor é um uso comum.
    A função "bool()" lhe permite verificar o valor booleano de qualquer variável. Sintaxe abaixo:
    print(bool(15))
    print(bool('olá''))
    print(bool(str1))

    Os valores de diversas coisas são considerados "True" por padrão, por exemplo:
    1. Strings são consideradas "True", mas se forem vazias são "False"
    2. Qualquer número é considerado "True", exceto o número zero, que é "False"
    3. Listas, tuples, sets e dicionários são "True" a menos que estejam vazios.
    '''

    print('E isso é tudo sobre operações booleanas.')

    modulo_retorno.retorno(package)


if __name__ == '__main__':
    boolean()
    