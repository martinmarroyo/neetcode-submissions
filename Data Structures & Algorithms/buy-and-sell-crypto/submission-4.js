class Solution {
    /**
     * @param {number[]} prices
     * @return {number}
     */
    maxProfit(prices) {
		let maxProfit = 0;
		let currentPrice = prices[0];

		for (let opt=0; opt < prices.length; opt++) {
			let currentProfit = prices[opt] - currentPrice;

			if (currentProfit == 0) {
				continue;
			} else if (currentProfit < 0) {
				currentPrice = prices[opt];
			}
			maxProfit = Math.max(maxProfit, currentProfit);
		}
		return maxProfit;
	}
}
