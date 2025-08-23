import unittest
from src.one_function_code.ValidEmails import Solution

class TestValidEmails(unittest.TestCase):
    def test_num_unique_emails(self):
        sol = Solution()
        emails = [
            "test.email+alex@leetcode.com",
            "test.e.mail+bob.cathy@leetcode.com",
            "testemail+david@lee.tcode.com"
        ]
        self.assertEqual(sol.numUniqueEmails(emails), 2)
        emails2 = [
            "a@leetcode.com",
            "b@leetcode.com",
            "c@leetcode.com"
        ]
        self.assertEqual(sol.numUniqueEmails(emails2), 3)
        emails3 = [
            "a+b@leetcode.com",
            "a@leetcode.com"
        ]
        self.assertEqual(sol.numUniqueEmails(emails3), 1)

if __name__ == "__main__":
    unittest.main()

