# coding: utf-8
import unittest

from rsa.key import calculate_tocient, select_e
from rsa.util import *

PRIME_MESSAGE = "It must be relatively prime"
NOT_PRIME_MESSAGE = "It shouldn't be relatively prime"


class TestUtil(unittest.TestCase):

    def setUp(self):
        self.p = 17
        self.q = 11

    def test_relatively_prime(self):
        phi = calculate_tocient(self.p, self.q)
        e = select_e(phi)
        self.assertTrue(is_relatively_prime(e, phi), PRIME_MESSAGE)

    def test_not_relatively_prime(self):
        phi = calculate_tocient(self.p, self.q)
        e = 8
        self.assertFalse(is_relatively_prime(e, phi), NOT_PRIME_MESSAGE)


if __name__ == '__main__':
    unittest.main()
