class Solution:
    def sortColors(self, nums):

        c0 = nums.count(0)
        c1 = nums.count(1)
        c2 = nums.count(2)

        n = len(nums)

        for i in range(n):
            if c0 > 0:
                nums[i] = 0
                c0 -= 1

            elif c1 > 0:
                nums[i] = 1
                c1 -= 1

            else:
                nums[i] = 2
                c2 -= 1
                c1-=1
            

    