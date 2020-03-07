# coding: utf-8
from rsa.util import transform_string_to_number


# TODO: Adicionar doc strings


def encrypt_number(message: int, n, e):
    return pow(message, e, n)


def encrypt_string(message: str, n, e):
    number = transform_string_to_number(message)
    return pow(number, e, n)
