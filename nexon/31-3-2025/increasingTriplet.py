class Solution:
    def increasingTriplet(self, nums: List[int]) -> bool:
        m1, m2 = float('inf'), float('inf')
        for num in nums:
            if num <= m1:
                m1 = num
            elif num <= m2:
                m2 = num
            else:
                return True
        return False
        