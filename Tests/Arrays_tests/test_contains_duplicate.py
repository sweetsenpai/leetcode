import pytest

from Arrays.contains_duplicate import Solution


@pytest.mark.parametrize(
    "nums, expected",
    [
        ([1, 2, 3, 1], True),
        ([1, 2, 3, 4], False),
        ([1, 1, 1, 3, 3, 4, 3, 2, 4, 2], True),
    ],
    ids=[
        "basic_case",
        "no_duplicates",
        "many_duplicates"
    ]
)
def test_contins_duplicate(nums, expected):
    solution = Solution()
    assert solution.containsDuplicate(nums) == expected