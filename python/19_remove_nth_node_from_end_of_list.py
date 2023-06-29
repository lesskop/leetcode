class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        temp = []
        curr = head

        while curr:
            temp.append(curr.val)
            curr = curr.next

        temp.pop(-n)

        if not temp:
            return None

        head = curr = ListNode(temp[0])

        for data in temp[1:]:
            new_node = ListNode(data)
            curr.next = new_node
            curr = new_node

        return head
