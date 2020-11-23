def maior_menor(numero1, numero2):
    """ Deve retornar qual número é maior ou se são iguais em forma da mensagem 'O número <maior_numero> é maior' """
    # Seu código aqui
    return f'O número {numero1} é maior' if numero1 > numero2 else f'O número {numero2} é maior'


def tras_para_frente(palavra):
    """Crie uma função que receba uma palavra e a retorne de trás para frente"""
    # Seu código aqui
    return palavra[::-1]


def nome_idade(nome, idade):
    """ Deve solicitar nome e idade ao usuário e retornar a mensagem: <Nome> tem <idade> anos."""
    # Seu código aqui
    return f'{nome} tem {idade} anos.'
