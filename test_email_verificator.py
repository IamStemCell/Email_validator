import unittest
from email_verificator import is_valid_email

class TestEmailValidator(unittest.TestCase):

    def test_valid_email(self):
        self.assertTrue(is_valid_email("user@gmail.com"))

    def test_invalid_format(self):
        self.assertFalse(is_valid_email("user[at]gmail.com"))

    def test_whitelist(self):
        self.assertTrue(is_valid_email("user@example.com", whitelist=["example.com"]))
        self.assertFalse(is_valid_email("user@other.com", whitelist=["example.com"]))

    def test_blacklist(self):
        self.assertFalse(is_valid_email("user@spam.com", blacklist=["spam.com"]))

if __name__ == '__main__':
    unittest.main()
  
