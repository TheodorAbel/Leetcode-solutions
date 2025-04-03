class Solution(object):
    def isValid(self, s):
        rel={'}':'{',']':'[',')':'('}
        stack=[]
        for c in s:
            if c in rel:
                if not stack or  rel[c]!=stack.pop():
                    return False
            else:
                stack.append(c)
        return not stack
            

                   

            

                    



        
        