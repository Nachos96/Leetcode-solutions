#
# @lc app=leetcode id=167 lang=python3
#
# [167] Two Sum II - Input Array Is Sorted
#

# @lc code=start
class Solution:
    def twoSum(self, numbers, target):
        left=0
        right=1
        for right in range(len(numbers)):
            complement=target-numbers[left]
            beg=left+1
            end=len(numbers)-1
            while(beg<=end):
                mid=(beg+end)//2
                if numbers[mid]==complement:
                    return [left+1, mid+1]
                elif numbers[mid]>complement:
                    end=mid-1
                else:
                    beg=mid+1
            left+=1
            


            
# @lc code=end

