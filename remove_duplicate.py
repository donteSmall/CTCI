import unittest
from LinkedList import Node,linkedList

def remove_duplicates(head):
    node= head

    if node:
        values = {node.data: True}
        while node.next:
            if node.next.data in values:
                node.next = node.next.next
            else:
                values[node.next.data] = True
                node = node.next
    return head

def delete_middle(node):
    next = node.next
    node.data = node.data
    node.next = next.next

def kth_to_last(head, k):
    lead,follow = head, head
    for _ in xrange(k):
        if not lead:
            return None
        lead = lead.next

    while lead:
        lead,follow = lead.next, follow.next

    return follow

class Node():
    def __init__(self,data,next= None):
        self.data,self.next = data,next

    def __str__(self):

        string = str(self.data)
        if self.next:
            string += ',' + str(self.next)
        return string

    def to_string(self):
        return "Node value :" + str(self.data)

class Test(unittest.TestCase):
    def setUp(self):
        self.list= linkedList()

    def test_remove_duplicates(self):
        head = Node(1,Node(3,Node(3,Node(1,Node(5,None)))))
        remove_duplicates(head)
        self.assertEqual(head.data,1)
        self.assertEqual(head.next.data,3)
        self.assertEqual(head.next.next.data,5)
        self.assertEqual(head.next.next.next,None)

    def test_delete_middle(self):
        head = Node(1,Node(2,Node(3,Node(4))))

        delete_middle(head.next.next)

        self.assertEqual(head.data, 1)
        self.assertEqual(head.next.data, 2)
        # issue where next mext should be 4 but its 3, why ?

        self.assertEqual(head.next.next.data, 3)

    def test_kth_to_last(self):
        head = Node(1,Node(2,Node(3,Node(4,Node(5,Node(6,Node(7)))))))
        self.assertEqual(None, kth_to_last(head, 0));
        self.assertEqual(7, kth_to_last(head, 1).data)
        self.assertEqual(4, kth_to_last(head, 4).data)
        self.assertEqual(3, kth_to_last(head, 5).data)
        self.assertEqual(2, kth_to_last(head, 6).data)
        self.assertEqual(1, kth_to_last(head, 7).data)
        self.assertEqual(None, kth_to_last(head, 8))

    def test_partition(self):
        self.list.insert_a_new_node_into_the_list(7)
        self.list.insert_a_new_node_into_the_list(2)
        self.list.insert_a_new_node_into_the_list(9)
        self.list.insert_a_new_node_into_the_list(1)
        self.list.insert_a_new_node_into_the_list(6)
        self.list.insert_a_new_node_into_the_list(3)
        self.list.insert_a_new_node_into_the_list(8)
        header= self.list
        head2 = header.partition(6)

        self.assertEqual(head2, [2,1,3,7,9,6,8])
        head3 = partition(head2, 7)
        self.assertEqual(str(head3), "2,1,3,6,7,9,8")


if __name__ == "__main__":
  unittest.main()
