class Solution(object):
    def findMaxLength(self, nums):
       count = 0 
       maxlen =0 
       mp = {0:-1}
       for i in range (len(nums)):
        if nums[i]==0 :
            count -= 1
        else :
            count += 1 
        if count in mp :
            maxlen = max(maxlen ,i - mp[count])
        else:
            mp[count]=i
       return maxlen 


        

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna