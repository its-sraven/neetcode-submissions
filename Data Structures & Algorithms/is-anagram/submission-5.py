class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        s_cnt = dict()
        t_cnt = dict()

        for ch in s:
            s_cnt[ch] = s_cnt.get(ch,0) + 1

        for ltr in t:
            t_cnt[ltr] = t_cnt.get(ltr,0) + 1
        
        print(s_cnt)
        print(t_cnt)

        return s_cnt == t_cnt