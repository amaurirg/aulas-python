from resolvidos.exercicios.exercicio01 import *


def test_maior_menor():
    assert maior_menor(3, 4) == 'O número 4 é maior'
    assert maior_menor(25, 18) == 'O número 25 é maior'


def test_tras_para_frente():
    assert tras_para_frente('faculdade') == 'edadlucaf'
    assert tras_para_frente('impacta') == 'atcapmi'


def test_nome_idade():
    assert nome_idade('Pedro', 27) == 'Pedro tem 27 anos.'
