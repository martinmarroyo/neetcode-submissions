func maxSubarraySumCircular(nums []int) int {
	currentMin, bestMin := 0, nums[0]
    currentMax, bestMax := 0, nums[0]
	total := 0

	for _, num := range nums {
		currentMin = min(currentMin+num, num)
		currentMax = max(currentMax+num, num)
		total += num
		bestMax = max(bestMax, currentMax)
		bestMin = min(bestMin, currentMin)
	}

	if bestMax > 0 {
		return max(bestMax, total - bestMin)
	} else {
		return bestMax
	}
}
