# coding: utf-8


# TODO: Adicionar doc strings

def encrypt(message, n, e):
    return pow(message, e, n)
