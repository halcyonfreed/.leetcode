#
# @lc app=leetcode.cn id=59 lang=python3
#
# [59] 螺旋矩阵 II
#

# @lc code=start
class Solution:
    def generateMatrix(self, n: int) -> List[List[int]]:
        #[] count=1
        # loop,mid=n//2,n//2
        # startx,starty=0,0
        # nums=[[0]*n for _ in range(n)]
        
        # for offset in range(1,loop+1):
        #     for i in range(starty,n-offset):
        #         nums[startx][i]=count
        #         count+=1
        #     for i in range(startx,n-offset):
        #         nums[i][n-offset]=count
        #         count+=1
        #     for i in range(n-offset,starty,-1):
        #         nums[n-offset][i]=count
        #         count+=1
        #     for i in range(n-offset,startx,-1):
        #         nums[i][starty]=count
        #         count+=1
        #     startx+=1
        #     starty+=1

        # if n%2!=0:
        #     nums[mid][mid]=count
        # return nums

        # count=1
        # loop,mid=n//2,n//2
        # startx,starty=0,0
        # nums=[[0]*n for _ in range(n)]

        # for offset in range(1,loop+1):
        #     for i in range(starty,n-offset):
        #         nums[startx][i]=count
        #         count+=1
        #     for i in range(startx,n-offset):
        #         nums[i][n-offset]=count
        #         count+=1
        #     for i in range(n-offset,starty,-1):
        #         nums[n-offset][i]=count
        #         count+=1
        #     for i in range(n-offset,startx,-1):
        #         nums[i][starty]=count
        #         count+=1
        #     startx+=1
        #     starty+=1
        # if n%2!=0:
        #     nums[mid][mid]=count
        # return nums
        count=1
        loop,mid=n//2,n//2

        startx,starty=0,0
        nums=[[0]*n for _ in range(n)]
        for offset in range(1,loop+1):
            for i in range(starty,n-offset):
                nums[startx][i]=count
                count+=1
            for i in range(startx,n-offset):
                nums[i][n-offset]=count
                count+=1
            for i in range(n-offset,starty,-1):
                nums[n-offset][i]=count
                count+=1
            for i in range(n-offset,startx,-1):
                nums[i][starty]=count
                count+=1
            startx+=1
            starty+=1
        if n%2!=0:
            # 奇数
            nums[mid][mid]=count
        return nums

# @lc code=end

