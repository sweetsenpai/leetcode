import pytest

from Arrays_HashTabls.TopKElements import Solution


@pytest.mark.parametrize(
    "nums, k, expected",
    [
        ([1, 1, 1, 2, 2, 3], 2, [1, 2]),
        ([1], 1, [1]),
        ([], 1, []),
        ([1, 2, 2, 3], 1, [2]),
    ],
    ids=["basic_case", "single_case", "empty_case", "collector_case"],
)
def test_topkelements(nums, k, expected):
    solution = Solution()
    assert solution.topKFrequent(nums, k) == expected
