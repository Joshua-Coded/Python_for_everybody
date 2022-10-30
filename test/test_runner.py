# run test with text runner

import unittest

class TextFoo(unittest.TestCase):
    def test_foo(self):
        self.assertTrue(True)
    def test_bar(self):
        self.assertFalse(False)


suite = unittest.TestLoader().loadTestsFromTestCase(TestFoo)
unittest.TextTestRunner(verbosity=2).run(suite)

test_bar (__main__.TestFoo) ... ok
test_foo (__main__.TestFoo) ... ok



