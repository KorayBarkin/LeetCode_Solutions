class Solution(object):
    def isMonotonic(self, nums):
        n = len(nums)-1
        countInc = 0
        countdec = 0
        for i in range(n):
            if nums[i] < nums[i+1]:
                countInc += 1
            elif nums[i] > nums[i+1]:
                countdec += 1
            else:
                countdec += 1
                countInc += 1
        print(countdec, countInc, n)
        if countInc == n or countdec == n:
            return True
        else:
            return False