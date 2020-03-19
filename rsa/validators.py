# coding: utf-8
from sympy import isprime

from rsa.util import transform_string_to_number

PRIME_EXCEPTION = 'It must be prime number'
LENGTH_KEY_EXCEPTION = 'The key must be greater than message'
MESSAGE_EXCEPTION = 'The message must contains only one character'


def is_prime(number):
    if not isprime(number):
        raise Exception(PRIME_EXCEPTION)


def key_length(message, p, q):
    result = None
    if type(message) is int:
        result = message
    if type(message) is str:
        result = transform_string_to_number(message)
    if result >= p * q:
        raise Exception(LENGTH_KEY_EXCEPTION)


def message_length(message):
    if type(message) is str and len(message) > 1:
        raise Exception(MESSAGE_EXCEPTION)
