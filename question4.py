# Reverse vowels of a string
# https://leetcode.com/problems/reverse-vowels-of-a-string/description/?envType=study-plan-v2&envId=leetcode-75

# Initial approach
# Loop through, need to save vowel and index to replace

class Solution(object):
    def reverseVowels(self, s):
        """
        :type s: str
        :rtype: str
        """
        vowels = "aeiou"
        vowels_found = []

        for i in range(len(s)):
            if s[i] in vowels:
                vowels_found.append(s[i])

        newString = ""
        for i in range(len(s)):
            if s[i] in vowels:
                newString += vowels_found.pop()
            else:
                newString += s[i]

        return newString
            
# Passed original tests but failed on aA
# Need to add capitals to vowel string

class Solution(object):
    def reverseVowels(self, s):
        """
        :type s: str
        :rtype: str
        """
        vowels = "aeiouAEIOU"
        vowels_found = []

        for i in range(len(s)):
            if s[i] in vowels:
                vowels_found.append(s[i])

        newString = ""
        for i in range(len(s)):
            if s[i] in vowels:
                newString += vowels_found.pop()
            else:
                newString += s[i]

        return newString
            

# Accepted! 
