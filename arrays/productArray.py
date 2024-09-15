class Solution:
    def productExceptSelf(self, nums):
        L_array = [1] * len(nums)
        R_array = [1] * len(nums)
        l_mult = 1
        r_mult = 1
        i = 0
        while i < len(nums):
            L_array[i] = l_mult
            l_mult = l_mult* nums[i]            
            i+=1
        
        i = len(nums) - 1
        while i > -1:
            R_array[i] = r_mult
            r_mult = r_mult* nums[i]            
            i-=1
        finalProduct = [l*r for l,r in zip(L_array,R_array)]
        return finalProduct   
 

a=Solution()
print(a.productExceptSelf([1,2,3,4]))