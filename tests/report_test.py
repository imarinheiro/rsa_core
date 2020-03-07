# coding: utf-8
import unittest

from rsa.decrypt import decrypt
from rsa.encrypt import encrypt_number
from rsa.key import calculate_tocient, select_e, calculate_n, calculate_d
from rsa.report import set_context_encrypt, set_context_decrypt


class TestReport(unittest.TestCase):

    def setUp(self):
        self.p = 17
        self.q = 11
        self.n = calculate_n(self.p, self.q)
        self.phi = calculate_tocient(self.p, self.q)
        self.e = select_e(self.phi)
        self.d = calculate_d(self.e, self.phi)
        self.message = 88
        self.encrypted_message = encrypt_number(88, self.n, self.e)
        self.decrypted_message = decrypt(44, self.n, self.d)

    def test_context_encrypt(self):
        context = set_context_encrypt(self.message, self.p, self.q)
        self.assertEqual(context['plain_text'], self.message, "Mensagem deve ser igual")
        self.assertEqual(context['p'], self.p, "P (primo) deve ser igual")
        self.assertEqual(context['q'], self.q, "Q (primo) deve ser igual")
        self.assertEqual(context['n'], self.n, "N deve ser igual")
        self.assertEqual(context['tocient'], self.phi, "Tocient deve ser igual")
        self.assertEqual(context['e'], self.e, "E Deve ser igual")
        self.assertEqual(context['d'], self.d, "D Deve ser igual")
        self.assertEqual(context['public_key'], (self.n, self.e), "Chave Publica deve ser igual")
        self.assertEqual(context['encrypted_text'], self.encrypted_message, "Texto criptografado Deve ser igual")

    def test_context_decrypt(self):
        context = set_context_decrypt(self.message, self.p, self.q)
        self.assertEqual(context['plain_text'], self.message, "Mensagem deve ser igual")
        self.assertEqual(context['p'], self.p, "P (primo) deve ser igual")
        self.assertEqual(context['q'], self.q, "Q (primo) deve ser igual")
        self.assertEqual(context['n'], self.n, "N deve ser igual")
        self.assertEqual(context['tocient'], self.phi, "Tocient deve ser igual")
        self.assertEqual(context['e'], self.e, "E Deve ser igual")
        self.assertEqual(context['d'], self.d, "D Deve ser igual")
        self.assertEqual(context['public_key'], (self.n, self.e), "Chave Publica deve ser igual")
        self.assertEqual(context['encrypted_text'], self.encrypted_message, "Texto criptografado deve ser igual")
        self.assertEqual(context['decrypted_text'], self.decrypted_message, "Texto descriptografado deve ser igual")


if __name__ == '__main__':
    unittest.main()
