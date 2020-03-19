# coding: utf-8
from rsa.util import transform_string_to_number


def encrypt_number(number: int, n, e):
    """
    Criptografa o número informado com base nos parâmetros number e a chave pública (n, e).

    :param number: número inteiro que representa o número a ser criptografado
    :param n: parte da chave pública, ou, produto de 'p *q' que respectivamente representam os números primos iniciais
    :param e: parte da chave pública, ou, resultado da seleção de um número relativamente primo ao tociente
    :return: número criptografado
    """
    return pow(number, e, n)


def encrypt_string(message: str, n, e):
    """
    Criptografa o texto com base nos parâmetros message e a chave pública (n, e).

    :param message: string que representa o texto a ser criptografado
    :param n: parte da chave pública, ou, produto de 'p *q' que respectivamente representam os números primos iniciais
    :param e: parte da chave pública, ou, resultado da seleção de um número relativamente primo ao tociente
    :return: texto criptografado
    """
    number = transform_string_to_number(message)
    return pow(number, e, n)
