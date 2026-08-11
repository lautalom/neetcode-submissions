class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        res = defaultdict(list)

        for s in strs:
            count = [[0, 0] for _ in range(26)]

            for c in s:
                if 'a' <= c <= 'z':
                    count[ord(c) - ord('a')][0] += 1
                else:
                    count[ord(c) - ord('A')][1] += 1

            key = tuple(tuple(pair) for pair in count)
            res[key].append(s)

        return list(res.values())
