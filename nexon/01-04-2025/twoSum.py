class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        m = {}
        for i in range(len(numbers)):
            diff = target - numbers[i]
            if diff in m:
                return [m[diff], i + 1]
            else:
                m[numbers[i]] = i + 1
        return []
        