def par_ou_impar(numero):
    """ Deve retorna PAR ou IMPAR apenas """
    # Seu código aqui
    if numero % 2 == 0:
        return 'PAR'
    return 'IMPAR'


def separa_frase(frase):
    """
    Deve separar uma frase de acordo com os espaços e retornar em formato de lista.
    Exemplo: 'Faculdade Impacta') retorna ['Faculdade', 'Impacta']
    """
    # Seu código aqui
    return frase.split()


def palindrome(palavra):
    """
    Palíndrome é quando uma plavra escrita de trás pra frente é igual.
    Exemplo: ovo, arara
    A mensagem retornada deverá ser:
    'Palíndrome'
    OU
    'Não é palíndrome'
    """
    # Seu código aqui
    if palavra == palavra[::-1]:
        return 'Palíndrome'
    return 'Não é palíndrome'

def tamanho_lista(lista):
    """
    Deve retornar o tamanho da lista
    Exemplo: [1, 2, 3, 4, 5] retorna 5
    """
    return len(lista)


def max_lista(lista):
    """
    Deve retornar o o maior número da lista
    Exemplo: [11, 32, 53, 44, 5] retorna 53
    """
    return max(lista)


def min_lista(lista):
    """
    Deve retornar o menor número da lista
    Exemplo: [11, 32, 53, 44, 5]) retorna 5
    """
    return min(lista)
