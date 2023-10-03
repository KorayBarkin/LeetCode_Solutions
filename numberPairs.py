from collections import Counter

class Solution:
    def numIdenticalPairs(self, nums: List[int]) -> int:
        total = Counter(nums)
        res = 0
        for i in range(max(total)+1):
            res += total[i] * (total[i] - 1) / 2
        return int(res)