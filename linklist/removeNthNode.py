class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:

        dup = ListNode(0)
        dup.next = head
        sp = fp = dup
        
        for _ in range(n+1):
            fp = fp.next
        
        while fp:
            sp = sp.next
            fp = fp.next
        sp.next = sp.next.next
        return dup.next        