class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        ltr, rtl = [1] * (len(nums)+1), [1] * (len(nums)+1)

        for i in range(len(nums)):
            ltr[i+1] = ltr[i] * nums[i]
            rtl[-2-i]=rtl[-1-i] * nums[-1-i]

        res=[]
        for i in range(len(nums)):
            res.append(ltr[i]*rtl[i+1])
        
        return res
        