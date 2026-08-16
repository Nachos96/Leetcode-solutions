#
# @lc app=leetcode id=238 lang=python3
#
# [238] Product of Array Except Self
#

# @lc code=start
class Solution:
    def productExceptSelf(self, nums):
        answer=[1]*len(nums)
        left=1
        right=1
        for i in range(len(nums)):
            answer[i]=left
            left*=nums[i]
        for i in reversed(range(len(nums))):
            answer[i]*=right
            right*=nums[i]
        return answer

# @lc code=end

