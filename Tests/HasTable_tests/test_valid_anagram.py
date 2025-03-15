import pytest
from HashTable.valid_anagram import Solution


@pytest.mark.parametrize(
    "s, t, expected",
    [
        ("anagram", "nagaram", True),
        ("aacc", "ccac", False),
        ("rat", "car", False),
    ],
    ids=[
        "true_case",
        "hard_case",
        "false_case"
    ]
)
def test_valid_anagram(s, t, expected):
    solution = Solution()
    assert solution.isAnagram(s, t) == expected