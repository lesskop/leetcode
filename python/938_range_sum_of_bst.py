class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def rangeSumBST(self, root: TreeNode | None, low: int, high: int) -> int:
        stack = []
        result = 0

        while root or stack:
            while root:
                stack.append(root)
                root = root.left

            root = stack.pop()
            if low <= root.val <= high:
                result += root.val

            root = root.right

        return result
