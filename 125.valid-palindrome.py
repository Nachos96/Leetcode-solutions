#
# @lc app=leetcode id=125 lang=python3
#
# [125] Valid Palindrome
#

# @lc code=start
class Solution:
    def isPalindrome(self, s):
        s1=[]
        for c in s:
            if c.isalnum():
                s1.append(c.lower())
        left=0
        for right in reversed(range(len(s1))):
            if s1[left]==s1[right]:
                left+=1
            else:
                return False
        return True
# @lc code=end

