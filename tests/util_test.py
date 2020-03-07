# coding: utf-8
import unittest

from rsa.key import calculate_tocient, select_e
from rsa.util import *


class TestUtil(unittest.TestCase):

    def setUp(self):
        self.p = 17
        self.q = 11

    def test_relative_prime(self):
        phi = calculate_tocient(self.p, self.q)
        e = select_e(phi)
        self.assertTrue(is_relatively_prime(e, phi), "Deve ser relativamente primo")

    def test_not_relative_prime(self):
        phi = calculate_tocient(self.p, self.q)
        e = 8
        self.assertFalse(is_relatively_prime(e, phi), "Não deve ser relativamente primo")


if __name__ == '__main__':
    unittest.main()
