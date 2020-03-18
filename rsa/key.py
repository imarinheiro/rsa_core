# coding: utf-8
from sympy import mod_inverse

from rsa.util import is_relatively_prime


def calculate_n(p, q):
    """
    Calcula 'n' de acorco com os números primos informados, através da fórmula 'p * q'

    :param p: número primo qualquer
    :param q: número primo qualquer
    :return: produto dos dois números primos informados
    """
    return p * q


def calculate_tocient(p, q):
    """
    Calcula tocient ou phi (alfabeto grego) de acordo com o parâmetro infomado e a fórmula '(p - 1) * (q - 1)'

    :param p: número primo qualquer
    :param q: número primo qualquer
    :return: retorna o valor de tocient ou phi
    """
    return (p - 1) * (q - 1)


def select_e(tocient):
    """
    Seleciona o primeiro número relativamente primo ao tociente informado, e que seja maior que 3 e menor que o tocient.
    Esta seleção é utilizada para criar parte da chave privada e da chave pública.
    Para calcular o tociente utilizar a função:
    :func:`calculate_tocient <rsa.key.calculate_tocient>`

    :param tocient: calculado através da função :func:`calculate_tocient <rsa.key.calculate_tocient>`
    :return: retorna o número primo com base no parâmetro
    """
    for e in range(3, tocient, 2):
        if is_relatively_prime(e, tocient):
            return e


def calculate_d(e, tocient):
    """
    Retorna o número c tal que, (e * c) = 1 (mod tocient)
    Desde que c tenha o mesmo sinal de m. Se nenhum valor existir a exceção ValueError é lançado.
    Esse cálculo é utilizadp para criar parte da chave privada.
    O 'calculate_d' usa a função da biblioteca matemática sympy :func:`mod_inverse <sympy.mod_inverse>` com os parâmetros
    'e' e 'tocient'.

    :param e: selecionado através da função :func:`select_e <rsa.key.select_e>`
    :param tocient: calculado através da função :func:`calculate_tocient <rsa.key.calculate_tocient>`
    :return: retorna o cálculo de 'd'
    """
    return mod_inverse(e, tocient)
