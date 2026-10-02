class Solution:
    def isAnagram(self, s: str, t: str) -> bool:

        # If length of strings are different , they are not Anagram
        if len(s) != len(t):
            return False
        
        # As all the chacters are in lower case from a to z(26 char)
        count = [0] *26

        for i in range(len(s)):
            # Increment for s, decrement for t
            count[ord(s[i]) - ord("a")] += 1
            count[ord(t[i]) - ord("a")] -=1
        
        # If they are Anagram , every valu in count must be zero
        for val in count:
            if val != 0:
                return False
        return True

     
    


        
        
    