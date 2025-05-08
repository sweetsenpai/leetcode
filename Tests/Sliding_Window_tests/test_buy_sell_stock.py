import pytest

from Sliding_Window.BuySellStock import Solution


@pytest.mark.parametrize(
    "prices, expected",
    [
        ([7,1,5,3,6,4], 5),
        ([7,6,4,3,1], 0),
        ([1, 2, 3, 4, 7], 6)
    ],
    ids=[
        "regular_case",
        "zero_case",
        "first_day_case"
    ]
)
def test_buy_sell_stock(prices, expected):
    solution = Solution()
    assert solution.maxProfit(prices) == expected
