class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        res = dict()
        for i in range(len(strs)):
            sorted_str = "".join(sorted(strs[i]))
            if sorted_str not in res:
                res[sorted_str] = [strs[i]]
            else:
                res[sorted_str].append(strs[i])
        return list(res.values())