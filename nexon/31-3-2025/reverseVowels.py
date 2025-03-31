class Solution:
    def reverseVowels(self, s: str) -> str:
        left, right = 0, len(s) - 1
        vowels = {'a', 'e', 'o', 'u', 'i', 'A', 'E', 'O', 'U', 'I'}
        s_list = list(s)
        while left < right:
            while s_list[left] not in vowels and left < right:
                left += 1
            while s_list[right] not in vowels and left < right:
                right -= 1
            if s_list[left] in vowels and s_list[right] in vowels:
                s_list[left], s_list[right] = s_list[right], s_list[left]
                left += 1
                right -= 1
        return "".join(s_list)
