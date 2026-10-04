class Solution:
    def isPalindrome(self, s: str) -> bool:

        t ="".join(char.lower() for char in s if char.isalnum())
        s = t[::-1]
        if t == s:
            return True
        else:
            return False

   