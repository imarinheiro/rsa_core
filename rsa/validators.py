# coding: utf-8
from sympy import isprime

from rsa.util import transform_string_to_number

PRIME_EXCEPTION = 'It must be prime number'
LENGTH_KEY_EXCEPTION = 'The key must be greater than message'
MESSAGE_EXCEPTION = 'The message must contains only one character'


def is_prime(number):
    """
    Verifica se é um número primo e uma exception é lançada caso 'number' ele não seja primo.

    :param number: número a ser verificado se é primo
    :return: None
    """
    if not isprime(number):
        raise Exception(PRIME_EXCEPTION)


def key_length(message, p, q):
    """
    Verifica se a partir do tamanho da mensagem se o tamanho dos números primos iniciais (p, q)
    para gerar o par de chaves publica e privada é suficientemente grande para criptografar a mensagem.
    Caso o par de  números primos não seja suficientemente grandes uma exception é lançada.

    :param message: inteiro ou string
    :param p: número primo inicial
    :param q: número primo inicial
    :return: None
    """
    result = None
    if type(message) is int:
        result = message
    if type(message) is str:
        result = transform_string_to_number(message)
    if result >= p * q:
        raise Exception(LENGTH_KEY_EXCEPTION)


def message_length(message):
    """
    Verifica se uma string contem apenas um caractere. Caso não seja uma exception é lançada.

    :param message: string ou número
    :return: None
    """
    if type(message) is str and len(message) > 1:
        raise Exception(MESSAGE_EXCEPTION)
