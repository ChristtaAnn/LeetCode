"""
LeetCode 1. Two Sum
https://leetcode.com/problems/two-sum/

Difficulty: Easy
Topics: Array, Hash Table
"""
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        l=len(nums)
        for i in range(l):
            x=nums[i]
            for j in range(l):
                if i!=j:
                    if nums[j]+x==target:
                        return [i,j]
