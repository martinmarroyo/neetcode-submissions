class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        """
        1. Loop through each character and compare it to the next
        2. If the characters are the same, increase the maximum string size
        3. If characters are different, swap and deduct from k
        4. Once k reaches 0, the window is depleted. Record the length of the substring, then update the window by shifting the left pointer to where the right pointer is. If the length of the substring is larger than the previous one, then it replaces the max substring size; reset k
        """
        left, max_substring = 0, 0
        count = {}
        max_freq = 0

        for right in range(len(s)):
            count[s[right]] = count.get(s[right], 0) + 1
            max_freq = max(max_freq, count[s[right]])

            # If the number of characters to replace exceeds k, shrink window from left
            while (right - left + 1) - max_freq > k:
                count[s[left]] -= 1
                left += 1

            max_substring = max(max_substring, right - left + 1)

        return max_substring
