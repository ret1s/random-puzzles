from typing import List
from collections import defaultdict

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        res = defaultdict(list)
        
        for s in strs:
            count = [0] * 26
            for c in s:
                count[ord(c) - ord('a')] += 1
            res[tuple(count)].append(s)
            # Alternatively, you can use sorted strings as keys:
            # sorted_s = ''.join(sorted(s))
            # res[sorted_s].append(s)
        
        return list(res.values())