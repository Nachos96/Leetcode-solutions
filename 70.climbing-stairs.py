#
# @lc app=leetcode id=70 lang=python3
#
# [70] Climbing Stairs
#

# @lc code=start
import math
class Solution:
    def climbStairs(self, n):
        sum=0
        one=n
        two=0
        for i in range((n//2)+1):
            ways=(math.factorial(one+two))/((math.factorial(one))*(math.factorial(two)))
            sum+=ways
            two+=1
            one-=2
        return int(sum)
# @lc code=end

