## Mirror reverse a binary tree
## Iterative Approach using level order bfs traversal and swapping the children of a particular node
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def invertTree(self, root: TreeNode) -> TreeNode:
        if root == None:
            return
        ## initialize bfs queue with root
        q = [root]
        while q:
            curr = q[0]
            q.pop(0)
            curr.left, curr.right = curr.right, curr.left
            if curr.left:
                q.append(curr.left)
            if curr.right:
                q.append(curr.right)
        return root
        