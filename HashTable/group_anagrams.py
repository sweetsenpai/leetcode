"""
# Group Anagrams
## Given an array of strings strs, group the anagrams together. You can return the answer in any order.
url: https://leetcode.com/problems/group-anagrams/description/
"""
from collections import defaultdict
from typing import List


class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:

        result_list = []
        unchecked_list = strs.copy()

        for item in strs:
            anagram_list = []
            anagram_list.append(item)

            if len(unchecked_list) == 0:
                break

            if item not in unchecked_list:
                continue

            item_dict = {letter: item.count(letter) for letter in set(item)}
            unchecked_list.remove(item)

            for sub_item in unchecked_list:
                sub_dict = {letter: sub_item.count(letter) for letter in set(sub_item)}

                if item_dict == sub_dict:
                    anagram_list.append(sub_item)
                    unchecked_list.remove(sub_item)

            result_list.append(anagram_list)
        return result_list

    def bettergroupAnagrams(self, strs: List[str]) -> List[List[str]]:
        groups = defaultdict(list)
        for word in strs:
            counts = [0] * 26  # все буквы английского алфавита
            for char in word:
                counts[ord(char) - ord("a")] +=1
            key = tuple(counts)
            groups[key].append(word)

        return list(groups.values())



























