class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        if target not in nums:
            return [-1,-1]
        res = []
        for i, el in enumerate(nums):
            if el == target:
                res.append(i)
        if len(res) == 1:
            res.insert(1, res[0])
            return res
        elif len(res) > 2:
            res = [res[0], res[-1]]
            return res
        return res