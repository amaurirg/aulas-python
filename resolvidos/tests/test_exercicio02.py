from resolvidos.exercicios.exercicio02 import *


def test_numero_ou_string():
    assert numero_ou_string(28) == '28 é número'
    assert numero_ou_string('Python') == 'Python é string'


def test_tamanho_frase():
    assert tamanho_frase('Eu estudo na Faculdade Impacta') == 'A frase tem 30 caracteres.'
    assert tamanho_frase('Hoje está fazendo sol') == 'A frase tem 21 caracteres.'


def test_situacao_aluno():
    assert situacao_aluno(9) == 'Aluno aprovado.'
    assert situacao_aluno(4.5) == 'Aluno reprovado.'
    assert situacao_aluno(6.2) == 'Aluno de recuperação.'
