from typing import List

class Solution:
    def hasDuplicates(self, nums: List[int]) -> bool:
        return len(set(nums)) < len(nums)