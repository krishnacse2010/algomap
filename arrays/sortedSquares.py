class Solution:
    def sortedSquares(self, nums):
        resultArray = []
        i = 0
        j = len(nums) - 1

        while i <= j :
            if abs(nums[i]) > abs(nums[j]):
                resultArray.append(nums[i])
                i+=1
            else:
                resultArray.append(nums[j])
                j-=1

        return [val**2 for val in resultArray[::-1]]


a=Solution()
print(a.sortedSquares([-4,-1,0,3,10]))