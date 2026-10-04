class Solution:
    def isPalindrome(self, s: str) -> bool:
        if (len(s) <= 1):
            return True
            
        s ="".join(char.lower() for char in s if char.isalnum())
        left, right  = 0 , len(s)-1

        while left <= right and s[left] == s[right]:
            left +=1
            right -= 1
        if left<right :
            return False
        return True