import pytest

from Stack_Queue.Valid_Parentheses import Solution


@pytest.mark.parametrize(
    "s, expected",
    [
        ("()", True),
        ("()[]{}", True),
        ("(]", False),
        ("([])", True),
        ("([[()]])", True),
        ("([[()]]", False),
        ("{[(])}", False),
        ("(]", False),
        ("){", False),
        ("(){}}{", False),
    ],
    ids=[
        "easy_case_one_pair",
        "easy_case_three_pair",
        "easy_case_none_pair",
        "easy_case_two_pair",
        "hard_case_four_pair",
        "hard_case_four_pair_false",
        "chat_gpt_case_false",
        "chat_gpt_second_case",
        "leetcode_only_close",
        "leet_code_error",
    ],
)
def test_valid_parentheses(s, expected):
    solution = Solution()
    assert solution.isValid(s) == expected
