"""
LeetCode 3. Pallindrome Number
https://leetcode.com/problems/palindrome-number/

Difficulty: Easy
Topics: math manipulation,loops

without converting to str
"""

class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        if x>=0:
            t=0;s=x
            while x>0:
                t=t*10+x%10
                x=x//10
            if t==s:
                return True
            else:
                return False
        else:
            return False
