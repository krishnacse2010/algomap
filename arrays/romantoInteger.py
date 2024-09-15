class Solution:
    def romanToInt(self, s):
        hMap = {'I':1,'V':5,'X':10,'L':50,'C':100,'D':500,'M':1000}
        i = 0
        finalInt =0         
        while i < len(s):
            if i+1 < len(s) and hMap[s[i+1]] > hMap[s[i]]:
                finalInt += hMap[s[i+1]] - hMap[s[i]] 
                i=i+2
            else:
                finalInt += hMap[s[i]]
                i+=1
        return finalInt


a=Solution()
print(a.romanToInt('MCMXCIV'))