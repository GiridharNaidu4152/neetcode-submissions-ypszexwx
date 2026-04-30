class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        minB,maxP=prices[0],0
        for i in prices:
            maxP=max(maxP,i-minB)
            minB=min(i,minB)
        return maxP