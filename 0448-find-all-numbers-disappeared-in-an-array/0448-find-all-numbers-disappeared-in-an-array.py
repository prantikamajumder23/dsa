class Solution(object):
    def findDisappearedNumbers(self, nums):
       n = len(nums)
       for i in range(n):
    
         index = abs(nums[i]) - 1
         nums[index] = -abs(nums[index])

       result = []
     
       for i in range(n):
         if nums[i] > 0:
            result.append(i + 1)

       return result
      
      
       

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna