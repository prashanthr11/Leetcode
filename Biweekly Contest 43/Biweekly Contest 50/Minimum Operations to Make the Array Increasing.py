class Solution:
    def minOperations(self, nums: List[int]) -> int:
        ret = 0
        for i in range(1, len(nums)):
            if nums[i] <= nums[i - 1]:
                ret += abs(nums[i - 1] - nums[i]) + 1
                nums[i] = nums[i - 1] + 1
        
        return ret
