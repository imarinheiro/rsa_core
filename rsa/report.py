# coding: utf-8
from rsa.decrypt import decrypt
from rsa.encrypt import encrypt
from rsa.key import calcular_n, selecionar_e, calcular_tocient, calcular_d


# TODO: Adicionar doc strings


def set_context_encrypt(message, p, q):
    context = {}
    context['plain_text'] = message
    context['p'] = p
    context['q'] = q
    context['n'] = calcular_n(p, q)
    context['tocient'] = calcular_tocient(p, q)
    context['e'] = selecionar_e(context['tocient'])
    context['d'] = calcular_d(context['e'], context['tocient'])
    context['public_key'] = (context['n'], context['e'])
    context['encrypted_text'] = encrypt(context['plain_text'], context['n'], context['e'])
    return context


def set_context_decrypt(message, p, q):
    context = {}
    context['plain_text'] = message
    context['p'] = p
    context['q'] = q
    context['n'] = calcular_n(p, q)
    context['tocient'] = calcular_tocient(p, q)
    context['e'] = selecionar_e(context['tocient'])
    context['d'] = calcular_d(context['e'], context['tocient'])
    context['public_key'] = (context['n'], context['e'])
    context['encrypted_text'] = encrypt(context['plain_text'], context['n'], context['e'])
    context['decrypted_text'] = decrypt(context['encrypted_text'], context['n'], context['d'])
    return context
