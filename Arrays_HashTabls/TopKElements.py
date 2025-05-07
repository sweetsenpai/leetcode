"""
### Top K Frequent Elements
## Given an integer array nums and an integer k, return the k most frequent elements. You may return the answer in any order.
https://leetcode.com/problems/top-k-frequent-elements/
"""

from collections import defaultdict
from typing import List


class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        result = []
        counts = defaultdict(int)
        freq = [[] for _ in range(len(nums) + 1)]
        for num in nums:
            counts[num] += 1
        for key, value in counts.items():
            freq[value].append(key)
        for i in range(len(freq) - 1, 0, -1):
            for num in freq[i]:
                result.append(num)
                if len(result) == k:
                    return result
        return result
