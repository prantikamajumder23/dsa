class Solution(object):
    def getConcatenation(self, nums):
        ans=[]
        n=len(nums)
        for i in range(2*n):
            if i< n:
             ans.append(nums[i])
            else:
             ans.append(nums[i-n])
        return ans
            
    
        

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna