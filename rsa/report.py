# coding: utf-8
from rsa.decrypt import decrypt_number, decrypt_string
from rsa.encrypt import encrypt_number, encrypt_string
from rsa.key import calculate_n, select_e, calculate_tocient, calculate_d


def set_context_encrypt_number(number, p, q):
    """
    Gera chaves privadas e públicas a partir dos parâmetros 'p' e 'q', e posteriormente criptografa
    o número informado a partir do pâmetro number. Todos os estados são salvos em um dicionário
    como contexto da criptografia para análise.
    As seguintes função são utilizadas para gerar esse contexto do dicionário:

    :func:`select_e <rsa_core.rsa.key.calculate_n>`
    :func:`select_e <rsa_core.rsa.key.calculate_tocient>`
    :func:`select_e <rsa_core.rsa.key.select_e>`
    :func:`select_e <rsa_core.rsa.key.calculate_d>`
    :func:`select_e <rsa_core.rsa.encrypt.encrypt_number>`

    :param number: número inteiro que representa o número a ser criptografado
    :param p: número primo qualquer
    :param q: número primo qualquer
    :return: dicionário contento as seguintes chaves: 'plain_text', 'p', 'q', 'n', 'tocient', 'e', 'd',
    'public_key' e 'encrypted_text'
    """
    context = {}
    context['plain_text'] = number
    context['p'] = p
    context['q'] = q
    context['n'] = calculate_n(p, q)
    context['tocient'] = calculate_tocient(p, q)
    context['e'] = select_e(context['tocient'])
    context['d'] = calculate_d(context['e'], context['tocient'])
    context['public_key'] = (context['n'], context['e'])
    context['encrypted_text'] = encrypt_number(context['plain_text'], context['n'], context['e'])
    return context


def set_context_decrypt_number(number, p, q):
    """
    Gera chaves privadas e públicas a partir dos parâmetros 'p' e 'q', criptografa
    o número informado a partir do pâmetro number e posteriormente descriptografa o resultado.
    Todos os estados são salvos em um dicionário como contexto da criptografia para análise.
    As seguintes função são utilizadas para gerar esse contexto do dicionário:

    :func:`select_e <rsa_core.rsa.key.calculate_n>`
    :func:`select_e <rsa_core.rsa.key.calculate_tocient>`
    :func:`select_e <rsa_core.rsa.key.select_e>`
    :func:`select_e <rsa_core.rsa.key.calculate_d>`
    :func:`select_e <rsa_core.rsa.encrypt.encrypt_number>`
    :func:`select_e <rsa_core.rsa.decrypt.decrypt_number>`

    :param number: número inteiro que representa o número a ser criptografado
    :param p: número primo qualquer
    :param q: número primo qualquer
    :return: dicionário contento as seguintes chaves: 'plain_text', 'p', 'q', 'n', 'tocient', 'e', 'd', 'public_key',
    'encrypted_text' e 'decrypted_text'
    """
    context = {}
    context['plain_text'] = number
    context['p'] = p
    context['q'] = q
    context['n'] = calculate_n(p, q)
    context['tocient'] = calculate_tocient(p, q)
    context['e'] = select_e(context['tocient'])
    context['d'] = calculate_d(context['e'], context['tocient'])
    context['public_key'] = (context['n'], context['e'])
    context['encrypted_text'] = encrypt_number(context['plain_text'], context['n'], context['e'])
    context['decrypted_text'] = decrypt_number(context['encrypted_text'], context['n'], context['d'])
    return context


def set_context_encrypt_string(text, p, q):
    """
    Gera chaves privadas e públicas a partir dos parâmetros 'p' e 'q', e posteriormente criptografa
    o texto informado a partir do pâmetro text. Todos os estados são salvos em um dicionário
    como contexto da criptografia para análise.
    As seguintes função são utilizadas para gerar esse contexto do dicionário:

    :func:`select_e <rsa_core.rsa.key.calculate_n>`
    :func:`select_e <rsa_core.rsa.key.calculate_tocient>`
    :func:`select_e <rsa_core.rsa.key.select_e>`
    :func:`select_e <rsa_core.rsa.key.calculate_d>`
    :func:`select_e <rsa_core.rsa.encrypt.encrypt_string>`

    :param text: string que representa o texto a ser criptografado
    :param p: número primo qualquer
    :param q: número primo qualquer
    :return: dicionário contento as seguintes chaves: 'plain_text', 'p', 'q', 'n', 'tocient', 'e', 'd',
    'public_key' e 'encrypted_text'
    """
    context = {}
    context['plain_text'] = text
    context['p'] = p
    context['q'] = q
    context['n'] = calculate_n(p, q)
    context['tocient'] = calculate_tocient(p, q)
    context['e'] = select_e(context['tocient'])
    context['d'] = calculate_d(context['e'], context['tocient'])
    context['public_key'] = (context['n'], context['e'])
    context['encrypted_text'] = encrypt_string(context['plain_text'], context['n'], context['e'])
    return context


def set_context_decrypt_string(text, p, q):
    """
    Gera chaves privadas e públicas a partir dos parâmetros 'p' e 'q', criptografa
    o texto informado a partir do pâmetro text e posteriormente descriptografa o resultado.
    Todos os estados são salvos em um dicionário como contexto da criptografia para análise.
    As seguintes função são utilizadas para gerar esse contexto do dicionário:

    :func:`select_e <rsa_core.rsa.key.calculate_n>`
    :func:`select_e <rsa_core.rsa.key.calculate_tocient>`
    :func:`select_e <rsa_core.rsa.key.select_e>`
    :func:`select_e <rsa_core.rsa.key.calculate_d>`
    :func:`select_e <rsa_core.rsa.encrypt.encrypt_string>`
    :func:`select_e <rsa_core.rsa.decrypt.decrypt_string>`

    :param text: string que representa o texto a ser criptografado
    :param p: número primo qualquer
    :param q: número primo qualquer
    :return: dicionário contento as seguintes chaves: 'plain_text', 'p', 'q', 'n', 'tocient', 'e', 'd', 'public_key',
    'encrypted_text' e 'decrypted_text'
    """
    context = {}
    context['plain_text'] = text
    context['p'] = p
    context['q'] = q
    context['n'] = calculate_n(p, q)
    context['tocient'] = calculate_tocient(p, q)
    context['e'] = select_e(context['tocient'])
    context['d'] = calculate_d(context['e'], context['tocient'])
    context['public_key'] = (context['n'], context['e'])
    context['encrypted_text'] = encrypt_string(context['plain_text'], context['n'], context['e'])
    context['decrypted_text'] = decrypt_string(context['encrypted_text'], context['n'], context['d'])
    return context
