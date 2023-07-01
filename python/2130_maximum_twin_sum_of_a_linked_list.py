class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def pairSum(self, head: Optional[ListNode]) -> int:
        temp = []
        curr = head

        while curr:
            temp.append(curr.val)
            curr = curr.next

        twin_sum = temp[0] + temp[-1]

        for i in range(1, len(temp) // 2):
            twin_sum = max(twin_sum, temp[i] + temp[-i - 1])

        return twin_sum
