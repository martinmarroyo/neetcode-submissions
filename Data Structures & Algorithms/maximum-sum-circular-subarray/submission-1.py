class Solution:
    def maxSubarraySumCircular(self, nums: List[int]) -> int:
        total = 0
        max_sum = min_sum = nums[0]
        cur_min = cur_max = 0
        
        for num in nums:
            cur_max = max(cur_max + num, num)
            cur_min = min(cur_min + num, num)
            total += num
            max_sum = max(max_sum, cur_max)
            min_sum = min(min_sum, cur_min)
        
        if max_sum > 0:
            return max(max_sum, total - min_sum)
        else:
            return max_sum