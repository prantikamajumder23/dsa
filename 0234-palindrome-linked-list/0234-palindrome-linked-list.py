
class ListNode(object):
     def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution(object):
    def isPalindrome(self, head):
        if not head or not head.next:
            return True

        slow = head
        fast = head
        prev = None

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        

        while slow:
            next_node = slow.next
            slow.next = prev
            prev = slow
            slow = next_node

        
        left = head
        right = prev

        while right:
            if left.val != right.val:
                return False

            left = left.next
            right = right.next

        return True
        

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna