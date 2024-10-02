class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        slowPointer = head
        fastPointer = head

        while fastPointer and fastPointer.next:
            slowPointer = slowPointer.next
            fastPointer = fastPointer.next.next

            if slowPointer == fastPointer:
                return True
        return False