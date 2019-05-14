#!/usr/bin/env python3

import unittest

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


def binary_search_insert(root, new_value):
    if root is None:
        raise TypeError()
    if new_value < root.value:
        if root.left:
            binary_search_insert(root.left, new_value)
        else:
            root.left = Node(new_value)
    else:
        if root.right:
            binary_search_insert(root.right, new_value)
        else:
            root.right = Node(new_value)


class BinaryTreeTest(unittest.TestCase):
    def test_node_created_with_value_has_that_value(self):
        node = Node(5)
        self.assertEqual(5, node.value)

    def test_node_unable_to_be_created_without_value(self):
        with self.assertRaises(TypeError):
            Node()

    def test_node_has_left_and_right_as_None_when_created(self):
        node = Node(5)
        self.assertIsNone(node.left)
        self.assertIsNone(node.right)

    def test_binary_search_insert_raises_if_no_root_given(self):
        with self.assertRaises(TypeError):
            binary_search_insert(None, 4)

    def test_binary_search_insert_when_value_is_less_than_root_inserts_left(self):
        root = Node(5)
        binary_search_insert(root, 4)
        self.assertEqual(4, root.left.value)
        self.assertIsNone(root.right)

    def test_binary_search_insert_when_value_is_greater_than_root_inserts_right(self):
        root = Node(5)
        binary_search_insert(root, 6)
        self.assertEqual(6, root.right.value)
        self.assertIsNone(root.left)

    def test_binary_search_insert_when_value_is_less_than_two_levels_down(self):
        root = Node(5)
        binary_search_insert(root, 4)
        binary_search_insert(root, 3)
        self.assertEqual(3, root.left.left.value)

    def test_binary_search_insert_when_value_is_greater_than_two_levels_down(self):
        root = Node(5)
        binary_search_insert(root, 6)
        binary_search_insert(root, 8)
        self.assertEqual(8, root.right.right.value)

def level_of_depth(root):
    if root is None:
        return []

    if root.left and root.right:
        # [[root.value]]
        # recurse left and right
        results = [[root.value]]
        for pair in zip(level_of_depth(root.left), level_of_depth(root.right)):
            # add items to results
            results.append(pair[0] + pair[1])
        return results

    if root.left:
        return [[root.value]] + level_of_depth(root.left)

    if root.right:
        #what do I contribute plus my children(recursion!!)
        return [[root.value]] + level_of_depth(root.right)

    return [[root.value]]

def count_Node(root):

    if root is None:
        return 0
    count = 1
    if root is not None:
        return count + count_Node(root.left) + count_Node(root.right)


def max_node(currentnode):
    if currentnode is None:
        return 0
    maxVal = currentnode.value
    leftNode= max_node(currentnode.left)
    rightNode= max_node(currentnode.right)
    if leftNode > maxVal:
        maxVal = leftNode

    if  maxVal < rightNode:
        maxVal = rightNode
    return maxVal

def min_node(root):
    current = root.value

    # If there is a left and right child, take the min value between nodes
    if root.left and root.right:
        if root.left.value < root.right.value:
            return min_node(root.left)

    if root.left:
        left = root.left
        return left.value

    return current


class min_nodeTest(unittest.TestCase):
    def test_when_there_is_one_node(self):
        root = Node(5)
        self.assertEqual(5, min_node(root))

    def test_when_there_is_two_nodes_in_binary_tree_the_min_is_returned(self):
        root = Node(6)
        binary_search_insert(root,4)
        binary_search_insert(root,9)
        self.assertEqual(4,min_node(root))

    def test_when_there_is_three_nodes_in_binary_tree_left_minVal_is_returned(self):
        root = Node(5)
        binary_search_insert(root,4)
        binary_search_insert(root,8)
        self.assertEqual(4,min_node(root))

    def test_when_there_is_three_nodes_in_binary_tree_left_minVal_is_returned(self):
        root = Node(7)
        binary_search_insert(root,4)
        binary_search_insert(root,2)
        binary_search_insert(root,9)

        self.assertEqual(2,min_node(root))



class max_nodeTest(unittest.TestCase):
    def test_when_there_is_no_binarytree_an_Zero_is_returned(self):
        self.assertEqual(0, max_node(None))

    def test_when_there_is_two_nodes_in_binary_tree_the_max_is_returned(self):
        root = Node(5)
        binary_search_insert(root,8)
        self.assertEqual(8,max_node(root))

    def test_when_there_is_three_nodes_max_is_returned(self):
        root = Node(5)
        binary_search_insert(root,4)
        binary_search_insert(root,3)
        binary_search_insert(root,79)
        self.assertEqual(79,max_node(root))

    def test_when_there_is_two_nodes_in_binary_tree_the_max_is_returned(self):
        root = Node(5)
        binary_search_insert(root,8)
        binary_search_insert(root,20)
        binary_search_insert(root,29)
        self.assertEqual(29,max_node(root))


class countNodesTest(unittest.TestCase):
    def test_when_there_is_no_binary_tree_an_Zero_is_returned(self):
        self.assertEqual(0, count_Node(None))

    def test_when_three_is_one_node_binary_tree_the_number_one_is_returned(self):
        self.assertEqual(1,count_Node(Node(5)))

    def test_when_there_is_two_nodes_in_binary_tree_the_number_two_is_returned(self):
        root = Node(5)
        binary_search_insert(root,4)
        self.assertEqual(2,count_Node(root))

    def test_when_there_is_root_and_left_in_binary_tree_two_is_returned(self):
        root = Node(5)
        binary_search_insert(root,6)
        self.assertEqual(2,count_Node(root))

    def test_when_there_is_four_Left_nodes_in_binary_tree_the_number_four_is_returned(self):
        root = Node(5)
        binary_search_insert(root,4)
        binary_search_insert(root,3)
        binary_search_insert(root,1)
        self.assertEqual(4,count_Node(root))

    def test_when_there_is_four_right_nodes_in_binary_tree_the_number_right_is_returned(self):
        root = Node(5)
        binary_search_insert(root,6)
        binary_search_insert(root,7)
        binary_search_insert(root,8)
        self.assertEqual(4,count_Node(root))



class LevelOfDepthTest(unittest.TestCase):
    def test_when_there_is_no_binary_tree_an_empty_list_is_returned(self):
        self.assertEqual([], level_of_depth(None))

    def test_when_there_is_one_node_binary_tree_a_list_of_list_isreturned(self):
        self.assertEqual([[5]],level_of_depth(Node(5)))

    def test_one_node_tree_with_a_different_value(self):
        self.assertEqual([[6]],level_of_depth(Node(6)))

    def test_root_with_a_left_child(self):
        root = Node(5)
        binary_search_insert(root, 4)

        self.assertEqual([[5], [4]], level_of_depth(root))

    def test_root_with_a_right_child(self):
        root = Node(5)
        binary_search_insert(root, 7)
        self.assertEqual([[5], [7]], level_of_depth(root))

    def test_root_with_a_left_and_right_child(self):
        root = Node(5)
        binary_search_insert(root, 4)
        binary_search_insert(root, 6)
        self.assertEqual([[5], [4, 6]], level_of_depth(root))

    def test_root_with_two_level_deep_left_children(self):
        root = Node(5)
        binary_search_insert(root, 4)
        binary_search_insert(root, 3)
        self.assertEqual([[5], [4], [3]], level_of_depth(root))

    def test_root_with_two_level_deep_right_children(self):
        root = Node(5)
        binary_search_insert(root,8)
        binary_search_insert(root, 10)
        self.assertEqual([[5],[8],[10]], level_of_depth(root))

    def test_root_with_both_left_and_right_children_multiple_deep(self):
        root = Node(5)
        binary_search_insert(root,4)
        binary_search_insert(root,3)
        binary_search_insert(root,7)
        binary_search_insert(root,8)
        self.assertEqual([[5],[4,7],[3,8]], level_of_depth(root))



if __name__ == '__main__':
    unittest.main()
