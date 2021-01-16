import unittest
from binary_tree_queue import Queue,Node

class binary_tree_tests(unittest.TestCase):
    def setUp(self):
        self.binaryTree = Node(None)
        self.FIFOQueue = Queue() 

    def test_preorder(self):
        tree = Node(1)
        tree.left = Node(2)
        tree.right = Node(3)
        tree.left.left = Node(4)
        tree.left.right = Node(5)
        tree.right.left = Node(6)
        tree.right.right = Node(7)
        self.assertEqual(tree.print_tree("preOrder"),'1-2-4-5-3-6-7-')
    
    def test_inorder(self):
        tree = Node(1)
        tree.left = Node(2)
        tree.right = Node(3)
        tree.left.left = Node(4)
        tree.left.right = Node(5)
        tree.right.left = Node(6)
        tree.right.right = Node(7)
        self.assertEqual(tree.print_tree("inOrder"),'4-2-5-1-6-3-7-')
    
    def test_postorder(self):
        tree = Node(1)
        tree.left = Node(2)
        tree.right = Node(3)
        tree.left.left = Node(4)
        tree.left.right = Node(5)
        tree.right.left = Node(6)
        tree.right.right = Node(7)
        self.assertEqual(tree.print_tree("postOrder"),'4-5-2-6-7-3-1-')

if __name__ == '__main__':
    unittest.main()
