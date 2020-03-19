# coding: utf-8
import unittest

from rsa.validators import is_prime, key_length, PRIME_EXCEPTION, LENGTH_KEY_EXCEPTION, MESSAGE_EXCEPTION, \
    message_length


class TestUtil(unittest.TestCase):

    def setUp(self):
        self.char = "x"
        self.number = 88
        self.p = 17
        self.q = 11
        self.text_raise = "xxxx"
        self.char_raise = "x"
        self.number_raise = 200
        self.p_raise = 1
        self.q_raise = 1

    def test_is_prime_p_sucess(self):
        self.assertIsNone(is_prime(self.p))

    def test_is_prime_q_sucess(self):
        self.assertIsNone(is_prime(self.q))

    def test_key_length_number_sucess(self):
        self.assertIsNone(key_length(self.number, self.p, self.q))

    def test_key_length_string_sucess(self):
        self.assertIsNone(key_length(self.char, self.p, self.q))

    def test_is_prime_p_raise(self):
        with self.assertRaises(Exception) as context:
            is_prime(self.p_raise)
        self.assertTrue(PRIME_EXCEPTION in str(context.exception))

    def test_is_prime_q_raise(self):
        with self.assertRaises(Exception) as context:
            is_prime(self.q_raise)
        self.assertTrue(PRIME_EXCEPTION in str(context.exception))

    def test_key_length_number_raise(self):
        with self.assertRaises(Exception) as context:
            key_length(self.number_raise, self.p_raise, self.q_raise)
        self.assertTrue(LENGTH_KEY_EXCEPTION in str(context.exception))

    def test_key_length_string_raise(self):
        with self.assertRaises(Exception) as context:
            key_length(self.char, self.p_raise, self.q_raise)
        self.assertTrue(LENGTH_KEY_EXCEPTION in str(context.exception))

    def test_message_length_raise(self):
        with self.assertRaises(Exception) as context:
            message_length(self.text_raise)
        self.assertTrue(MESSAGE_EXCEPTION in str(context.exception))


if __name__ == '__main__':
    unittest.main()
