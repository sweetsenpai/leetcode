import pytest

from Sorting_Pointers.MostWater import Solution


@pytest.mark.parametrize(
    "height, expected",
    [
        ([1, 8, 6, 2, 5, 4, 8, 3, 7], 49),
        ([1, 1], 1),
        ([4, 3, 2, 1, 4], 16),
        ([1, 2, 1], 2),
        ([1, 3, 2, 5, 25, 24, 5], 24),
    ],
    ids=[
        "basic_case",
        "single_case",
        "collector_case",
        "middle_peak_case",
        "max_in_middle_case",
    ],
)
def test_mostwater(height, expected):
    solution = Solution()
    assert solution.maxArea(height) == expected
