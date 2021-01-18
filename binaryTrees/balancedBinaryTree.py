from pprint import pprint
import unittest

class Node(object):
    def __init__(self, value ):
        self.value = value
        self.left = None
        self.right = None
'''
Determine if binary tree is height-balanced:
* The left and right subtree 
  of every node differ in height by no more than 1

        Ex: Balanced          3                           Ex:unbalanced        1
                            /  \                                              / \
        treeHeight(1)      9    20                         treeHeight(4)     2   2  treeHeight(1)
                               / \                                          / \
                               15  7 treeHeight(2)                         3   3
output : true                                                             / \        height = 4 - 1
Explaination: Diff from treeHeight(2) & treeHeight(1)= 1                 4   4
Traveral Type : Postorder Traveral                                                                       
                                                                       

'''         

def isBalancedSubtree(root):

    def dfs(root):
        if not root:
            return (0,True)
        
        #unpack returned value
        l_Height, isLeftbalanced = dfs(root.left)
        r_Height, isRightbalanced = dfs(root.right)

        #at the root node
        return (max(l_Height,r_Height) + 1 , isLeftbalanced and isRightbalanced and abs(l_Height - r_Height) <=  1)

    height, result = dfs(root)
    return result
    
class Test(unittest.TestCase):
    def test_isBalancedTreeTrue(self):
        tree = Node(1)
        tree.left = Node(2)
        tree.left.left = Node(2)
        tree.right = Node(3)
        tree.right.left = Node(4)
        tree.right.right = Node(5)
        
        self.assertTrue(isBalancedSubtree(tree))

    def test_isBalancedTreeFalse(self):
        tree = Node(1)
        tree.left = Node(2)
        tree.left.right = Node(3)
        tree.left.left = Node(3)
        tree.left.left.right = Node(4)
        tree.left.left.left = Node(4)

        
        self.assertFalse(isBalancedSubtree(tree))
    
  
if __name__ == "__main__":
    unittest.main()

         
# print(tree.right.value)
# print(isBalancedSubtree(tree))

            
if __name__ == "__main__":
  unittest.main()