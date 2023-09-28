class Solution(object):
    def sortArrayByParity(self, nums):
        odds = []
        evens = []
        res = []
        for num in nums:
            if num % 2 == 0:
                evens.append(num)
            else:
                odds.append(num)
        res = evens + odds
        return res