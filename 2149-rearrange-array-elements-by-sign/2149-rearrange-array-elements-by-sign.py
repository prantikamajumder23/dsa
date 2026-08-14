class Solution(object):
    def rearrangeArray(self, nums):
        n= len(nums)
        ans=[0]* n 
        pos=0
        neg=1
        for i in nums :
            if(i >0):
                ans[pos]= i
                pos+=2
            else:
                ans[neg]= i
                neg+=2
        return ans
              

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna