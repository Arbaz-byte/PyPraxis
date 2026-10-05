class Solution:
    def characterReplacement(self, s: str, k: int) -> int:

        left = 0
        max_len = 0
        max_fre = 0
        count = {}

        for right in range(len(s)):
            count[s[right]] = count.get(s[right], 0) + 1
            max_fre = max(max_fre, count[s[right]])
            
            slide_window = right - left + 1

            if slide_window - max_fre > k:
                count[s[left]] -= 1
                left +=1
            
            max_len = max(max_len, right - left + 1)

        return max_len



 
        