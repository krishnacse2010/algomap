class Solution:
    def summaryRanges(self, nums):
        finalStringList = []

        i = 0
        j = 0

        while i < len(nums):
                sStr = str(nums[i])
                while True:
                    if i+1 < len(nums) and (nums[i] + 1) == nums[i+1]:
                        i+=1
                    else:
                        if sStr!=str(nums[i]):
                            fStr = sStr + "->" + str(nums[i])
                        else:
                            fStr = sStr
                        i+=1
                        break
                finalStringList.append(fStr)
        return finalStringList

   
a=Solution()
print(a.summaryRanges([0,1,2,4,5,7]))