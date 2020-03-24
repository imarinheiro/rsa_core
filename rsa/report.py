# coding: utf-8
from rsa.decrypt import decrypt_number, decrypt_string
from rsa.encrypt import encrypt_number, encrypt_string
from rsa.key import calculate_n, select_e, calculate_tocient, calculate_d
from rsa.util import transform_string_to_number


def set_context_key(p: int, q: int):
    """
    Gera chaves privadas e públicas a partir dos parâmetros 'p' e 'q'.
    Todos os estados são salvos em um dicionário como contexto para análise.
    As seguintes função são utilizadas para gerar esse contexto do dicionário:

    :func:`calculate_n <rsa_core.rsa.key.calculate_n>`
    :func:`calculate_tocient <rsa_core.rsa.key.calculate_tocient>`
    :func:`select_e <rsa_core.rsa.key.select_e>`
    :func:`calculate_d <rsa_core.rsa.key.calculate_d>`

    :param p: número primo qualquer
    :param q: número primo qualquer
    :return: dicionário contento as seguintes chaves: 'p', 'q', 'n', 'tocient', 'e', 'd', 'public_key', 'private_key'
    """
    context = {}
    context['p'] = p
    context['q'] = q
    context['n'] = calculate_n(p, q)
    context['tocient'] = calculate_tocient(p, q)
    context['e'] = select_e(context['tocient'])
    context['d'] = calculate_d(context['e'], context['tocient'])
    context['public_key'] = (context['n'], context['e'])
    context['private_key'] = (context['n'], context['d'])
    return context


def set_context_key_encrypt_number(number: int, p: int, q: int):
    """
    Gera chaves privadas e públicas a partir dos parâmetros 'p' e 'q', e posteriormente criptografa
    o número informado a partir do pâmetro number. Todos os estados são salvos em um dicionário
    como contexto da criptografia para análise.
    As seguintes função são utilizadas para gerar esse contexto do dicionário:

    :func:`calculate_n <rsa_core.rsa.key.calculate_n>`
    :func:`calculate_tocient <rsa_core.rsa.key.calculate_tocient>`
    :func:`select_e <rsa_core.rsa.key.select_e>`
    :func:`calculate_d <rsa_core.rsa.key.calculate_d>`
    :func:`encrypt_number <rsa_core.rsa.encrypt.encrypt_number>`

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


def set_context_key_encrypt_decrypt_number(number: int, p: int, q: int):
    """
    Gera chaves privadas e públicas a partir dos parâmetros 'p' e 'q', criptografa
    o número informado a partir do pâmetro number e posteriormente descriptografa o resultado.
    Todos os estados são salvos em um dicionário como contexto da criptografia para análise.
    As seguintes função são utilizadas para gerar esse contexto do dicionário:

    :func:`calculate_n <rsa_core.rsa.key.calculate_n>`
    :func:`calculate_tocient <rsa_core.rsa.key.calculate_tocient>`
    :func:`select_e <rsa_core.rsa.key.select_e>`
    :func:`calculate_d <rsa_core.rsa.key.calculate_d>`
    :func:`encrypt_number <rsa_core.rsa.encrypt.encrypt_number>`
    :func:`decrypt_number <rsa_core.rsa.decrypt.decrypt_number>`

    :param number: número inteiro que representa o número a ser criptografado
    :param p: número primo qualquer
    :param q: número primo qualquer
    :return: dicionário contento as seguintes chaves: 'plain_text', 'p', 'q', 'n', 'tocient', 'e', 'd', 'public_key',
    'private_key', 'encrypted_text' e 'decrypted_text'
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
    context['private_key'] = (context['n'], context['d'])
    context['encrypted_text'] = encrypt_number(context['plain_text'], context['n'], context['e'])
    context['decrypted_text'] = decrypt_number(context['encrypted_text'], context['n'], context['d'])
    return context


def set_context_key_encrypt_string(text: str, p: int, q: int):
    """
    Gera chaves privadas e públicas a partir dos parâmetros 'p' e 'q', e posteriormente criptografa
    o texto informado a partir do pâmetro text. Todos os estados são salvos em um dicionário
    como contexto da criptografia para análise.
    As seguintes função são utilizadas para gerar esse contexto do dicionário:

    :func:`transform_string_to_number <rsa_core.rsa.util.transform_string_to_number>`
    :func:`calculate_n <rsa_core.rsa.key.calculate_n>`
    :func:`calculate_tocient <rsa_core.rsa.key.calculate_tocient>`
    :func:`select_e <rsa_core.rsa.key.select_e>`
    :func:`calculate_d <rsa_core.rsa.key.calculate_d>`
    :func:`encrypt_string <rsa_core.rsa.encrypt.encrypt_string>`

    :param text: string que representa o texto a ser criptografado
    :param p: número primo qualquer
    :param q: número primo qualquer
    :return: dicionário contento as seguintes chaves: 'plain_text', 'converted_text', 'p', 'q', 'n', 'tocient', 'e',
    'd', 'public_key' e 'encrypted_text'
    """
    context = {}
    context['plain_text'] = text
    context['converted_text'] = transform_string_to_number(text)
    context['p'] = p
    context['q'] = q
    context['n'] = calculate_n(p, q)
    context['tocient'] = calculate_tocient(p, q)
    context['e'] = select_e(context['tocient'])
    context['d'] = calculate_d(context['e'], context['tocient'])
    context['public_key'] = (context['n'], context['e'])
    context['encrypted_text'] = encrypt_string(context['plain_text'], context['n'], context['e'])
    return context


def set_context_key_encrypt_decrypt_string(text: str, p: int, q: int):
    """
    Gera chaves privadas e públicas a partir dos parâmetros 'p' e 'q', criptografa
    o texto informado a partir do pâmetro text e posteriormente descriptografa o resultado.
    Todos os estados são salvos em um dicionário como contexto da criptografia para análise.
    As seguintes função são utilizadas para gerar esse contexto do dicionário:

    :func:`transform_string_to_number <rsa_core.rsa.util.transform_string_to_number>`
    :func:`calculate_n <rsa_core.rsa.key.calculate_n>`
    :func:`calculate_tocient <rsa_core.rsa.key.calculate_tocient>`
    :func:`select_e <rsa_core.rsa.key.select_e>`
    :func:`calculate_d <rsa_core.rsa.key.calculate_d>`
    :func:`encrypt_string <rsa_core.rsa.encrypt.encrypt_string>`
    :func:`decrypt_string <rsa_core.rsa.decrypt.decrypt_string>`

    :param text: string que representa o texto a ser criptografado
    :param p: número primo qualquer
    :param q: número primo qualquer
    :return: dicionário contento as seguintes chaves: 'plain_text', 'converted_text', 'p', 'q', 'n', 'tocient', 'e',
    'd', 'public_key', 'private_key', 'encrypted_text' e 'decrypted_text'
    """
    context = {}
    context['plain_text'] = text
    context['converted_text'] = transform_string_to_number(text)
    context['p'] = p
    context['q'] = q
    context['n'] = calculate_n(p, q)
    context['tocient'] = calculate_tocient(p, q)
    context['e'] = select_e(context['tocient'])
    context['d'] = calculate_d(context['e'], context['tocient'])
    context['public_key'] = (context['n'], context['e'])
    context['private_key'] = (context['n'], context['d'])
    context['encrypted_text'] = encrypt_string(context['plain_text'], context['n'], context['e'])
    context['decrypted_text'] = decrypt_string(context['encrypted_text'], context['n'], context['d'])
    return context


# ######################################################################################################################

def set_context_encrypt_number(number: int, n: int, e: int):
    """
    Criptografa o número informado a partir da chave informada ('n', 'e'). Todos os estados são salvos em um dicionário
    como contexto da criptografia para análise.
    As seguintes função são utilizadas para gerar esse contexto do dicionário:

    :func:`encrypt_number <rsa_core.rsa.encrypt.encrypt_number>`

    :param number: número inteiro que representa o número a ser criptografado
    :param n: parte da chave pública
    :param e: parte da chave pública
    :return: dicionário contento as seguintes chaves: 'plain_text', 'n', 'e', 'public_key' e 'encrypted_text'
    """
    context = {}
    context['plain_text'] = number
    context['n'] = n
    context['e'] = e
    context['public_key'] = (context['n'], context['e'])
    context['encrypted_text'] = encrypt_number(context['plain_text'], context['n'], context['e'])
    return context


def set_context_decrypt_number(encryted_number: int, n: int, d: int):
    """
    Descriptografa o número informado a partir da chave informada ('n', 'd').
    Todos os estados são salvos em um dicionário como contexto da criptografia para análise.
    As seguintes função são utilizadas para gerar esse contexto do dicionário:

    :func:`decrypt_number <rsa_core.rsa.decrypt.decrypt_number>`

    :param encryted_number: número inteiro que representa o número a ser criptografado
    :param n: parte da chave privada
    :param d: parte da chave privada
    :return: dicionário contento as seguintes chaves: 'encryted_text', 'n', 'd', 'private_key' e 'decrypted_text'
    """
    context = {}
    context['encrypted_text'] = encryted_number
    context['n'] = n
    context['d'] = d
    context['private_key'] = (context['n'], context['d'])
    context['decrypted_text'] = decrypt_number(context['encrypted_text'], context['n'], context['d'])
    return context


def set_context_encrypt_string(text: str, n: int, e: int):
    """
    Criptografa o texto informado a partir da chave informada ('n', 'e').
    Todos os estados são salvos em um dicionário como contexto da criptografia para análise.
    As seguintes função são utilizadas para gerar esse contexto do dicionário:

    :func:`transform_string_to_number <rsa_core.rsa.util.transform_string_to_number>`
    :func:`encrypt_string <rsa_core.rsa.encrypt.encrypt_string>`

    :param text: string que representa o texto a ser criptografado
    :param n: parte da chave pública
    :param e: parte da chave pública
    :return: dicionário contento as seguintes chaves: 'plain_text', 'converted_text', 'n', 'e', 'public_key'
    e 'encrypted_text'
    """
    context = {}
    context['plain_text'] = text
    context['converted_text'] = transform_string_to_number(text)
    context['n'] = n
    context['e'] = e
    context['public_key'] = (context['n'], context['e'])
    context['encrypted_text'] = encrypt_string(context['plain_text'], context['n'], context['e'])
    return context


def set_context_decrypt_string(encrypted_text: int, n: int, d: int):
    """
    Descriptografa o texto informado a partir da chave informada ('n', 'd').
    Todos os estados são salvos em um dicionário como contexto da criptografia para análise.
    As seguintes função são utilizadas para gerar esse contexto do dicionário:

    :func:`transform_string_to_number <rsa_core.rsa.util.transform_string_to_number>`
    :func:`decrypt_string <rsa_core.rsa.decrypt.decrypt_string>`

    :param encrypted_text: string que representa o texto a ser criptografado
    :param n: parte da chave privada
    :param d: parte da chave privada
    :return: dicionário contento as seguintes chaves: 'encrypted_text', 'converted_text', 'n', 'd',
    'private_key' e 'decrypted_text'
    """
    context = {}
    context['encrypted_text'] = encrypted_text
    context['n'] = n
    context['d'] = d
    context['private_key'] = (context['n'], context['d'])
    context['decrypted_text'] = decrypt_string(context['encrypted_text'], context['n'], context['d'])
    return context
