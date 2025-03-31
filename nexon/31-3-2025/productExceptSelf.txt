class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        res = [1] * len(nums)
        l, r = 1, 1
        for i in range(len(nums)):
            res[i] *= l
            l *= nums[i]
        for i in range(len(nums) - 1, -1, -1):
            res[i] *= r
            r *= nums[i]
        return res
