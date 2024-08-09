class Solution(object):
    def pivotIndex(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """        
        rnums = nums[::-1]
        A = [0]
        B = [0]
        for i in range(len(nums)):
            A.append(nums[i] + A[-1])
            B.append(rnums[i] + B[-1])
        B = B[::-1]
        for i in range(len(A) - 1):
            if A[i] == B[i + 1]:
                return i

        return -1
