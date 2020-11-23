def numero_ou_string(parametro):
    """
    Crie uma função que receba um parâmetro e retorne a mensagem:
    '<parametro> é número' ou '<parametro> é string'
    """
    return f'{parametro} é número' if isinstance(parametro, int) else f'{parametro} é string'


def tamanho_frase(frase):
    """ Deve retornar a quantidade de caracteres da frase ne mensagem 'A frase tem <número> caracteres.' """
    return f'A frase tem {len(frase)} caracteres.'


def situacao_aluno(nota):
    """
    Deve retornar a situação do aluno conforme a nota de acordo com a mensagem abaixo:
    Nota 7 ou maior retorna 'Aluno aprovado.'
    Nota 5.1 até 6.9 retorna 'Aluno de recuperação.'
    Nota 5 ou menor retorna 'Aluno reprovado.'
    """
    if nota >= 7:
        return 'Aluno aprovado.'
    elif nota < 5:
        return 'Aluno reprovado.'
    else:
        return 'Aluno de recuperação.'
