#
# @lc app=leetcode id=53 lang=python3
#
# [53] Maximum Subarray
#

# @lc code=start
class Solution:
    def maxSubArray(self, nums):
        maxi=nums[0]
        curr=0
        for i in nums:
            curr+=i
            curr=max(curr, i)
            maxi=max(maxi, curr)
        return maxi
# @lc code=end

