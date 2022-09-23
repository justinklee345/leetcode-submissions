# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
def findLength(ln):
        iterator = ln
        count = 0
        while iterator is not None:
            count += 1
            iterator = iterator.next
        return count

class Solution:
    
    
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        oneLength = findLength(list1)
        twoLength = findLength(list2)
        to_return = ListNode()
        addIter = to_return
        oneIter = list1
        twoIter = list2
        for i in range(oneLength+twoLength):
            if oneIter is None and twoIter is None:
                break
            elif twoIter is None:
                addIter.next = oneIter
                addIter = addIter.next
                oneIter = oneIter.next
            elif oneIter is None:
                addIter.next = twoIter
                addIter = addIter.next
                twoIter = twoIter.next
            else:
                if oneIter.val <= twoIter.val:
                    addIter.next = oneIter
                    addIter = addIter.next
                    oneIter = oneIter.next
                else:
                    addIter.next = twoIter
                    addIter = addIter.next
                    twoIter = twoIter.next
        return to_return.next
        
