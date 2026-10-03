class Solution:
    def topKFrequent(self, nums: list[int], k: int) -> list[int]:
        
        # To store Key and value counts
        hasmap = {}

        for num in nums:
            # if key is not there add
            if num not in hasmap:
                hasmap[num] = 0
            # Increment value of given key
            hasmap[num] += 1

        # sort by values
        hasmap = dict(sorted(hasmap.items(), key=lambda item: item[1], reverse=True))
        
        # Return k most frequent
        return list(hasmap.keys())[:k]