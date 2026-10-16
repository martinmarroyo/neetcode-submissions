func numOfSubarrays(arr []int, k int, threshold int) int {
	left := 0
	subArrays := 0
	runningSum := 0

	for right, val := range arr {
		runningSum += val
		if right >= k-1 {
			if runningSum >= threshold * k {
				subArrays++
			}
			runningSum -= arr[left]
			left++
		}
		
	}

	return subArrays
}
