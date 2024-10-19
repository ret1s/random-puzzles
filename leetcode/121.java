class Solution {
    public int maxProfit(int[] prices) {
        int profit = 0;
        int left = 0, right = 1;
        while (right < prices.length) {
            if (prices[left] < prices[right]) {
                profit = Math.max(profit, prices[right] - prices[left]);
            } else {
                left = right;
            }
            right++;
        }
        return profit;
    }
}