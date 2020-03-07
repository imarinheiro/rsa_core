# coding: utf-8
import unittest

from rsa.encrypt import encrypt_number
from rsa.key import calculate_tocient, calculate_n, calculate_d


class TestEncrypt(unittest.TestCase):

    def setUp(self):
        self.p = 17
        self.q = 11
        self.n = calculate_n(self.p, self.q)
        self.phi = calculate_tocient(self.p, self.q)
        self.e = 7
        self.d = calculate_d(self.e, self.phi)
        self.message = 88
        self.encrypted_message = 11

    def test_encrypt(self):
        encrypted_message = encrypt_number(self.message, self.n, self.e)
        self.assertEqual(encrypted_message, self.encrypted_message, "It must be equal")


if __name__ == '__main__':
    unittest.main()
