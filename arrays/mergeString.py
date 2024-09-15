class Solution:
    def mergeAlternately(self, word1, word2):
        if len(word2) > len(word1):
            n = len(word1)
        else:
            n = len(word2)
        i = 0
        finalString = ""
        while i < n:
            temString = word1[i] + word2[i]
            finalString += temString
            i+=1        
        finalString = finalString+word1[n:]+word2[n:]

word1 = "ab"
word2 = "pqrs"
a=Solution()
a.mergeAlternately(word1,word2)
        