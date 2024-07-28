class Solution(object):
    def largestAltitude(self, gain):
        """
        :type gain: List[int]
        :rtype: int
        """
        A = [0]
        for i in gain:
            A.append(i + A[-1])
        
        return max(A)
        
        