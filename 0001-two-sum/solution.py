class Solution:
    def twoSum(self, nums, target):
        """
        LeetCode Problem 1: Two Sum
        Given an array of integers nums and an integer target, return indices of the 
        two numbers such that they add up to target.

        :param nums: List[int] - list of integers
        :param target: int - target sum
        :return: List[int] - indices of the two numbers
        """
        num_map = {}  # Maps number to its index

        for i, num in enumerate(nums):
            diff = target - num
            if diff in num_map:
                return [num_map[diff], i]
            num_map[num] = i
        
        return []
