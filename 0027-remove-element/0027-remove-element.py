class Solution(object):
    def removeElement(self, nums, val):
        count = 0 
        i=0
     
        for i in range(len(nums)):

          if nums[i] != val :
            nums[count]= nums[i]
            count+=1
          
           
        return count
        
            

        

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna