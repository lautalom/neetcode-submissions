class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        cs,ct = Counter(s), Counter(t)
        return ct==cs