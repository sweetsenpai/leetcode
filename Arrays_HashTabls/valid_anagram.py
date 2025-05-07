"""
https://leetcode.com/problems/valid-anagram/
Given two strings s and t, return true if t is an of s, and false otherwise.
"""


class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        dict_s = {item: s.count(item) for item in set(s)}
        dict_b = {item: t.count(item) for item in set(t)}
        return dict_b == dict_s
