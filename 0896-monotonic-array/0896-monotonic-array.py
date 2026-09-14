class Solution(object):
    def isMonotonic(self, nums):
       increase = True
       decrease = True
       for i in range(len(nums)-1):

         if nums[i] > nums[i+1]:
            increase = False
         elif nums[i]< nums[i+1]:
            decrease = False
       return increase or decrease 

        

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna