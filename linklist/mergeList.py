class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        #List Node Class is assumed to be present
        dummy=ListNode(0)
        current = dummy
        
        while list1 and list2:
            if list1.val <= list2.val:
                current.next = list1
                current = list1
                list1=list1.next
            else:
                current.next = list2
                current = list2
                list2=list2.next
        while list1:
                current.next = list1
                current = list1
                list1=list1.next
        while list2:
                current.next = list2
                current = list2
                list2=list2.next
        return dummy.next