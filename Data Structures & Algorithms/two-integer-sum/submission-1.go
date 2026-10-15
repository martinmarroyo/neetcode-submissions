func twoSum(nums []int, target int) []int {
    seen := make(map[int]int)
	for idx, num := range nums {
		if value, exists := seen[target - num]; exists {
			return []int{value, idx}
		} else {
			seen[num] = idx
		}
	}
	return []int{-1, 0}
}
