class Solution(object):
    def sumCounts(self, nums): 
        count = 0 
        distinct =[]
        for i in range(len(nums)):
            for j in range(i+1,len(nums)+1):
               
                    s = len(set(nums[i:j]))
                    count += s*s

        return count  

       

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna