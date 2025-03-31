class Solution:
    def findDifference(self, nums1: List[int], nums2: List[int]) -> List[List[int]]:
        s1, s2 = set(nums1), set(nums2)
        for num in nums1:
            if num in s2:
                s1.remove(num)
                s2.remove(num)

        return [list(s1), list(s2)]
        