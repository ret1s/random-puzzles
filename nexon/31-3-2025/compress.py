class Solution:
    def compress(self, chars: List[str]) -> int:
        n = len(chars)
        idx = 0
        i = 0
        while i < n:
            ch = chars[i]
            cnt = 0
            while i < n and chars[i] == ch:
                cnt += 1
                i += 1
            if cnt == 1:
                chars[idx] = ch
                idx += 1
            else:
                chars[idx] = ch
                idx += 1
                for digit in str(cnt):
                    chars[idx] = digit
                    idx += 1
        chars[:] = chars[:idx]
        return idx
