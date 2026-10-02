class Solution:
    def isAnagram(self, s: str, t: str) -> bool:

        # If length of strings are different , they are not Anagram
        if len(s) != len(t):
            return False
        
        # If we make a set of char and check how many time each char occure if same --> Anagram
        for i in set(s):
            if s.count(i) != t.count(i):
                return False
        return True
     
    


        
        
    