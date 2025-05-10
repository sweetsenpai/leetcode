import pytest

from Sliding_Window.LongestSubstring import Solution

@pytest.mark.parametrize(
    "s, expected",
    [
        ("abcabcbb", 3),
        ("bbbbb", 1),
        ("pwwkew", 3)
    ],
    ids=[
        "first_leetcode_case",
        "second_leetcode_case",
        "therd_leetcode_case"
    ]
)
def test_longest_substring(s, expected):
    solution = Solution()
    assert solution.lengthOfLongestSubstring(s) == expected