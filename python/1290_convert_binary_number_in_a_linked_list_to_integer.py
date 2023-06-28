class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def getDecimalValue(self, head: ListNode) -> int:
        bin_str = ''
        current = head

        while current:
            bin_str += str(current.val)
            current = current.next

        return int(bin_str, 2)
