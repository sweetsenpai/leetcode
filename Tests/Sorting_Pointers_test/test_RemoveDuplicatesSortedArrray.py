import pytest
from Sorting_Pointers.RemoveDuplicatesSortedArrray import Solution


@pytest.mark.parametrize(
    "nums, expected",
    [
        ([1, 1, 2], 2),
        ([0, 0, 1, 1, 1, 2, 2, 3, 3, 4], 5),
        ([1, 2, 3, 4, 5], 5),
        ([1, 1, 1, 1, 1], 1),
        ([1, 2, 2, 3, 4, 4, 5, 5, 6], 6)
    ],
    ids=[
        "leetcode_first_test",
        "leetcode_second_test",
        "unique_elements",
        "all_same_elements",
        "mixed_case"
    ]
)
def test_solution(nums, expected):
    solution = Solution()
    assert solution.removeDuplicates(nums) == expected