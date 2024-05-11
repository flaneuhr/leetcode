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
            if memo.get(need, -1) != -1:
                return [i, memo[need]]
            else: 
                memo[nums[i]] = i
