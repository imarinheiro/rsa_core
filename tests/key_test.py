# coding: utf-8
import unittest

from rsa.key import *

N_MESSAGE = "N = (P *Q) must be equal"
TOCIENT_MESSAGE = "Tocient must be equal"
E_LT_TOCIENT_MESSAGE = "It must be less than or equal to phi (tocient)"
E_GT_TWO_MESSAGE = "It must be less than or equal to phi (tocient)"
E_IS_PRIME_MESSAGE = "It must be true"
D_MESSAGE = "D must be equal"
D_LESS_THAN_PHI_MESSAGE = "D must be less than phi (tocient)"


class TestKey(unittest.TestCase):

    def setUp(self):
        self.p = 17
        self.q = 11

    def test_n(self):
        self.assertEqual(calculate_n(self.p, self.q), 187, N_MESSAGE)

    def test_tocient(self):
        self.assertEqual(calculate_tocient(self.p, self.q), 160, TOCIENT_MESSAGE)

    def test_e(self):
        phi = calculate_tocient(self.p, self.q)
        e = select_e(phi)
        self.assertLessEqual(e, phi, E_LT_TOCIENT_MESSAGE)
        self.assertGreaterEqual(e, 2, E_GT_TWO_MESSAGE)
        self.assertTrue(is_relatively_prime(e, phi), E_IS_PRIME_MESSAGE)

    def test_d(self):
        phi = calculate_tocient(self.p, self.q)
        e = 7
        d = calculate_d(e, phi)
        self.assertEqual(d, 23, D_MESSAGE)
        self.assertLess(d, phi, D_LESS_THAN_PHI_MESSAGE)


if __name__ == '__main__':
    unittest.main()
