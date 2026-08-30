class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        
        start, n = 0, len(nums)

        while start < n:
            if nums[start]==val:
                n-=1
                nums[start] = nums[n]
            else:
                start+=1
        
        return n