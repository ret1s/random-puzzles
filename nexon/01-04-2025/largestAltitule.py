class Solution:
    def largestAltitude(self, gain: List[int]) -> int:
        res = height = 0
        for i in gain:
            height += i
            res = max(height, res)
        return res
        