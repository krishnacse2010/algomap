class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        current = head
        previous = None

        while current:
            forward = current.next
            current.next = previous
            previous = current
            current = forward
            
        
        return previous