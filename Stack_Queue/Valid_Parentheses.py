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
    @staticmethod
    def isValid_my(s: str) -> bool:
        breckit_dict = defaultdict(lambda: None)
        breckit_dict["("] = ")"
        breckit_dict["["] = "]"
        breckit_dict["{"] = "}"
        lenth = len(s)
        if lenth % 2 !=0:
            return False
        s_list = list(s)
        if not breckit_dict[s_list[0]]:
            return False
        for index, letter in enumerate(s_list):
            if breckit_dict[letter]:
                opposite_brecket = breckit_dict[letter]
                if s_list[index+1]!= opposite_brecket and s_list[len(s) - 1 - index]!=opposite_brecket:
                    return False

        return True

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