# Greatest common divisor of strings
# https://leetcode.com/problems/greatest-common-divisor-of-strings/description/

# First approach: Iterate through two strings at once and return as soon as they deviate
# or one of them ends. 

# Solution 1: 

class Solution(object):
    def gcdOfStrings(self, str1, str2):
        divisor = ""

        for i in range(min(len(str1), len(str2))):
            if str1[i] == str2[i]: 
                divisor += str1[i]
            else:
                break

        return divisor

# Failed because this does not ensure that it's a common divisor.. 
# Perhaps we need to find the common divisor # based on the two lengths. 
# Check with each iteration if the length is a divisor of both strings! Else return

# Solution 2: 

class Solution(object):
    def gcdOfStrings(self, str1, str2):
        """
        :type str1: str
        :type str2: str
        :rtype: str
        """
        divisor = ""
        str1,str2 = (str1,str2) if len(str1) <= len(str2) else (str2,str1)

        for i in range(min(len(str1), len(str2))):
            if str1[i] == str2[i]: 
                divisor += str1[i]
            else:
                break

        for i in range(len(divisor)):
            mod = len(divisor)
            result1 = len(str1) % mod
            result2 = len(str2) % mod
            if result1 == 0 and result2 == 0:
                return divisor
            else: 
                divisor = divisor[:-1]

        return divisor

# We need to check for valid divisor
# We can do this by multiplying the proposed divisor * the length of the str/length divisor

class Solution(object):
    def gcdOfStrings(self, str1, str2):
        """
        :type str1: str
        :type str2: str
        :rtype: str
        """
        divisor = ""
        str1,str2 = (str1,str2) if len(str1) <= len(str2) else (str2,str1)

        for i in range(min(len(str1), len(str2))):
            if str1[i] == str2[i]: 
                divisor += str1[i]
            else:
                break

        for i in range(len(divisor)):
            mod = len(divisor)
            result1 = len(str1) % mod
            result2 = len(str2) % mod
            if result1 == 0 and result2 == 0:
                n1, n2 = len(str1) // mod, len(str2) // mod
                if divisor*n1 == str1 and divisor*n2 == str2:
                    return divisor
                else: 
                    divisor = divisor[:-1]
            else: 
                divisor = divisor[:-1]

        return divisor
