# -*- coding: utf-8 -*-
from __future__ import unicode_literals

import unittest

from tests.decrypt_test import TestDecrypt
from tests.encrypt_test import TestEncrypt
from tests.key_test import TestKey
from tests.report_test import TestReport
from tests.util_test import TestUtil
from tests.validators_test import TestValidators


def main():
    suite_key = unittest.TestLoader().loadTestsFromTestCase(TestKey)
    suite_cipher = unittest.TestLoader().loadTestsFromTestCase(TestEncrypt)
    suite_decipher = unittest.TestLoader().loadTestsFromTestCase(TestDecrypt)
    suite_report = unittest.TestLoader().loadTestsFromTestCase(TestReport)
    suite_util = unittest.TestLoader().loadTestsFromTestCase(TestUtil)
    suite_validators = unittest.TestLoader().loadTestsFromTestCase(TestValidators)

    suite_tests = unittest.TestSuite(
        [suite_key,
         suite_cipher,
         suite_decipher,
         suite_report,
         suite_util,
         suite_validators])
    unittest.TextTestRunner(verbosity=2).run(suite_tests)


if __name__ == '__main__':
    main()
