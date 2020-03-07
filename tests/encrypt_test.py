# coding: utf-8
import unittest

from rsa.encrypt import encrypt_number, encrypt_string
from rsa.key import calculate_tocient, calculate_n, calculate_d

ENCRYPT_MESSAGE = "It must be equal"


class TestEncrypt(unittest.TestCase):

    def setUp(self):
        self.p = 17
        self.q = 11
        self.n = calculate_n(self.p, self.q)
        self.phi = calculate_tocient(self.p, self.q)
        self.e = 7
        self.d = calculate_d(self.e, self.phi)
        self.number = 88
        self.encrypted_number = 11
        self.text = "i"
        self.encrypted_text = 96

    def test_encrypt_number(self):
        encrypted_message = encrypt_number(self.number, self.n, self.e)
        self.assertEqual(encrypted_message, self.encrypted_number, ENCRYPT_MESSAGE)

    def test_encrypt_text(self):
        encrypted_message = encrypt_string(self.text, self.n, self.e)
        self.assertEqual(encrypted_message, self.encrypted_text, ENCRYPT_MESSAGE)


if __name__ == '__main__':
    unittest.main()
