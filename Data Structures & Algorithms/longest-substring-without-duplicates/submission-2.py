class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        left = longest = 0
        window = {}

        for right, char in enumerate(s):
            if char in window:
                left = max(left, window[char] + 1)

            window[char] = right
            longest = max(longest, right - left + 1)
        
        return longest