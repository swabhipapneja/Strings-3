# Time Complexity : O(1) 
# Space Complexity : O(1), always dealing with 3 digits so we can ignore recursive stack space as well
# Did this code successfully run on Leetcode : Yes
# Any problem you faced while coding this : NA 

# Your code here along with comments explaining your approach:
# every set of 3 digits is processed together - first 3 are hundred, then million, then billion
# maintaing the words in the arrays
# recursively checking the words for every 3 digits by taking % 1000
# for every 3 digit number, - hundred + tens[i] + below_20[i] - recursively

class Solution(object):
    def __init__(self):
        self.thousands = ["", "Thousand", "Million", "Billion"]
        self.below_20 = ["", "One", "Two", "Three", "Four", "Five", "Six", "Seven", "Eight", "Nine", "Ten", "Eleven", "Twelve", "Thirteen", "Fourteen", "Fifteen", "Sixteen", "Seventeen", "Eighteen", "Nineteen"]
        self.tens = ["", "Ten", "Twenty", "Thirty", "Forty", "Fifty", "Sixty", "Seventy", "Eighty", "Ninety"]
    
    def numberToWords(self, num):
        """
        :type num: int
        :rtype: str
        """
        if num == 0:
            return "Zero"
        
        # to iterate over the thoudands array
        i = 0

        result = ""

        while num > 0:
            if num % 1000 != 0:
                result = self.recurse(num % 1000) + self.thousands[i] + " " + result
            i += 1
            num = num / 1000
        
        # to remove extra zeroes
        return result.strip()
    
    def recurse(self, num):
        if num == 0:
            return ""
        
        elif num < 20:
            return self.below_20[num] + " "
        
        elif num < 100:
            return self.tens[num / 10] + " " + self.recurse(num % 10)
        
        else:
            return self.below_20[num / 100] + " Hundred " + self.recurse(num % 100)



        