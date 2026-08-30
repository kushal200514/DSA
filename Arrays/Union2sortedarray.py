class Solution:
    def unionArray(self, nums1, nums2):
        union=[]
        union = list(set(nums1) | set(nums2))
        return union