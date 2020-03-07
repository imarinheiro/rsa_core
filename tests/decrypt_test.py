# coding: utf-8
import unittest

from rsa.decrypt import decrypt
from rsa.encrypt import encrypt_number
from rsa.key import calculate_tocient, select_e, calculate_n, calculate_d


class TestDecrypt(unittest.TestCase):

    def setUp(self):
        self.p = 17
        self.q = 11
        self.n = calculate_n(self.p, self.q)
        self.phi = calculate_tocient(self.p, self.q)
        self.e = select_e(self.phi)
        self.d = calculate_d(self.e, self.phi)
        self.message = 88
        self.encrypted_message = encrypt_number(88, self.n, self.e)

    def test_decrypt(self):
        decrypted_message = decrypt(self.encrypted_message, self.n, self.d)
        self.assertEqual(decrypted_message, self.message, "It must be equal")


if __name__ == '__main__':
    unittest.main()
