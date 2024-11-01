class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        f, s = 0, 1
        profit = 0

        while s <= len(prices) - 1:
            temp_profit = prices[s] - prices[f]
            if temp_profit > profit:
                profit = temp_profit

            if prices[s] < prices[f]:
                f = s
                s+=1
            elif prices[f] < prices[s] or prices[f] == prices[s]:
                s+=1
            else:
                s+=1
                f+=1

        return profit

# roadblocks: handling increment for second pointer. such as handling cases for the second pointer being greater than, less than, or equal to the first
