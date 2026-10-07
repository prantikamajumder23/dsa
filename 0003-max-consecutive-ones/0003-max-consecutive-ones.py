class Solution(object):
    def findMaxConsecutiveOnes(self, nums):
        count=0
        result=0
        for i in nums:
         if i== 1  :
             count +=1
             result = max(result,count)

         else :
             
             count = 0 
       
        return result

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna