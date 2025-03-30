from typing import List

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # Time complexity: O(n log n) due to sorting
        freq = {}
        for num in nums:
            freq[num] = 1 + freq.get(num, 0)
        
        sorted_freq = dict(sorted(freq.items(), key=lambda item: item[1]))

        return list(sorted_freq.keys())[-k:]