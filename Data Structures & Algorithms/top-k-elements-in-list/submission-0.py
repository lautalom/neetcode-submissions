class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = Counter(nums)
        l = list()
        for key,v in count.items():
            t = tuple((-v,key))
            l.append(t)
        
        heapq.heapify(l)
        res = []
        for i in range(k):
            res.append(heapq.heappop(l)[1])
        del(l)
        return res
