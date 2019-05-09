import unittest
class Node(object):
    def __init__(self,value):
        self.value = value
        self.left = None
        self.right = None

    def __repr__(self):
        return  str(self.value)


class BinaryTree(object):
    def __init__(self,root):
        #Assumes a value will be passed into the tree Node(root)
        self.root = Node(root)

    def print_tree(self, traversal_type):
        if traversal_type == "preOrder":
            return self.preOrder(self.root,"")
        elif traversal_type == "inOrder":
            return self.inOrder(self.root, "")
        elif traversal_type == "postOrder":
            return self.postOrder(self.root, "")
        else:
            print("Traversal type " + str(traversal_type) + " is not supported.")
            return False

    def preOrder(self,start, traversal):
        # Root -> Left->Right
        if start:
            traversal += (str(start.value)+ "-")
            traversal = self.preOrder(start.left,traversal)
            traversal = self.preOrder(start.right,traversal)
        return traversal

    def inOrder(self,start, traversal):
        #  Left->Root ->Right
        if start:
            traversal = self.inOrder(start.left,traversal)
            traversal += (str(start.value)+ "-")
            traversal = self.inOrder(start.right,traversal)
        return traversal

    def postOrder(self,start, traversal):
        #  Left->Right -> Root
        if start:
            traversal = self.postOrder(start.left,traversal)
            traversal = self.postOrder(start.right,traversal)
            traversal += (str(start.value)+ "-")

        return traversal

    def __repr__(self):
        return "--> " + str(self.root)


    def lod(self,bt):
        start = self.root
        explored = []
        queue = [start]
        levels= {}
        levels[start]=0
        visited= [start]
        if queue:
            node = queue.pop(0)
            explored.append(node)


            #parent = bt[node]
            import pdb; pdb.set_trace()
            for child in bt:
                if child not in visited:
                    queue.append(child)
                    visited.append(child)
                    levels[child] = levels[node]+1
        return explored





tree = BinaryTree(8)
tree.root.left = Node(4)
tree.root.right = Node(10)
tree.root.left.left = Node(2)
tree.root.left.right = Node(6)
tree.root.right.right = Node(20)

reciever = BinaryTree(tree).lod(tree)




#        1
#     /     \
#    2       3
#   / \     /  \
#  4   5    6   7

class Test(unittest.TestCase):

    def test_preorder(self):
        tree = BinaryTree(1)
        tree.root.left = Node(2)
        tree.root.right = Node(3)
        tree.root.left.left = Node(4)
        tree.root.left.right = Node(5)
        tree.root.right.left = Node(6)
        tree.root.right.right = Node(7)
        self.assertEqual(tree.print_tree("preOrder"),'1-2-4-5-3-6-7-')

    def test_inorder(self):
        tree = BinaryTree(1)
        tree.root.left = Node(2)
        tree.root.right = Node(3)
        tree.root.left.left = Node(4)
        tree.root.left.right = Node(5)
        tree.root.right.left = Node(6)
        tree.root.right.right = Node(7)
        self.assertEqual(tree.print_tree("inOrder"),'4-2-5-1-6-3-7-')

    def test_postorder(self):
        tree = BinaryTree(1)
        tree.root.left = Node(2)
        tree.root.right = Node(3)
        tree.root.left.left = Node(4)
        tree.root.left.right = Node(5)
        tree.root.right.left = Node(6)
        tree.root.right.right = Node(7)
        self.assertEqual(tree.print_tree("postOrder"),'4-5-2-6-7-3-1-')

if __name__ == '__main__':
    unittest.main()
#print(tree.print_tree("preOrder"))
#print(tree.print_tree("inorder"))
#print(tree.print_tree("postorder"))
