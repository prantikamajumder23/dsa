
class Solution(object):
    def isValid(self, s):
        stack=[]
        dict = {')':'('
        ,'}':'{',']':'['}
        for i in  s:
         if i in '({[':
             stack.append(i)
         else:
             if not stack:
                 return False
             if stack[-1]!= dict[i]:
                 return False
             stack.pop() 
        return len(stack)==0


       

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna