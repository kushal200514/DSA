class Solution(object):
    def findMaxConsecutiveOnes(self, nums):
        n = len(nums)
        count = 0
        highest = 0

        for i in range (0,n):
            if nums[i] == 1:
                count += 1
                highest = max(highest ,count)
            else:
                count = 0
                
        return highest
        