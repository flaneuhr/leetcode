class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        memo = {}
        for i in range(len(nums)):
            need = target - nums[i]
            if need in memo:
                return [i, memo[need]]
            else: 
                memo[nums[i]] = i
