class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


# Dumb
class Solution:
    def deleteMiddle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        temp = []
        curr = head

        while curr:
            temp.append(curr.val)
            curr = curr.next

        temp.pop(len(temp) // 2)

        if not temp:
            return None

        head = curr = ListNode(temp[0])

        for data in temp[1:]:
            new_node = ListNode(data)
            curr.next = new_node
            curr = new_node

        return head


# Better
class Solution:
    def deleteMiddle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head.next:
            return None

        n = 0
        curr = head

        while curr:
            n += 1
            curr = curr.next

        middle = n // 2

        curr = head

        for _ in range(middle - 1):
            curr = curr.next

        curr.next = curr.next.next

        return head


# The best, slow and fast pointers
class Solution:
    def deleteMiddle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head.next:
            return None

        slow, fast = head, head.next.next

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        slow.next = slow.next.next

        return head
