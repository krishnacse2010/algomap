class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        minLength = float('inf')
        for word in strs:
            if len(word) < minLength:
                minLength = len(word)

        i = 0
        while i < minLength:
            for word in strs:
                if word[i] != strs[0][i]:
                    return strs[0][:i]
            i+=1

        return strs[0][:i]
        

strs = ["flower","flow","flight"]
a=Solution()
print(a.longestCommonPrefix(strs))