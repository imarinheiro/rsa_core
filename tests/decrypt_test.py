# coding: utf-8
import unittest

from rsa.decrypt import decrypt
from rsa.encrypt import encrypt
from rsa.key import calcular_tocient, selecionar_e, calcular_n, calcular_d


class TestDecrypt(unittest.TestCase):

    def setUp(self):
        self.p = 17
        self.q = 11
        self.n = calcular_n(self.p, self.q)
        self.phi = calcular_tocient(self.p, self.q)
        self.e = selecionar_e(self.phi)
        self.d = calcular_d(self.e, self.phi)
        self.message = 88
        self.encrypted_message = encrypt(88, self.n, self.e)

    def test_decrypt(self):
        decrypted_message = decrypt(self.encrypted_message, self.n, self.d)
        self.assertEqual(decrypted_message, self.message, "Deve ser igual")


if __name__ == '__main__':
    unittest.main()
