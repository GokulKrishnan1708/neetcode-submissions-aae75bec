# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        index_map = {val: i for i, val in enumerate(inorder)}

        self.preorder_index = 0

        def build(left, right):
            if left > right:
                return None

            root_val = preorder[self.preorder_index]
            self.preorder_index += 1

            root = TreeNode(root_val)

            inorder_index = index_map[root_val]

            root.left = build(left, inorder_index - 1)
            root.right = build(inorder_index + 1, right)

            return root

        return build(0, len(inorder) - 1)