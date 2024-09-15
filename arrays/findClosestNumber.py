class Solution:
    def findClosestNumber(self, nums):
        closestNumber = float('inf')

        for num in nums:            
            if abs(num) < abs(closestNumber):
                closestNumber = num
                

        if abs(closestNumber) in nums:
            return abs(closestNumber)
        return closestNumber




a=Solution()
print(a.findClosestNumber([-100000,-100000]))
print(a.findClosestNumber([-4,-2,1,4,8]))
        