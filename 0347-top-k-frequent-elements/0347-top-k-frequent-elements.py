class Solution:
    def topKFrequent(self, nums: list[int], k: int) -> list[int]:
        hasmap = {}
        for num in nums:
            if num not in hasmap:
                hasmap[num] = 0
            hasmap[num] += 1

        hasmap = dict(sorted(hasmap.items(), key=lambda item: item[1], reverse=True))
        
        return list(hasmap.keys())[:k]