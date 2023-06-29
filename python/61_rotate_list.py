class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        temp = []

        curr = head

        while curr:
            temp.append(curr.val)
            curr = curr.next

        n = len(temp)

        if not n:
            return head

        if k % n == 0:
            return head

        shift = k % n

        temp = temp[n - shift:] + temp[:n - shift]

        head = curr = ListNode(temp[0])

        for data in temp[1:]:
            new_node = ListNode(data)
            curr.next = new_node
            curr = new_node

        return head
