"""
Given an integer array nums, return true if any value appears at least twice in the array, and return false if every element is distinct.
"""
from typing import List


class Solution2:
    def containsDuplicate(self, nums: List[int]) -> bool:
        return len(set(nums)) != len(nums)
