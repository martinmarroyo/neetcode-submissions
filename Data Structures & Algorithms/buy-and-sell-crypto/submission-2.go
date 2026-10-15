func maxProfit(prices []int) int {
	maxProfit := 0
	currentPrice := prices[0]

	for _, opt := range prices {
		currentProfit := opt - currentPrice

		if currentProfit == 0 {
			continue
		} else if currentProfit < 0 {
			currentPrice = opt
		}

		maxProfit = max(currentProfit, maxProfit)
	}

	return maxProfit
}
