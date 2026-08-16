#
# @lc app=leetcode id=704 lang=python3
#
# [704] Binary Search
#

# @lc code=start
class Solution:
    def search(self, nums, target):
        beg=0
        end=len(nums)-1
        while(beg<=end):
            mid=(beg+end)//2
            if nums[mid]==target:
                return mid
            elif target<nums[mid]:
                end=mid-1
            else: 
                beg=mid+1
        return -1
# @lc code=end

