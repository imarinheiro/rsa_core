# coding: utf-8
import unittest

from rsa.key import *


class TestKey(unittest.TestCase):

    def setUp(self):
        self.p = 17
        self.q = 11

    def test_n(self):
        self.assertEqual(calcular_n(self.p, self.q), 187)

    def test_tocient(self):
        self.assertEqual(calcular_tocient(self.p, self.q), 160)

    def test_e(self):
        phi = calcular_tocient(self.p, self.q)
        e = selecionar_e(phi)
        self.assertLessEqual(e, phi, "Deve ser menor ou igual a phi (tocient)")
        self.assertGreaterEqual(e, 2, "Deve ser maior ou igual 2")
        self.assertTrue(is_relatively_prime(e, phi), "Deve ser verdadeiro")

    def test_d(self):
        # TODO: adicionar exemplo do livro stalllings para validar d
        phi = calcular_tocient(self.p, self.q)
        e = 7
        d = calcular_d(e, phi)
        self.assertEqual(d, 23, "Deve ser igual")
        self.assertLess(d, phi, "Deve ser menor que phi (tocient)")


if __name__ == '__main__':
    unittest.main()
