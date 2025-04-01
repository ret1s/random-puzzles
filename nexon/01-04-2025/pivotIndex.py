class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        total = sum(nums)
        pre = 0
        for i, num in enumerate(nums):
            pre += num
            r = total - pre
            if r == pre - num:
                return i
        return -1
        