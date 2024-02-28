# Add digits

# Semi brute force solution
class Solution:
    def addDigits(self, num: int) -> int:
        # brute force 
        if num < 10:
            return num 
        stringnumber = str(num)
        sum = int(stringnumber[0])
        for i in range(1, len(stringnumber)):
            sum += int(stringnumber[i])
            if sum >= 10:
                sum = int(str(sum)[0]) + int(str(sum)[1])
        return sum


# Passed but can use math to avoid string conversions - this would greatly improve runtime