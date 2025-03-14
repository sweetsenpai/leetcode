import pytest
from Arrays.two_sum import Solution


@pytest.mark.parametrize(
    "nums, target, expected",
    [
        ([2, 7, 11, 15], 9, [0, 1]),
        ([3, 2, 4], 6, [1, 2]),
        ([3, 3], 6, [0, 1]),
        ([1, 2, 3, 4, 5], 10, []),
        ([-3, 4, 3, 90], 0, [0, 2]),
    ],
    ids=[
            "basic_case",
            "no_duplicates",
            "duplicate_numbers",
            "no_solution",
            "negative_numbers",
        ]
)
def test_two_sum(nums, target, expected):
    solution = Solution()
    assert solution.twoSum(nums, target) == expected