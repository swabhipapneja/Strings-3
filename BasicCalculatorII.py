# Time Complexity : O(n) 
# Space Complexity : O(1) 
# Did this code successfully run on Leetcode : Yes
# Any problem you faced while coding this : NA 

# Your code here along with comments explaining your approach:
# using tail to maintain the precedencce of operators
# traversing the given string
# if we get a digit - num changes to num * 10 + num
# if we get an operator - we have 4 choices
# if we get a + : calc changes to calc + num, tail changes to +num
# if we get a - : calc changes to calc - num, tail changes to -num
# if we get a * : calc changes to cal - tail + (tail * num) and tail changes to tail * num
# if we get a / : calc changes to cal - tail + (tail / num) and tail changes to tail / num


class Solution(object):
    def calculate(self, s):
        """
        :type s: str
        :rtype: int
        """

        if s is None:
            return 0
        
        # required variables
        calc = 0
        tail = 0
        num = 0
        lastSign = '+'

        # iterate over the given string
        for i in range(len(s)):
            c = s[i]
            # if c is a digit
            if c.isdigit():
                # num becomes old num * 10 + new num
                # rest everything remains same
                num = num * 10 + (ord(c) - ord('0'))

            # cannot use elif here because the character at the last index could be a digit too
            if (not c.isdigit() and c != ' ') or i == len(s) - 1:
                # condition for last index - evaluate the expression
                # character is an operator
                # now there can be 4 options
                if lastSign == '+':
                    calc = calc + num
                    tail = +num
                elif lastSign == '-':
                    calc = calc - num
                    tail = -num
                elif lastSign == '*':
                    calc = calc - tail + (tail * num)
                    tail = tail * num
                elif lastSign == '/':
                    if tail < 0:
                        calc = calc - tail + (-(-tail // num))
                        tail = -(-tail // num)
                    else:
                        calc = calc - tail + (tail // num)
                        tail = tail // num
                
                lastSign = c
                num = 0
        
        return calc

                    
                
                
        