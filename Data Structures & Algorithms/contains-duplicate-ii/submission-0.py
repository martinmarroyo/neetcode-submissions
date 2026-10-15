class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        left = 0
        seen = set()
        for right, val in enumerate(nums):
            if abs(right - left) > k:
                seen.remove(nums[left])
                left += 1
            if val in seen:
                return True
            seen.add(val)
        return False