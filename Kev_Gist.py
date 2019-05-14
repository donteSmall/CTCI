#!/usr/bin/env python3

import unittest
import itertools

class Node(object):
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None



def binary_search_insert(root, new_value):
    if new_value < root.value:
        if root.left is None:
            root.left = Node(new_value)
        else:
            binary_search_insert(root.left, new_value)
    else:
        if root.right is None:
            root.right = Node(new_value)
        else:
            binary_search_insert(root.right, new_value)

def recursive_list_of_depths(root):
    this_depth = [[root.value]]
    if root.left and root.right:
        for pair in zip(list_of_depths(root.left), list_of_depths(root.right)):
            this_depth.append(pair[0] + pair[1])
        return this_depth
    elif root.left:
        return this_depth + list_of_depths(root.left)
    elif root.right:
        return this_depth + list_of_depths(root.right)
    else:
        return this_depth

def refactored_recursive_lod(root):
    this_depth = [[root.value]]
    left = []
    right = []

    if root.left:
        left = list_of_depths(root.left)
    if root.right:
        right = list_of_depths(root.right)

    for pair in itertools.zip_longest(left, right):
        # The ors here are just to handle None, which is how zip_longest pads the shorter iterable
        this_depth.append((pair[0] or []) + (pair[1] or []))

    return this_depth

def in_order_map_reduce(root, map_fn, reduce_fn):
    """Given a root note and a map and reduce function

    map_fn is passed a node's value to map
    reduce_fn is passed a list of [left_subtrees_reduction, this mapping, right_subtree_reduction]
              and expected to return a new reduction"""
    results = []

    if root.left:
        results.append(in_order_map_reduce(root.left, map_fn, reduce_fn))
    else:
        results.append(None)

    results.append(map_fn(root.value))

    if root.right:
        results.append(in_order_map_reduce(root.right, map_fn, reduce_fn))
    else:
        results.append(None)

    return reduce_fn(results)

def map_reduce_lod(root):
    def lod_map(value):
        """A single node's lod value is a list of one list containing this value"""
        return [[value]]

    def lod_reduce(left_this_right):
        """To combine the left and right subtrees with this value, we combine left and right's lists and append them to this value"""
        left, this, right = left_this_right
        for pair in itertools.zip_longest(left or [], right or []):
            this.append((pair[0] or []) + (pair[1] or []))
        return this

    return in_order_map_reduce(root, lod_map, lod_reduce)

# Change which function we're using for tests here
list_of_depths = map_reduce_lod
#list_of_depths = refactored_recursive_lod
#list_of_depths = recursive_list_of_depths




class BinaryTreeTest(unittest.TestCase):
    def test_node_created_with_value_has_that_value(self):
        node = Node(5)
        self.assertEquals(5, node.value)

    def test_node_unable_to_be_created_without_value(self):
        with self.assertRaises(TypeError):
            Node()

    def test_node_has_left_and_right_as_None_when_created(self):
        node = Node(5)
        self.assertIsNone(node.left)
        self.assertIsNone(node.right)

    def test_binary_search_insert_with_a_value_less_than_node_goes_left(self):
        root = Node(5)
        binary_search_insert(root, 4)
        self.assertEquals(4, root.left.value)
        self.assertIsNone(root.right)

    def test_binary_search_insert_with_a_value_more_than_node_goes_right(self):
        root = Node(5)
        binary_search_insert(root, 6)
        self.assertEquals(6, root.right.value)
        self.assertIsNone(root.left)

    def test_binary_search_insert_in_either_direction_more_than_once_goes_down_multiple_levels(self):
        root = Node(5)
        binary_search_insert(root, 4)
        binary_search_insert(root, 3)
        self.assertEquals(3, root.left.left.value)


    def test_list_of_depths_single_level(self):
        root = Node(5)
        self.assertEquals([[5]], list_of_depths(root))

    def test_list_of_depths_two_levels_one_side(self):
        root = Node(5)
        binary_search_insert(root, 4)
        self.assertEquals([[5], [4]], list_of_depths(root))

    def test_list_of_depths_two_levels_two_sides(self):
        root = Node(5)
        binary_search_insert(root, 4)
        binary_search_insert(root, 6)
        self.assertEquals([[5], [4, 6]], list_of_depths(root))

    def test_list_of_depths_multiple_levels(self):
        root = Node(5)
        binary_search_insert(root, 4)
        binary_search_insert(root, 3)
        binary_search_insert(root, 6)
        binary_search_insert(root, 7)

        self.assertEquals([[5], [4,6], [3,7]], list_of_depths(root))


if __name__ == '__main__':
    unittest.main()
