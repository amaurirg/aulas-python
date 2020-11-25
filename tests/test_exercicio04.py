from exercicios.exercicio04 import *


def test_lista_num_str():
	assert lista_num_str(['1', 4, 'F', 56, 92, 'T', 'H', 'Teste', 87]) == [['1', 'F', 'T', 'H', 'Teste'], [4, 56, 92, 87]]
	assert lista_num_str(['asdf', '100', 100, 234, 'qwert', 'ok', 789]) == [['asdf', '100','qwert', 'ok'], [100, 234, 789]]


def test_lista_join():
	assert lista_join(['Hoje', 'o', 'dia', 'está', 'nublado']) == 'Hoje o dia está nublado'
	assert lista_join(['Transforma', 'a', 'lista', 'recebida', 'em', 'uma', 'frase']) == 'Transforma a lista recebida em uma frase'


def test_troca_string_por_indice():
	assert troca_string_por_indice(['a', 'B', 'indice', 'd', 'E']) == ['a', 'B', 2, 'd', 'E']	
	assert troca_string_por_indice(['a', 'B', 'c', 'D', 'indice', 'f', 'G']) == ['a', 'B', 'c', 'D', 4, 'f', 'G']
