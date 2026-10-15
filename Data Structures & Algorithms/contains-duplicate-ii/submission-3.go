func containsNearbyDuplicate(nums []int, k int) bool {
    left := 0
    seen := make(map[int]int)
    for right, val := range nums {
        if right - left > k {
            delete(seen, nums[left])
            left++
        }
        
        if _, exists := seen[val]; exists {
            return true
        }

        seen[val] = 1
    }
    return false
}
