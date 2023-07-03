class Solution(object):
    def containsDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        numsSet = set(nums)
        uniqList = list(numsSet)

        if len(nums) == len(uniqList):
            return False
        else:
            return True