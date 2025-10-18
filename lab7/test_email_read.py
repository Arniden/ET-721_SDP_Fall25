"""
Unit test for email_read() in lab7_function.py
"""
import unittest
from lab7.lab7_function import email_read
import os

class TestEmailRead(unittest.TestCase):
    def test_email_read_counts(self):
        # Path to provided user_email.txt in lab7
        filepath = os.path.join(os.path.dirname(__file__), 'user_email.txt')
        # expected counts based on the provided file
        expected_gmail = 6
        expected_yahoo = 3
        expected_hotmail = 4

        gmail_count, yahoo_count, hotmail_count = email_read(filepath)

        self.assertEqual(gmail_count, expected_gmail)
        self.assertEqual(yahoo_count, expected_yahoo)
        self.assertEqual(hotmail_count, expected_hotmail)

if __name__ == '__main__':
    unittest.main()
