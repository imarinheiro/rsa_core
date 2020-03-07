# coding: utf-8
import unittest

from rsa.key import *


class TestKey(unittest.TestCase):

    def setUp(self):
        self.p = 17
        self.q = 11

    def test_n(self):
        self.assertEqual(calculate_n(self.p, self.q), 187)

    def test_tocient(self):
        self.assertEqual(calculate_tocient(self.p, self.q), 160)

    def test_e(self):
        phi = calculate_tocient(self.p, self.q)
        e = select_e(phi)
        self.assertLessEqual(e, phi, "It must be less than or equal to phi (tocient)")
        self.assertGreaterEqual(e, 2, "It must be greater than or equal 2")
        self.assertTrue(is_relatively_prime(e, phi), "It must be true")

    def test_d(self):
        # TODO: adicionar exemplo do livro stalllings para validar d
        phi = calculate_tocient(self.p, self.q)
        e = 7
        d = calculate_d(e, phi)
        self.assertEqual(d, 23, "It must be the equal")
        self.assertLess(d, phi, "It must be less than phi (tocient)")


if __name__ == '__main__':
    unittest.main()
