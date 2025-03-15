import pytest
from HashTable.group_anagrams import Solution


@pytest.mark.parametrize(
    "strs, expected",
    [
        (["eat", "tea", "tan", "ate", "nat", "bat"],
         [['eat', 'tea', 'ate'], ['tan', 'nat'], ['bat']]),
        ([""], [[""]]),
        (["a"], [["a"]])
    ],
    ids=[
        "real_case",
        "empty_case",
        "one_letter_case"
    ]
)
def test_goup_anagrams(strs, expected):
    solution = Solution()
    assert solution.groupAnagrams(strs) == expected


@pytest.mark.parametrize(
    "strs, expected",
    [
        (["eat", "tea", "tan", "ate", "nat", "bat"],
         [['eat', 'tea', 'ate'], ['tan', 'nat'], ['bat']]),
        ([""], [[""]]),
        (["a"], [["a"]])
    ],
    ids=[
        "real_case",
        "empty_case",
        "one_letter_case"
    ]
)
def test_better_goup_anagrams(strs, expected):
    solution = Solution()
    assert solution.bettergroupAnagrams(strs) == expected