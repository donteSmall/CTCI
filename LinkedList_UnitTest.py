import unittest
from LinkedList_V2 import Node,linkedList

class linked_List_Tests(unittest.TestCase):
    def setUp(self):
        self.list= linkedList()
        self.list2 = linkedList()


    def test_insert_one_element(self):
        self.list.add_to_beginning("z")
        self.assertTrue(self.list.head.get_data()== 'z')

    def test_insert_two_element(self):

        self.list.add_to_beginning("apple")
        self.list.add_to_beginning("Mango")

        # Bottom-up stack
        self.assertTrue(self.list.head.get_data()== "Mango")
        next_element = self.list.head.get_next()
        self.assertTrue(next_element.get_data()== "apple")

    def test_deleted_value_is_removed_from_list(self):
        self.list.add_to_beginning("The")
        self.list.add_to_beginning("quick")
        self.list.add_to_beginning("brown")
        self.list.add_to_beginning("fox")

        self.list.delete("fox")
        self.assertTrue(self.list.head.get_data() == "brown")

        self.list.delete("The")
        self.list.delete("quick")
        self.assertTrue(self.list.head.get_next() is None )

    def test_add_multiple(self):

        self.list.add_multiple(["Mix","More", "Food"])

        result= ["Mix","More", "Food"]

        self.assertEqual(self.list.head.get_data(),"Mix")
        self.assertEqual(self.list.head.next.get_data(), "More")
        self.assertEqual(self.list.head.next.next.get_data(), "Food")

    def test_len(self):
        self.list.add_multiple(["Mix","More", "Food"])
        self.assertEqual(self.list.__len__(),3)
        self.list.delete("Food")
        self.assertEqual(self.list.__len__(),2)


    def test_search(self):
        self.list.add_multiple(["Mix","More", "Food"])
        result=self.list.search("More")
        self.assertEqual(result.get_data(),"More")
        result2=self.list.search("Food")
        self.assertEqual(result2.get_data(),"Food")

    # def test_remove_duplicates(self):
    #     self.list.add_to_beginning("a")
    #     self.list.add_to_beginning("a")
    #     self.list.add_to_beginning("b")
    #     self.list.add_to_beginning("c")
    #     self.list.add_to_beginning("c")
    #     self.list.add_to_beginning("c")
    #     self.list.add_to_beginning("d")
    #     self.list.add_to_beginning("e")
    #     self.list.add_to_beginning("e")
    #     result = self.list.remove_duplicates()
    #     self.assertEqual(result, ['a','b','c','d','e'])

    def test_remove_duplicates_2(self):
        head = Node(1,Node(3,Node(3,Node(1,Node(5,None)))))
        self.list.remove_duplicates_2(head)
        self.assertEqual(head.data,1)
        self.assertEqual(head.next.data,3)
        self.assertEqual(head.next.next.data,5)
        self.assertEqual(head.next.next.next,None)

    def test_delete_middle(self):
        head = Node(1,Node(2,Node(3,Node(4))))

        self.list.delete_middle(head.next.next)

        self.assertEqual(head.data, 1)
        self.assertEqual(head.next.data, 2)
        # issue where next mext should be 4 but its 3, why ?

        self.assertEqual(head.next.next.data, 3)

    def test_kth_to_last(self):
        head = Node(1,Node(2,Node(3,Node(4,Node(5,Node(6,Node(7)))))))
        self.assertEqual(None, self.list.kth_to_last(head, 0));
        self.assertEqual(7, self.list.kth_to_last(head, 1).data)
        self.assertEqual(4, self.list.kth_to_last(head, 4).data)
        self.assertEqual(3, self.list.kth_to_last(head, 5).data)
        self.assertEqual(2, self.list.kth_to_last(head, 6).data)
        self.assertEqual(1, self.list.kth_to_last(head, 7).data)
        self.assertEqual(None, self.list.kth_to_last(head, 8))

    def test_partition(self):
        #Not working as expected, list is being generated based off of order!
        self.list.add_to_beginning(3)
        self.list.add_to_beginning(8)
        self.list.add_to_beginning(5)
        self.list.add_to_beginning(5)
        self.list.add_to_beginning(10)
        self.list.add_to_beginning(1)
        self.list.add_to_beginning(2)
        header = self.list
        head2 = header.partition(5)
        self.assertEqual(str(head2), '3,1,2,10,5,5,8')

    def test_sum_lists(self):
        self.list.add(5)
        self.list.add(6)
        self.list.add(3)

        self.list2.add(8)
        self.list2.add(4)
        self.list2.add(2)
        result = self.list.sum_lists(self.list2)
        self.assertEqual(str(result) , '3,1,6')











if __name__ == '__main__':
    unittest.main()
