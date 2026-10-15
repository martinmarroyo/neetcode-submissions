func hasDuplicate(nums []int) bool {
    seen := make(map[int]int)

    for _, num := range nums {
        if _, exists := seen[num]; exists {
            return true
        } else {
            seen[num] = 1
        }
    }

    return false
}
