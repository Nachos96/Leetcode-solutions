#
# @lc app=leetcode id=153 lang=python3
#
# [153] Find Minimum in Rotated Sorted Array
#

# @lc code=start
class Solution(object):
    def findMin(self, nums):
        n=min(nums)
        for i in range(len(nums)):
            if nums[i]==n:
                rotations=i
        k=len(nums)-rotations
        while(nums[0]!=n):
            k=k%len(nums)
            nums[:]=nums[-k:]+nums[:-k]
            return nums[0]
        return nums[0]
# @lc code=end

