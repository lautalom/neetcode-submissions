class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        a = Counter(nums)
        for _,val in a.items():
            if val > 1:
                return True
        return False