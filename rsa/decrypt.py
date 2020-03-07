# coding: utf-8
from rsa.util import transform_number_to_string


# TODO: Adicionar doc strings


def decrypt_number(message, n, d):
    return pow(message, d, n)


def decrypt_string(number: int, n, d):
    result = pow(number, d, n)
    return transform_number_to_string(result)
