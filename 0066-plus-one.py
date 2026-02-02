"""
LeetCode 2. Plus one
https://leetcode.com/problems/plus-one/

Difficulty: Easy
Topic: Array
"""
class Solution(object):
    def plusOne(self, digits):
        s=0
        for i in digits:
            s=10*s+i
        t=s+1
        res=[int(i) for i in str(t)]
        return res
