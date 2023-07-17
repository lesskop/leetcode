class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def addTwoNumbers(
        self, l1: Optional[ListNode], l2: Optional[ListNode]
    ) -> Optional[ListNode]:
        def get_num(node) -> int:
            num = ""

            while node:
                num += str(node.val)
                node = node.next

            return num

        num = str(int(get_num(l1)) + int(get_num(l2)))

        if not num:
            return None

        head = cur = ListNode(num[0])

        for digit in num[1:]:
            node = ListNode(digit)
            cur.next = node
            cur = node

        return head
