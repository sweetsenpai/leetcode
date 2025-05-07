import pytest

from Stack_Queue.EvaluateReversePolishNotation import Solution


@pytest.mark.parametrize(
    "tokens, expected",
    [
        (["2", "1", "+", "3", "*"], 9),
        (["4", "13", "5", "/", "+"], 6),
        (["10", "6", "9", "3", "+", "-11", "*", "/", "*", "17", "+", "5", "+"], 22),
    ],
    ids=["leetcode_first_example", "leetcode_second_example", "leetcode_third_example"],
)
def test_erpn(tokens, expected):
    solution = Solution()
    assert solution.evalRPN(tokens) == expected
