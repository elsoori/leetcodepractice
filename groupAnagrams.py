class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        dict = {}
        for s in strs:
            j = "".join(sorted(s))
            if j not in dict:
                dict[j] = [s]
            else:
                dict[j].append(s)
        return dict.values()
            