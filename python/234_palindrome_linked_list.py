class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        temp = []
        curr = head

        while curr:
            temp.append(curr.val)
            curr = curr.next

        return temp == temp[::-1]
