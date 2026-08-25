class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        ans = ""
        start = strs[0]
        if len(strs)==1:
            return start

        for i,c in enumerate(start):
            for s in strs[1:]:
                if i<len(s):
                    if c!=s[i]:
                        return ans
                else:
                    return ans
            ans+=c
        return ans
        
