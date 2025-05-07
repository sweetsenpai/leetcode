import pytest

from Sorting_Pointers.MoveZeroes import Solution


@pytest.mark.parametrize(
    "nums, expected",
    [
        ([0, 1, 0, 3, 12], [1, 3, 12, 0, 0]),
        ([0], [0]),
        ([2, 1], [2, 1]),
        ([0, 0, 0, 1], [1, 0, 0, 0]),
        ([1, 0, 0, 0], [1, 0, 0, 0]),
        ([0, 0, 1, 0, 0], [1, 0, 0, 0, 0]),
        ([1, 2, 0, 3, 4], [1, 2, 3, 4, 0]),
    ],
    ids=[
        "leetcode_regular_test",
        "leetcode_onlyzeroes_test",
        "leetcode_none_zeroes",
        "multiple_leading_zeros",
        "single_nonzero_with_trailing_zeros",
        "one_number_in_middle",
        "one_zeroe_in_middle",
    ],
)
def test_MoveZeroes(nums, expected):
    solution = Solution()
    solution.moveZeroes(nums)
    assert nums == expected
