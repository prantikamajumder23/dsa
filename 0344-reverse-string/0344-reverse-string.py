class Solution(object):
    def reverseString(self, s):
        n = len(s)
        for i in range(n/2):
            m = s[i]
            s[i]=s[n-1-i]
            s[n-1-i]= m 
        return s 

        
        

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna