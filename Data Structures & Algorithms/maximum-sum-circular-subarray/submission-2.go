func maxSubarraySumCircular(nums []int) int {
	maxSum := nums[0]
	minSum := nums[0]
	currentMin, currentMax := 0, 0
	total := 0

	for _, num := range nums {
		currentMin = min(currentMin+num, num)
		currentMax = max(currentMax+num, num)
		total += num
		maxSum = max(maxSum, currentMax)
		minSum = min(minSum, currentMin)
	}

	if maxSum > 0 {
		return max(maxSum, total - minSum)
	} else {
		return maxSum
	}
}
