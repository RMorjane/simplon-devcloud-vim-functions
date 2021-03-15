import unittest
from str_reverse import str_reverse

class TestStrReverse(unittest.TestCase):

    def test_str_reverse(self):
        str_value = "tester"
        rev_value = str_reverse(str_value)
        self.assertEquals(rev_value,"retset")

if __name__ == "__main__":
    unittest.main()
