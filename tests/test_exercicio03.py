from exercicios.exercicio03 import *


def test_par_ou_impar():
    assert par_ou_impar(12) == 'PAR'
    assert par_ou_impar(15) == 'IMPAR'


def test_separa_string():
    assert separa_frase('Faculdade Impacta') == ['Faculdade', 'Impacta']
    assert separa_frase('Aulas de Python') == ['Aulas', 'de', 'Python']


def test_palindrome():
    assert palindrome('ovo') == 'Palíndrome'
    assert palindrome('arara') == 'Palíndrome'
    assert palindrome('faculdade') == 'Não é palíndrome'
    assert palindrome('impacta') == 'Não é palíndrome'


def test_tamanho_lista():
    assert tamanho_lista([1, 2, 3, 4, 5]) == 5
    assert tamanho_lista(['um', 'dois', 'três', 'quatro', 'cinco', 'seis', 'sete', 'oito']) == 8


def test_max_lista():
    assert max_lista([11, 32, 53, 44, 5]) == 53
    assert max_lista([5, 76, 32, 60, 14]) == 76


def test_min_lista():
    assert min_lista([11, 32, 53, 44, 5]) == 5
    assert max_lista([15, 76, 32, 6, 143]) == 6
