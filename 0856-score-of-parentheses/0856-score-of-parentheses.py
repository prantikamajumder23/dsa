class Solution(object):
    def scoreOfParentheses(self, s):
        
        stack=[0]
        for i in s :
            if i =='(':
                stack.append(0)
           
            else:
                result=stack.pop()
                if result == 0:
                    result =1
                else:
                    result = 2*result
                stack[-1] += result
                
            
                
        return stack[0]
        
        

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna