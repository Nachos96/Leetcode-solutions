#
# @lc app=leetcode id=11 lang=python3
#
# [11] Container With Most Water
#

# @lc code=start
class Solution:
    def maxArea(self, height):
        max_area=0
        left=0
        right=len(height)-1
        while left<right:
            area=min(height[left], height[right])*(right-left)
            max_area=max(max_area, area)
            if(height[left]>height[right]):
                right-=1
            else:
                left+=1
        return max_area
# @lc code=end

