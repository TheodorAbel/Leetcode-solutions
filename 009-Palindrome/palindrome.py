class Solution(object):
    def isPalindrome(self, x):

        if abs(x)>=2**31-1 or x<0:
            return False
        else:
            orignal=x
            z=0
            while(x>0):
                y=x%10
                if x>9:
                    z=(z+y)*10
                else:
                    z=z+y
                x=x//10
            if z==orignal:
                return True
            else:
                 return False


        