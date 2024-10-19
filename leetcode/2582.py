class Solution(object):
    def passThePillow(self, n, time):
        """
        :type n: int
        :type time: int
        :rtype: int
        """
        a = time / (n - 1)
        b = time % (n - 1)
        position = -1
        if a % 2 == 0:
            position = 1 + b
        else:
            position = n - b
        return position
        