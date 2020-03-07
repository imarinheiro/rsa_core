# coding: utf-8


# TODO: Adicionar doc strings

def encrypt_number(message: int, n, e):
    return pow(message, e, n)

