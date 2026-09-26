
class Solution(object):
    def removeElements(self, head, val):
         dummy = ListNode(0)
         dummy.next = head

         current = dummy

         while current.next:
            if current.next.val == val:
                current.next = current.next.next
            else:
                current = current.next

         return dummy.next
        

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna