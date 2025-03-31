class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        curSum = maxSum = sum(nums[:k])
        for i in range(k, len(nums)):
            curSum += nums[i] - nums[i - k]
            maxSum = max(curSum, maxSum)
        return maxSum/k