import pytest
from Sorting_Pointers.MergeSortedArray import Solution


@pytest.mark.parametrize(
    "nums1, m, nums2, n, expected",
    [
        ([1, 2, 3, 0, 0, 0], 3, [2, 5, 6], 3, [1, 2, 2, 3, 5, 6]),
        ([1], 1, [], 0, [1]),
        ([0], 0, [1], 1, [1]),
        ([4, 5, 6, 0, 0, 0], 3, [1, 2, 3], 3, [1, 2, 3, 4, 5, 6]),
        ([1, 2, 3, 0, 0, 0], 3, [7, 8, 9], 3, [1, 2, 3, 7, 8, 9])

    ],

    ids=[
        "leetcose_first_test",
        "leetcode_empty_nums2",
        "leetcode_empty_nums1",
        "less_min_num2",
        "bigger_nums2"
    ]
)
def test_merge_sorted_arrays(nums1, m, nums2, n, expected):
    solution = Solution()
    solution.merge(nums1, m, nums2, n)
    assert nums1 ==expected
