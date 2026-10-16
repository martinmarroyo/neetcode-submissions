func minSubArrayLen(target int, nums []int) int {
	minLen := math.MaxInt
	left, total := 0, 0

	for right, val := range nums {
		total += val
		for total >= target {
			total -= nums[left]
			minLen = min(minLen, right - left + 1)
			left++
		}
	}
	if minLen == math.MaxInt {
		return 0
	} else {
		return minLen
	}
}