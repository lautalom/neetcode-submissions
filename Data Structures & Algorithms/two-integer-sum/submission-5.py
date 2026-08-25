class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        d = defaultdict(list)
        for k, v in enumerate(nums):
            d[v].append(k)
        for i,v in enumerate(nums):
            complement = target - v
            if complement in d:
                if complement==v:
                    if len(d[v]) > 1:
                        return [d[v][0], d[v][1]]
                    else:
                        continue
                else:
                    return [i, d[complement][0]]