class Solution:
    def maxSubarraySumCircular(self, nums: List[int]) -> int:
        total = 0
        best_max = best_min = nums[0]
        cur_min = cur_max = 0
        
        for num in nums:
            cur_max = max(cur_max + num, num)
            cur_min = min(cur_min + num, num)
            total += num
            best_max = max(best_max, cur_max)
            best_min = min(best_min, cur_min)
        
        if best_max > 0:
            return max(best_max, total - best_min)
        else:
            return best_max