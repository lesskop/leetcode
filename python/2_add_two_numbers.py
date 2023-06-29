class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        num1 = num2 = ''
        curr = l1

        while curr:
            num1 += str(curr.val)
            curr = curr.next

        num1 = int(num1[::-1])

        curr = l2

        while curr:
            num2 += str(curr.val)
            curr = curr.next

        num2 = int(num2[::-1])

        num = num1 + num2

        num = str(num)[::-1]

        head = curr = ListNode(int(num[0]))

        for data in num[1:]:
            new_node = ListNode(int(data))
            curr.next = new_node
            curr = new_node

        return head
