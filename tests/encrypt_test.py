# coding: utf-8
import unittest

from rsa.encrypt import encrypt
from rsa.key import calcular_tocient, calcular_n, calcular_d


class TestEncrypt(unittest.TestCase):

    def setUp(self):
        self.p = 17
        self.q = 11
        self.n = calcular_n(self.p, self.q)
        self.phi = calcular_tocient(self.p, self.q)
        self.e = 7
        self.d = calcular_d(self.e, self.phi)
        self.message = 88
        self.encrypted_message = 11

    def test_encrypt(self):
        encrypted_message = encrypt(self.message, self.n, self.e)
        self.assertEqual(encrypted_message, self.encrypted_message, "Deve ser igual")


if __name__ == '__main__':
    unittest.main()
