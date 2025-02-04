class Solution:
    def maxAscendingSum(self, nums: List[int]) -> int:
        res = nums[0] 
        curr_max = nums[0] 
        for i in range(1, len(nums)): 
            if (nums[i-1] < nums[i]):
                curr_max += nums[i]
            else: 
                curr_max = nums[i] 
            res = max(res, curr_max)
        return res
            