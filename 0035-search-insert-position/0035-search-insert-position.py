class Solution(object):
    def searchInsert(self, nums, target):
        for i in range (len(nums)):
            if nums[i] == target:
                return i
            elif nums[i]> target :
                return i
           
        return len(nums)
            

        

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna