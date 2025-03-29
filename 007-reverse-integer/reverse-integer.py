# Reverse Integer
# Given a signed 32-bit integer x, return x with its digits reversed.
# If reversing x causes the value to go outside the 32-bit integer range, return 0.
# Assume the environment does not allow storing 64-bit integers.

class Solution(object):
    def reverse(self, x):
        pos = True
        if x < 0:
            pos = False   
        x = str(abs(x))
        reversed_x = x[::-1]

        if int(reversed_x) > (2**31 - 1):
            return 0
        elif pos:
            return int(reversed_x)
        else:
            return -int(reversed_x)