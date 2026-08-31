class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        candidate, count = nums[0], 1

        for i in range(len(nums[1:])):
            if count == 0:
                candidate = nums[i]
            
            if candidate!=nums[i]:
                count-=1
            else:
                count+=1
        
        return candidate

