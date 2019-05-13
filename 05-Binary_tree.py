import unittest



class Queue(object):
    def __init__(self):
        self.items = []
    def enqueue(self,item):
        self.items.insert(0,item)
    def dequeue(self):
        if not self.is_empty():
            return self.items.pop()
    def is_empty(self):
        return len(self.items) == 0

    def peek(self):
       if not self.is_empty():
           return self.items[-1].value

    def __len__(slef):
        return len(self.items)
    def __repr__(self):
        return "Queue(%r)" % (self.items)


class Node(object):
    def __init__(self,value):
        self.value = value
        self.left = None
        self.right = None

    def __repr__(self):
        if self.left is None and self.right is None:
            s = '{}'.format(self.value)
        else:
            s = '[value:{}, left:{}, right:{}]'.format(self.value, self.left, self.right)
        return s

    def __iter__(self):

        if self.left != None:
            for elem in self.left:
                yield elem
        yield self.value

        if self.right != None:
            for elem in self.left:
                yield elem

    def __len__(self):
        total = 1
        if self.left is not None:
            total += self.left.__len__()
        if self.right is not None:
            total += self.right.__len__()
        return total

    def __getItem__(slef):
        return self.value


# def print_tree(self, traversal_type):
#     if traversal_type == "preOrder":
#         return self.preOrder(self.root,"")
#     elif traversal_type == "inOrder":
#         return self.inOrder(self.root, "")
#     elif traversal_type == "postOrder":
#         return self.postOrder(self.root, "")
#     else:
#         print("Traversal type " + str(traversal_type) + " is not supported.")
#         return False
#
# def preOrder(self,start, traversal):
#     # Root -> Left->Right
#     if start:
#         traversal += (str(start.value)+ "-")
#         traversal = self.preOrder(start.left,traversal)
#         traversal = self.preOrder(start.right,traversal)
#     return traversal
#
# def inOrder(self,start, traversal):
#     #  Left->Root ->Right
#     if start:
#         traversal = self.inOrder(start.left,traversal)
#         traversal += (str(start.value)+ "-")
#         traversal = self.inOrder(start.right,traversal)
#     return traversal
#
# def postOrder(self,start, traversal):
#     #  Left->Right -> Root
#     if start:
#         traversal = self.postOrder(start.left,traversal)
#         traversal = self.postOrder(start.right,traversal)
#         traversal += (str(start.value)+ "-")
#
#     return traversal

    # def __repr__(self):
    #     return "BinaryTree(%r)" % (self.root,self.left,self.right)

def insert(self, data):
    if self.root:
        if data < self.root:
            if self.left is None:
                self.left = Node(data)
            else:
                self.left.insert(data)
        elif data > self.root:
            if self.right is None:
                self.right = Node(data)
            else:
                self.right.insert(data)
        else:
            self.value= data

def inorderTraversal(root):
        result = []
        if root:
            result = inorderTraversal(root.left)
            result.append(root.value)
            result +=inorderTraversal(root.right)
        return result

def lod(bt):
    if bt.value is None:
        return
    explored = Queue()
    explored.enqueue(bt)
    explored_items = ""
    #levels= {}
    #explored.append(bt)
    while bt:
        explored_items += str(explored.peek()) + "-"
        node = explored.dequeue()

        if node is not None:
            if node.left :
                explored.enqueue(node.left)
            if node.right :
                explored.enqueue(node.right)


    return explored_items

    # if(bt.left is None):
    #     import pdb; pdb.set_trace()
    #     predecessor = bt.right
    #     queue.append(predecessor)
    #     visited.append(child)
    #     levels[predecessor] = levels[node]+1
    # else:
    #     predecessor = bt.left
    #     queue.append(predecessor)
    #     visited.append(predecessor)
    #     levels[predecessor] = levels[node]+1




tree = Node(8)
tree.left = Node(4)
tree.right = Node(10)
tree.left.left = Node(2)
tree.left.right = Node(6)
tree.right.right = Node(20)

reciever = lod(tree)
print("Data here :-> "+str(reciever ))


#        1
#     /     \
#    2       3
#   / \     /  \
#  4   5    6   7

class Test(unittest.TestCase):

    def test_preorder(self):
        tree = Node(1)
        tree.left = Node(2)
        tree.right = Node(3)
        tree.left.left = Node(4)
        tree.left.right = Node(5)
        tree.right.left = Node(6)
        tree.right.right = Node(7)
    #     self.assertEqual(tree.print_tree("preOrder"),'1-2-4-5-3-6-7-')
    #
    # def test_inorder(self):
    #     tree = BinaryTree(1)
    #     tree.root.left = Node(2)
    #     tree.root.right = Node(3)
    #     tree.root.left.left = Node(4)
    #     tree.root.left.right = Node(5)
    #     tree.root.right.left = Node(6)
    #     tree.root.right.right = Node(7)
    #     self.assertEqual(tree.print_tree("inOrder"),'4-2-5-1-6-3-7-')
    #
    # def test_postorder(self):
    #     tree = BinaryTree(1)
    #     tree.root.left = Node(2)
    #     tree.root.right = Node(3)
    #     tree.root.left.left = Node(4)
    #     tree.root.left.right = Node(5)
    #     tree.root.right.left = Node(6)
    #     tree.root.right.right = Node(7)
    #     self.assertEqual(tree.print_tree("postOrder"),'4-5-2-6-7-3-1-')

if __name__ == '__main__':
    unittest.main()
