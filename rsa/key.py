# coding: utf-8
from sympy import mod_inverse

from rsa.util import is_relatively_prime


# TODO: Adicionar doc strings

def calculate_n(p, q):
    return p * q


def calculate_tocient(p, q):
    return (p - 1) * (q - 1)


def select_e(tocient):
    # TODO: Alterar para retornar erro quando não encontrar um e
    for e in range(3, tocient, 2):
        if is_relatively_prime(e, tocient):
            return e


def calculate_d(e, tocient):
    return mod_inverse(e, tocient)
