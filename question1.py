# Merge strings alternately: https://leetcode.com/problems/merge-strings-alternately/

# Solution 1: 

# We want to iterate through the words and append each new char to the new word
class Solution(object):
    def mergeAlternately(self, word1, word2):
        """
        :type word1: str
        :type word2: str
        :rtype: str
        """
        newWord = ""
        length = max(len(word1), len(word2))

        for i in range(length):
            if len(word1) > (i): 
                newWord += word1[i]
            if len(word2) > (i):
                newWord += word2[i]

        return newWord

# Solution was accepted 
# Beats 73.10% of users with Python in Runtime
# Beats 91/83% of users with Python in Memory

# Possible improvements: once we reach the length of the shortest word, we don't need to continue to check the length. We could
# base the iteration off the min length instead and then append the rest of the longer word.