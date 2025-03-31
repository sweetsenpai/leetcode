import pytest
from Sorting_Pointers.ValidPalindrome import Solution

@pytest.mark.parametrize(
    "s, expected",
    [
        ("A man, a plan, a canal: Panama", True),
        ("race a car", False),
        (" ", True),
        (".,", True),
        ("0P", False)
    ],
    ids=[
        "leetcode_regular_test",
        "leetcode_regular_false_test",
        "leetcode_emppty_test",
        "only_punctuation",
        "digit_letter_mismatch"
    ]
)
def test_ValidPalindrome(s, expected):
    solution = Solution()
    assert solution.isPalindrome(s) == expected