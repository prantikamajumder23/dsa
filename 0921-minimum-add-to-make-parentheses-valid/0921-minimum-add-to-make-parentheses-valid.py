class Solution(object):
    def minAddToMakeValid(self, s):
        op=0
        cp=0
        for i in s :
            if i =='(':
                op+=1
            elif i ==')' and op> 0:
                op-=1
            else :
                cp+=1
            result = cp+op
        return result 



       

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna