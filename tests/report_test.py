# coding: utf-8
import unittest

from rsa.decrypt import decrypt_number, decrypt_string
from rsa.encrypt import encrypt_number, encrypt_string
from rsa.key import calculate_tocient, select_e, calculate_n, calculate_d
from rsa.report import \
    set_context_key, \
    set_context_key_encrypt_number, \
    set_context_key_encrypt_decrypt_number, \
    set_context_key_encrypt_string, \
    set_context_key_encrypt_decrypt_string, \
    set_context_encrypt_number, \
    set_context_decrypt_number, \
    set_context_encrypt_string, \
    set_context_decrypt_string

PLAIN_TEXT_MESSAGE = "The message must be the equal"
CONVERTED_TEXT_MESSAGE = "The converted text must be the equal"
P_PRIME_MESSAGE = "P (prime) must be equal"
Q_PRIME_MESSAGE = "Q (prime) must be equal"
N_PRIME_MESSAGE = "N must be equal"
TOCIENT_MESSAGE = "Tocient must be equal"
E_MESSAGE = "E must be equal"
D_MESSAGE = "D must be equal"
PUBLIC_KEY_MESSAGE = "The Public Key must be equal"
PRIVATE_KEY_MESSAGE = "The Private Key must be equal"
ENCRYPTED_MESSAGE = "The encrypted must be equal"
DECRYPTED_MESSAGE = "The decrypted must be equal"


class TestReport(unittest.TestCase):

    def setUp(self):
        self.p = 17
        self.q = 11
        self.n = calculate_n(self.p, self.q)
        self.phi = calculate_tocient(self.p, self.q)
        self.e = select_e(self.phi)
        self.d = calculate_d(self.e, self.phi)
        self.number = 88
        self.encrypted_number = encrypt_number(88, self.n, self.e)
        self.decrypted_number = decrypt_number(44, self.n, self.d)
        self.text = "i"
        self.converted_text = 105
        self.encrypted_text = encrypt_string("i", self.n, self.e)
        self.decrypted_text = decrypt_string(95, self.n, self.d)
        self.public_key = (self.n, self.e)
        self.private_key = (self.n, self.d)

    def test_context_key(self):
        context = set_context_key(self.p, self.q)
        self.assertEqual(context['p'], self.p, P_PRIME_MESSAGE)
        self.assertEqual(context['q'], self.q, Q_PRIME_MESSAGE)
        self.assertEqual(context['n'], self.n, N_PRIME_MESSAGE)
        self.assertEqual(context['tocient'], self.phi, TOCIENT_MESSAGE)
        self.assertEqual(context['e'], self.e, E_MESSAGE)
        self.assertEqual(context['d'], self.d, D_MESSAGE)
        self.assertEqual(context['public_key'], self.public_key, PUBLIC_KEY_MESSAGE)
        self.assertEqual(context['private_key'], self.private_key, PRIVATE_KEY_MESSAGE)

    def test_context_encrypt_number_without_key(self):
        context = set_context_key_encrypt_number(self.number, self.p, self.q)
        self.assertEqual(context['plain_text'], self.number, PLAIN_TEXT_MESSAGE)
        self.assertEqual(context['p'], self.p, P_PRIME_MESSAGE)
        self.assertEqual(context['q'], self.q, Q_PRIME_MESSAGE)
        self.assertEqual(context['n'], self.n, N_PRIME_MESSAGE)
        self.assertEqual(context['tocient'], self.phi, TOCIENT_MESSAGE)
        self.assertEqual(context['e'], self.e, E_MESSAGE)
        self.assertEqual(context['d'], self.d, D_MESSAGE)
        self.assertEqual(context['public_key'], self.public_key, PUBLIC_KEY_MESSAGE)
        self.assertEqual(context['encrypted_text'], self.encrypted_number, ENCRYPTED_MESSAGE)

    def test_context_decrypt_number_without_key(self):
        context = set_context_key_encrypt_decrypt_number(self.number, self.p, self.q)
        self.assertEqual(context['plain_text'], self.number, PLAIN_TEXT_MESSAGE)
        self.assertEqual(context['p'], self.p, P_PRIME_MESSAGE)
        self.assertEqual(context['q'], self.q, Q_PRIME_MESSAGE)
        self.assertEqual(context['n'], self.n, N_PRIME_MESSAGE)
        self.assertEqual(context['tocient'], self.phi, TOCIENT_MESSAGE)
        self.assertEqual(context['e'], self.e, E_MESSAGE)
        self.assertEqual(context['d'], self.d, D_MESSAGE)
        self.assertEqual(context['public_key'], self.public_key, PUBLIC_KEY_MESSAGE)
        self.assertEqual(context['private_key'], self.private_key, PRIVATE_KEY_MESSAGE)
        self.assertEqual(context['encrypted_text'], self.encrypted_number, ENCRYPTED_MESSAGE)
        self.assertEqual(context['decrypted_text'], self.decrypted_number, DECRYPTED_MESSAGE)

    def test_context_encrypt_string_without_key(self):
        context = set_context_key_encrypt_string(self.text, self.p, self.q)
        self.assertEqual(context['plain_text'], self.text, PLAIN_TEXT_MESSAGE)
        self.assertEqual(context['converted_text'], self.converted_text, CONVERTED_TEXT_MESSAGE)
        self.assertEqual(context['p'], self.p, P_PRIME_MESSAGE)
        self.assertEqual(context['q'], self.q, Q_PRIME_MESSAGE)
        self.assertEqual(context['n'], self.n, N_PRIME_MESSAGE)
        self.assertEqual(context['tocient'], self.phi, TOCIENT_MESSAGE)
        self.assertEqual(context['e'], self.e, E_MESSAGE)
        self.assertEqual(context['d'], self.d, D_MESSAGE)
        self.assertEqual(context['public_key'], self.public_key, PUBLIC_KEY_MESSAGE)
        self.assertEqual(context['encrypted_text'], self.encrypted_text, ENCRYPTED_MESSAGE)

    def test_context_decrypt_string_without_key(self):
        context = set_context_key_encrypt_decrypt_string(self.text, self.p, self.q)
        self.assertEqual(context['plain_text'], self.text, PLAIN_TEXT_MESSAGE)
        self.assertEqual(context['converted_text'], self.converted_text, CONVERTED_TEXT_MESSAGE)
        self.assertEqual(context['p'], self.p, P_PRIME_MESSAGE)
        self.assertEqual(context['q'], self.q, Q_PRIME_MESSAGE)
        self.assertEqual(context['n'], self.n, N_PRIME_MESSAGE)
        self.assertEqual(context['tocient'], self.phi, TOCIENT_MESSAGE)
        self.assertEqual(context['e'], self.e, E_MESSAGE)
        self.assertEqual(context['d'], self.d, D_MESSAGE)
        self.assertEqual(context['public_key'], self.public_key, PUBLIC_KEY_MESSAGE)
        self.assertEqual(context['private_key'], self.private_key, PRIVATE_KEY_MESSAGE)
        self.assertEqual(context['encrypted_text'], self.encrypted_text, ENCRYPTED_MESSAGE)
        self.assertEqual(context['decrypted_text'], self.decrypted_text, DECRYPTED_MESSAGE)

    def test_context_encrypt_number_with_key(self):
        context = set_context_encrypt_number(self.number, self.n, self.e)
        self.assertEqual(context['plain_text'], self.number, PLAIN_TEXT_MESSAGE)
        self.assertEqual(context['n'], self.n, N_PRIME_MESSAGE)
        self.assertEqual(context['e'], self.e, E_MESSAGE)
        self.assertEqual(context['public_key'], self.public_key, PUBLIC_KEY_MESSAGE)
        self.assertEqual(context['encrypted_text'], self.encrypted_number, ENCRYPTED_MESSAGE)

    def test_context_decrypt_number_with_key(self):
        context = set_context_decrypt_number(self.encrypted_number, self.n, self.d)
        self.assertEqual(context['encrypted_text'], self.encrypted_number, ENCRYPTED_MESSAGE)
        self.assertEqual(context['n'], self.n, N_PRIME_MESSAGE)
        self.assertEqual(context['d'], self.d, D_MESSAGE)
        self.assertEqual(context['private_key'], self.private_key, PRIVATE_KEY_MESSAGE)
        self.assertEqual(context['decrypted_text'], self.decrypted_number, DECRYPTED_MESSAGE)

    def test_context_encrypt_string_with_key(self):
        context = set_context_encrypt_string(self.text, self.n, self.e)
        self.assertEqual(context['plain_text'], self.text, PLAIN_TEXT_MESSAGE)
        self.assertEqual(context['converted_text'], self.converted_text, CONVERTED_TEXT_MESSAGE)
        self.assertEqual(context['n'], self.n, N_PRIME_MESSAGE)
        self.assertEqual(context['e'], self.e, E_MESSAGE)
        self.assertEqual(context['public_key'], self.public_key, PUBLIC_KEY_MESSAGE)
        self.assertEqual(context['encrypted_text'], self.encrypted_text, ENCRYPTED_MESSAGE)

    def test_context_decrypt_string_with_key(self):
        context = set_context_decrypt_string(self.encrypted_text, self.n, self.d)
        self.assertEqual(context['encrypted_text'], self.encrypted_text, ENCRYPTED_MESSAGE)
        self.assertEqual(context['n'], self.n, N_PRIME_MESSAGE)
        self.assertEqual(context['d'], self.d, D_MESSAGE)
        self.assertEqual(context['private_key'], self.private_key, PRIVATE_KEY_MESSAGE)
        self.assertEqual(context['decrypted_text'], self.decrypted_text, DECRYPTED_MESSAGE)


if __name__ == '__main__':
    unittest.main()
