class Solution:
    def groupAnagrams(self, strs: list[str]) -> list[list[str]]:

        # Creates a dictionary where every missing key automatically gets an empty list as its value.
        group = defaultdict(list)

        for i in range(len(strs)):
            # key that allow duplicate
            key = "".join(sorted(strs[i]))
            # if find that same signature , add value
            group[key].append(strs[i])

        return list(group.values())







                    
