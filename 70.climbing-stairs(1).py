#
# @lc app=leetcode id=70 lang=python3
#
# [70] Climbing Stairs
#

# @lc code=start
import math
class Solution:
    def climbStairs(self, n):
        stairs=[1, 1]
        sum=1
        for i in range(n-1):
            sum+=stairs[len(stairs)-2]
            stairs.append(sum)
        return sum
# @lc code=end

