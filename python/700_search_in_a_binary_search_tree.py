class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    # # Recursive
    # def searchBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
    #     if not root or root.val == val:
    #         return root
    #
    #     return self.searchBST(root.left, val) if root.val > val else self.searchBST(root.right, val)

    # Iterative
    def searchBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        node = root

        while node:
            if node.val == val:
                return node
            elif node.val > val:
                node = node.left
            else:
                node = node.right

        return None
