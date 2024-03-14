# Maximum Average Subarray I 
# https://leetcode.com/problems/maximum-average-subarray-i/description/?envType=study-plan-v2&envId=leetcode-75

# We know that this is a sliding window question based on the tags

# First approach: have two pointers and increment them one at a time
# Pointer 1 starts at 0, pointer 2 starts at k - 1 

class Solution(object):
    def findMaxAverage(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: float
        """
        max = 0
        current = 0
        
        for index in range(k):
            max += nums[index]
        
        current = max
        pointer1 = 0
        pointer2 = k

        while pointer2 < len(nums):
            current = current - nums[pointer1] + nums[pointer2]
            if current > max:
                max = current

            pointer1 += 1
            pointer2 += 1

        return max * 1.0 / k

# I'm not worrying about the average until the end since the highest sum will have the highest average

# Solution accepted