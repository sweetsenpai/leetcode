"""
Merge Sorted Array

You are given two integer arrays nums1 and nums2, sorted in non-decreasing order, and two integers m and n, representing the number of elements in nums1 and nums2 respectively.

Merge nums1 and nums2 into a single array sorted in non-decreasing order.

The final sorted array should not be returned by the function, but instead be stored inside the array nums1. To accommodate this, nums1 has a length of m + n, where the first m elements denote the elements that should be merged, and the last n elements are set to 0 and should be ignored. nums2 has a length of n.

https://leetcode.com/problems/merge-sorted-array/description/
"""
from typing import List


class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        i, j, k = m - 1, n - 1, m + n - 1  # Указатели

        while i >= 0 and j >= 0:  # Пока есть элементы в обоих массивах
            if nums1[i] > nums2[j]:
                nums1[k] = nums1[i]
                i -= 1
            else:
                nums1[k] = nums2[j]
                j -= 1
            k -= 1  # Двигаем указатель на следующую позицию

        # Если остались элементы в nums2, добавляем их (nums1 уже на месте)
        while j >= 0:
            nums1[k] = nums2[j]
            j -= 1
            k -= 1
