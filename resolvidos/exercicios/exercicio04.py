def lista_num_str(lista):
	""" 
	Deve retornar uma lista com duas listas dentro, 
	uma para strings e outra para inteiros 
	Exemplo: [['1', 'F', 'T', 'H', 'Teste'], [4, 56, 92, 87]]	
	"""
	# Seu código aqui
	lista_int = []
	lista_str = []
	for item in lista:	
		if isinstance(item, int):
			lista_int.append(item)
		else:
			lista_str.append(item)
	return [lista_str, lista_int]


def lista_join(lista):
	""" 
	Deve juntar os itens da lista, separados por espaço para formar a frase 
	Exemplo: ['Eu', 'gosto', 'dessa', 'música'] retorna 'Eu gosto dessa música'
	"""
	# Seu código aqui
	return ' '.join(lista)


def troca_string_por_indice(lista):
	""" 
	Deve substituir o item 'indice' pelo número do índice correspondente na lista 
	Exemplo: ['um', 'outro', 'indice', 'palavra', 'qualquer'] retorna	['um', 'outro', 2, 'palavra', 'qualquer']
	"""
	# Seu código aqui
	lista.insert(lista.index('indice'), lista.index('indice'))
	lista.remove('indice')
	return lista
	