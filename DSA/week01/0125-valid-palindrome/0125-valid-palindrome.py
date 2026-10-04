class Solution:
    def isPalindrome(self, s: str) -> bool:

        t ="".join(char.lower() for char in s if char.isalnum())
        if t == t[::-1]:
            return True
        else:
            return False

   