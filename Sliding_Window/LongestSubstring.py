"""
Longest substring without repeating characters
Given a string s, find the length of the longest substring without duplicate characters.

https://leetcode.com/problems/longest-substring-without-repeating-characters/description/
"""

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        left = 0
        seen_letters = set()
        max_len = 0
        for right, letter  in enumerate(s):
            while letter in seen_letters:
                seen_letters.remove(s[left])
                left += 1
            seen_letters.add(letter)
            max_len = max(max_len, right - left + 1)
        return max_len


