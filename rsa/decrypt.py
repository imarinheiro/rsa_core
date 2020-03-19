# coding: utf-8
from rsa.util import transform_number_to_string


def decrypt_number(number, n, d):
    """
    Descriptografa o número informado com base nos parâmetros number e a chave privada (n, d).

    :param number: número inteiro que representa o texto criptografado
    :param n: parte da chave privada, ou, produto de 'p *q' que respectivamente representam os números primos iniciais
    :param d: parte da chave privada, ou, resultado equivalente ao módulo inverso baseado em 'e' e 'tocient'
    :return: número descriptografado
    """
    return pow(number, d, n)


def decrypt_string(number: int, n, d):
    """
    Descriptografa o texto com base nos parâmetros number e a chave privada (n, d).

    :param number: número inteiro que representa o texto criptografado
    :param n: parte da chave privada, ou, produto de 'p *q' que respectivamente representam os números primos iniciais
    :param d: parte da chave privada, ou, resultado equivalente ao módulo inverso baseado em 'e' e 'tocient'
    :return: texto descriptografado
    """
    result = pow(number, d, n)
    return transform_number_to_string(result)
