class Solution(object):
    def mySqrt(self, x):
       l =1 
       r =x
       while l<= r :
        m =  (l+r)//2

        if m*m == x :
            return m 
        elif m*m< x:
            l = m+1
        else :
            r = m-1
       return r 


# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna