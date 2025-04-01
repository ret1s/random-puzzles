class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        d = defaultdict(int)
        for i in arr:
            d[i] += 1
        return len(set(d.values())) == len(d)