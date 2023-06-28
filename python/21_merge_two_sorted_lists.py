class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        temp = []

        curr = list1

        while curr:
            temp.append(curr.val)
            curr = curr.next

        curr = list2

        while curr:
            temp.append(curr.val)
            curr = curr.next

        temp.sort()

        if not temp:
            return None

        head = ListNode(temp[0])

        curr = head

        for data in temp[1:]:
            new_node = ListNode(data)
            curr.next = new_node
            curr = new_node

        return head
