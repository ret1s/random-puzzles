class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x < 0:
            return False

        orgNumber = x
        reverseNumber = 0
        while x > 0:
            reverseNumber = reverseNumber*10 + x%10 
            x = x//10
        return reverseNumber == orgNumber
