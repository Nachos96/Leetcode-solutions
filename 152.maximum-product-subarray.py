#
# @lc app=leetcode id=152 lang=python3
#
# [152] Maximum Product Subarray
#

# @lc code=start
class Solution(object):
    def maxProduct(self, nums):
        maxi=nums[0]
        curr=1
        negcurr=1
        for i in nums:
            negcurr*=i
            curr*=i
            curr1=max(curr, i, negcurr)
            negcurr=min(curr, i, negcurr)
            maxi=max(maxi, curr1)
            curr=curr1
        return maxi 
        
# @lc code=end

