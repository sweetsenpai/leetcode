"""
Valid Parentheses
Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.

An input string is valid if:

    Open brackets must be closed by the same type of brackets.
    Open brackets must be closed in the correct order.
    Every close bracket has a corresponding open bracket of the same type.

https://leetcode.com/problems/valid-parentheses/description/
"""
from collections import defaultdict


class Solution:
    def isValid(self, s: str) -> bool:
        bracket_dict = {')': '(', '}': '{', ']': '['}
        stack = []

        for bracket in s:
            if bracket in bracket_dict:
                if not (stack and stack.pop() == bracket_dict[bracket]):
                    return False
            else:
                stack.append(bracket)
        return not stack