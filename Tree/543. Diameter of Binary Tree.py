'''
543. Diameter of Binary Tree
Given a binary tree, you need to compute the length of the diameter of the tree. The diameter of a binary tree is the length of the longest path between any two nodes in a tree. This path may or may not pass through the root.

Example:
Given a binary tree
          1
         / \
        2   3
       / \     
      4   5    
Return 3, which is the length of the path [4,2,1,3] or [5,2,1,3].

Note: The length of path between two nodes is represented by the number of edges between them.
'''

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def diameterOfBinaryTree(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        self.p_len = 0    # 儲存當前最大探索路徑
        def depth(root):            
            if root == None:
                return 0                     # 深度 = 0
            else:                
                left, right = depth(root.left), depth(root.right)
                self.p_len = max(self.p_len, left+right)  # 更新當前最大探索路徑
                return 1 + max(left, right)  # 計算當前深度
        depth(root)
        return self.p_len  # 回傳最大探索路徑