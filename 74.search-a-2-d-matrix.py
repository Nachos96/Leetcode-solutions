#
# @lc app=leetcode id=74 lang=python3
#
# [74] Search a 2D Matrix
#

# @lc code=start
class Solution:
    def searchMatrix(self, matrix, target):
        rows=len(matrix)-1
        cols=len(matrix[0])-1
        beg=0
        end=rows
        while(beg<=end):
            mid=(beg+end)//2
            if target>=matrix[mid][0] and target<=matrix[mid][cols]:
                beg1=0
                end1=cols
                while(beg1<=end1):
                    mid1=(beg1+end1)//2
                    if target==matrix[mid][mid1]:
                        return True
                    elif target<matrix[mid][mid1]:
                        end1=mid1-1
                    else:
                        beg1=mid1+1
                return False
            elif target>matrix[mid][cols]:
                beg=mid+1
            else:
                end=mid-1
        return False
# @lc code=end

