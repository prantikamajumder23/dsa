class Solution(object):
    def maxDepthAfterSplit(self, seq):
        ans=[]
        s=0
        for i in seq:
            if i =="(" :
                s+=1
                ans.append(s%2)
            if i ==")":
                ans.append(s%2)
                s-=1
        return ans 
      
        

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna