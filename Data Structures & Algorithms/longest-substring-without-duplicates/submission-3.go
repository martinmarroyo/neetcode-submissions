func lengthOfLongestSubstring(s string) int {
	left, longest := 0, 0
	window := make(map[rune]int)

	for right, char := range s {
		if idx, exists := window[char]; exists {
			left = max(left, idx+1)
		}
		window[char] = right
		longest = max(longest, right - left + 1)
	}

	return longest
}
