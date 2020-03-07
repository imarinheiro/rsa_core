# coding: utf-8
import unittest

from rsa.decrypt import decrypt_number, decrypt_string
from rsa.encrypt import encrypt_number, encrypt_string
from rsa.key import calculate_tocient, select_e, calculate_n, calculate_d

DECRYPT_MESSAGE = "It must be equal"


class TestDecrypt(unittest.TestCase):

    def setUp(self):
        self.p = 17
        self.q = 11
        self.n = calculate_n(self.p, self.q)
        self.phi = calculate_tocient(self.p, self.q)
        self.e = select_e(self.phi)
        self.d = calculate_d(self.e, self.phi)
        self.number = 88
        self.text = "i"
        self.encrypted_number = encrypt_number(self.number, self.n, self.e)
        self.encrypted_text = encrypt_string(self.text, self.n, self.e)

    def test_decrypt_number(self):
        decrypted_message = decrypt_number(self.encrypted_number, self.n, self.d)
        self.assertEqual(decrypted_message, self.number, DECRYPT_MESSAGE)

    def test_decrypt_text(self):
        decrypted_message = decrypt_string(self.encrypted_text, self.n, self.d)
        self.assertEqual(decrypted_message, self.text, DECRYPT_MESSAGE)


if __name__ == '__main__':
    unittest.main()
