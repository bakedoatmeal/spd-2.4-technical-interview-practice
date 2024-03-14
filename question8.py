# Guess number higher or lower
# https://leetcode.com/problems/guess-number-higher-or-lower


# This is a binary search question
# To solve it, I guess the middle between the possible values each time
# narrowing the possible range by half 

# The guess API is already defined for you.
# @param num, your guess
# @return -1 if num is higher than the picked number
#          1 if num is lower than the picked number
#          otherwise return 0
# def guess(num):

class Solution(object):
    def guessNumber(self, n):
        """
        :type n: int
        :rtype: int
        """

        curr = n / 2
        min = 0
        max = n
        while n:
            result = guess(curr)
            if result == -1:
                max = curr
                curr = (max + min) / 2
            if result == 1:
                min = curr
                if max - min == 1:
                    curr = max
                else:
                    curr = (max + min) / 2
            if result == 0:
                return curr