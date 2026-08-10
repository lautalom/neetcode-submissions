class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        rem = dict()
        for k,n in enumerate(nums):
            r = target - n
            if r in rem:
                return [min(k,rem[r]),max(k,rem[r])]
            else:
                rem[n] = k
        