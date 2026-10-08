class Solution(object):
    def removeOuterParentheses(self, s):
       count = 0 
       stack =[]
       for i in s :
         if i =='(':
            count +=1
            if count>1:
              stack.append(i)
            
                
         else:
            count -=1
            if count>0:
             stack.append(i)
        
       return ''.join(stack) 


        

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna