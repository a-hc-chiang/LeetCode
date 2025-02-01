class Solution:
    def isArraySpecial(self, nums: List[int]) -> bool:
        if len(nums) < 2: 
            return True 
        is_even = True if nums[0] % 2 == 0 else False 
        for i in range(len(nums)): 
            if i == 0: 
                continue 
            if nums[i]%2 == 0 and is_even: 
                return False 
            elif nums[i]%2 == 1 and not is_even: 
                return False
            else: 
                is_even = True if nums[i] % 2 == 0 else False 
        return True     
