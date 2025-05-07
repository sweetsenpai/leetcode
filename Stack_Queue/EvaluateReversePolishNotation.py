"""
Evaluate Reverse Polish notation
You are given an array of strings tokens that represents an arithmetic expression in a Reverse Polish Notation.

Evaluate the expression. Return an integer that represents the value of the expression.

Note that:

    The valid operators are '+', '-', '*', and '/'.
    Each operand may be an integer or another expression.
    The division between two integers always truncates toward zero.
    There will not be any division by zero.
    The input represents a valid arithmetic expression in a reverse polish notation.
    The answer and all the intermediate calculations can be represented in a 32-bit integer.

https://leetcode.com/problems/evaluate-reverse-polish-notation/description/
"""

import operator
from typing import List


class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        operator_dict = {
            "+": lambda x, y: x + y,
            "-": lambda x, y: y - x,
            "*": lambda x, y: x * y,
            "/": lambda x, y: int(y / x),
        }
        operand_list = []
        for token in tokens:
            if token in operator_dict:
                result = operator_dict[token](operand_list.pop(), operand_list.pop())
                operand_list.append(result)
            else:
                operand_list.append(int(token))
        return operand_list[0]
