class Solution:
    def maxProfit(self, prices):
        maxProfit = 0
        minprice = float('inf')

        for pr in prices:

            if pr < minprice:
                minprice = pr

            maxProfit = max(maxProfit,pr-minprice)

        return maxProfit







prices = [7,1,5,3,6,4]
a=Solution()
print(a.maxProfit(prices))
print(a.maxProfit([7,6,4,3,1]))