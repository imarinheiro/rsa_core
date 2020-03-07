# coding: utf-8
from rsa.decrypt import decrypt
from rsa.encrypt import encrypt_number
from rsa.key import calculate_n, select_e, calculate_tocient, calculate_d


# TODO: Adicionar doc strings


def set_context_encrypt(message, p, q):
    context = {}
    context['plain_text'] = message
    context['p'] = p
    context['q'] = q
    context['n'] = calculate_n(p, q)
    context['tocient'] = calculate_tocient(p, q)
    context['e'] = select_e(context['tocient'])
    context['d'] = calculate_d(context['e'], context['tocient'])
    context['public_key'] = (context['n'], context['e'])
    context['encrypted_text'] = encrypt_number(context['plain_text'], context['n'], context['e'])
    return context


def set_context_decrypt(message, p, q):
    context = {}
    context['plain_text'] = message
    context['p'] = p
    context['q'] = q
    context['n'] = calculate_n(p, q)
    context['tocient'] = calculate_tocient(p, q)
    context['e'] = select_e(context['tocient'])
    context['d'] = calculate_d(context['e'], context['tocient'])
    context['public_key'] = (context['n'], context['e'])
    context['encrypted_text'] = encrypt_number(context['plain_text'], context['n'], context['e'])
    context['decrypted_text'] = decrypt(context['encrypted_text'], context['n'], context['d'])
    return context


# message = "iago"
# by = bytes(message)
# by_list = list(by)
# # >> [105, 97, 103, 111]
# "".join(map(chr, by_list))
# # >> 'iago'
# int.from_bytes(by, byteorder='big')
# int.from


d = set_context_decrypt(252, 23, 11)
print(d)
