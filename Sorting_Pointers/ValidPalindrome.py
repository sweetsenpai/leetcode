"""
Valid Palindrome

A phrase is a palindrome if, after converting all uppercase letters into lowercase letters and removing all non-alphanumeric characters, it reads the same forward and backward. Alphanumeric characters include letters and numbers.

Given a string s, return true if it is a palindrome, or false otherwise.

https://leetcode.com/problems/valid-palindrome/
"""


class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = "".join(filter(str.isalnum, s)).lower()

        for left in range(len(s) // 2):
            if s[left] != s[len(s) - 1 - left]:
                return False
        return True
