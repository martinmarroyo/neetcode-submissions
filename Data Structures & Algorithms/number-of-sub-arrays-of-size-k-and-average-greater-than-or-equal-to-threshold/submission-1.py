class Solution:
    def numOfSubarrays(self, arr: List[int], k: int, threshold: int) -> int:
        left = 0
        max_threshold = k * threshold
        running_sum = 0
        subarrays = 0

        for right, val in enumerate(arr):
            running_sum += val 
            if right >= k-1:
                if running_sum >= max_threshold:
                    subarrays += 1
                running_sum -= arr[left]
                left += 1
        return subarrays