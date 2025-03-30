"""
Move Zeroes

Given an integer array nums, move all 0's to the end of it while maintaining the relative order of the non-zero elements.

Note that you must do this in-place without making a copy of the array.

https://leetcode.com/problems/move-zeroes/
"""
from typing import List


class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        slow = 0
        for fast in range(len(nums)):
            if nums[fast] != 0:
                if nums[slow] == 0:
                    nums[slow] = nums[fast]
                    nums[fast] = 0
                slow += 1
        return


test = [2,1]
x = Solution()
x.moveZeroes(test)
print(test)